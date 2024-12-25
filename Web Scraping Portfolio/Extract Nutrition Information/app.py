import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import matplotlib.font_manager as fm 

# 使用 FontProperties 建立字體屬性物件 - 以利plot graph時可顯示中文
ZHfont = fm.FontProperties(fname=r'./NotoSansCJK-DemiLight.ttc')

# Project Introduction and link to GitHub for deployment purposes
st.title("Data Visualization of Nutritional Information")
st.text("This is the Data Visualization part of a Nutritional Information Web Scraping Project by Eve Lee, who is looking for a career change in data analytics and backend development. The data was extracted from the 'frozen' foods of the processed  category of the Taiwan Food and Drug Administration (TFDA)'s database.")
st.markdown(
    'For more details on this project, please visit [my GitHub directory](https://github.com/evelee9393/evelee9393/tree/main/Web%20Scraping%20Portfolio/Extract%20Nutrition%20Information).',
    unsafe_allow_html=True
)
        
# PART 1: Load dataset with caching
def load_data():
    return pd.read_csv('FrozenFood_ExtractedNutrInfo.csv', encoding='utf-8')

df = load_data()

# PART 2: Function to calculate Health Score Rating (HSR)
def calculate_hsr(row):
    # Example calculation, adjust the logic as per your rating system
    rating = 0
    if row['熱量'] < 80:
        rating += 1
    if row['飽和脂肪'] < 4.5:
        rating += 1
    if row['糖質總量'] < 20.7:
        rating += 1
    if row['鈉'] < 90:
        rating += 1
    # Additional rating based on Protein and Fiber
    if row['粗蛋白'] > 4.8:
        rating += 1
    if row['膳食纖維'] > 2.1:
        rating += 1
    return rating

df['HSR'] = df.apply(calculate_hsr, axis=1)

# PART 3: Sidebar filters and data selection
st.sidebar.title('Filter Nutritional Data')
selected_filter = st.sidebar.selectbox('Select an Item', ['Average', *df['樣品名稱'].unique()])

# Display Selected Filter on Main Section
st.write(f"Selected Filter: {selected_filter}")

# PART 4: Filter data based on sidebar selection
def data_filter(df, filter_value):
    """
    Returns the data row to be plotted based on filter_value.
    If filter_value is 'Average', returns the average of numeric columns.
    Otherwise, returns the data for the specified filter_value.
    """
    if filter_value == 'Average':
        return df.select_dtypes(include=['number']).mean().round(2)
    else:
        # Filter by selected item and select first numeric row
        filtered_data = df[df['樣品名稱'] == filter_value].select_dtypes(include=['number'])
        if not filtered_data.empty:
            return filtered_data.iloc[0]
        else:
            st.warning("No numeric data available for the selected item.")
            return None

# Get data for filtering
st.session_state.data_filtered = data_filter(df, selected_filter)

# PART 5: SIDEBAR - Nutrition Information Table Section
def nutr_info():
    # Display filtered nutritional information
    if st.session_state.data_filtered is not None:
        dF = pd.DataFrame(st.session_state.data_filtered).reset_index()
        dF.columns = ['Nutrient', selected_filter]

        # Explicitly set the units column as string type
        units = ['kcal', 'g', 'g', 'g','g','g','g','g','g','mg', 'Score']
        dF['Unit per 100 g or ml'] = units[:len(dF)]
        
        # Return the DataFrame instead of displaying it directly
        return dF

# Generate the nutrition info DataFrame
nutrition_html = nutr_info().to_html(index=False)

st.sidebar.title("**Nutrition Information:**")
st.sidebar.markdown(nutrition_html, unsafe_allow_html=True)


# PART 6: Calculations for Graph (nutr_table function)
def nutr_table():
    # Step 1: Fetch DataFrame from nutr_info
    dF = pd.DataFrame(nutr_info())
    
    # Ensure dF is not None
    if dF is None or dF.empty:
        st.error("Data could not be fetched. Please check the nutr_info() function.")
        return None

    # Step 2: Define the targeted nutrients and recommended daily values (DRV)
    selected_nutrients = ['熱量', '粗蛋白', '飽和脂肪', '膳食纖維', '糖質總量', '鈉']
    DRV = [1800, 65, 20, 25, 45, 2300] #每日飲食建議 31-50歲, 男女不同取稍低活動的中間值

    # Step 3: Filter and check for selected nutrients in the DataFrame
    NutrTable = dF[dF['Nutrient'].isin(selected_nutrients)].copy().fillna(0) # fill NA as 0 to avoid graph issue

    # Step 4: Calculate Percent Daily Value (PDV)
    try:
        # Align DRV list with selected nutrients in case of filtering issues
        DRV_filtered = [DRV[selected_nutrients.index(nutr)] for nutr in NutrTable['Nutrient']]
        
        # Add PDV as new column
        NutrTable['PDV'] = (NutrTable[selected_filter].values / DRV_filtered) * 100 
        NutrTable['PDV'] = NutrTable['PDV'].round(2).fillna(0)  # Round PDV values, and  fill NA as 0 to avoid graph issue
    except Exception as e:
        st.error(f"Error calculating PDV: {e}")
        return None
    
    # Step 5: Return the result
    return NutrTable

# PART 7: Function to graph the nutrition information from nutr_table()
def nutr_graph():
    # Define colors
    bg_color = 'lightgray'
    progress_colors = ['blue', 'orange', 'brown', 'green', 'red', 'lightblue']

    # Create 3x2 grid of subplots
    fig, axes = plt.subplots(2, 3, figsize=(8, 6))
    axes = axes.ravel()  # Flatten axes array for easy indexing

    # Fetch dF from nutr_table()
    Nutr_Table = nutr_table() 
    Nutr_Table['Unit'] = Nutr_Table['Unit per 100 g or ml']

    for i, row in enumerate(Nutr_Table.itertuples()):
        # Define the value for the progress percentage
        Pvalue = getattr(row, 'PDV') # Get the percentage from the PDV(%) column
        value = row[2]
        unit = getattr(row, 'Unit')

        # Plot each nutrient's progress ring
        axes[i].pie(
                [Pvalue, 100 - Pvalue],
                startangle=90, 
                colors=[progress_colors[i], bg_color], 
                wedgeprops={'width': 0.3}
        )
        # Set title for each subplot with the nutrient name
        axes[i].set_title(row.Nutrient, fontproperties=ZHfont, fontsize=16) 

        # Annotate the pie chart with two lines in the center
        axes[i].text(
        0, 0.1, f"{Pvalue:.1f}% DV" if Pvalue != 0 else "No Info",  # The percentage in large font
        ha="center", va="center", fontsize=16, fontweight="bold"
        )
        axes[i].text(
        0, -0.1, f"{value} {unit}" if value != 0 else "No Info",  # The actual value in smaller font
        ha="center", va="center", fontsize=10, color="gray"
        )

    # Adjust layout
    fig.tight_layout()

    # Display in Streamlit
    st.pyplot(fig)

# PART 8: Function to show Health Score Rating meter, use nutr_info()
def HSR_meter():
    dF = pd.DataFrame(nutr_info()) # Fetch DataFrame from nutr_info()
    score = dF.loc[dF['Nutrient'] == 'HSR', selected_filter].values[0]

    # Set the meter color based on value
    bar_color = (
        "red" if score <= 1 else
        "orange" if score <= 2 else
        "yellow" if score <= 3 else
        "lightgreen" if score <= 4 else
        "green"
    )

    fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = score,
        mode = "gauge+number",
        gauge = {'axis': {'range': [None, 5]},
                 'bar': {'color': bar_color},
                 'steps' : [
                     {'range': [0, 2], 'color': "gray"},
                     {'range': [2, 3.5], 'color': "lightgray"}]
                }   
    ))

    # Add a custom title as an annotation beneath the value
    fig.update_layout(
        annotations=[
            go.layout.Annotation(
                text="Health Score Value",  # Title text
                x=0.5,  # Centered horizontally
                y=0.5,  # Position it just below the gauge
                showarrow=False,
                font=dict(size=20)
            )
        ]
    )

    st.plotly_chart(fig)

HSR_meter()
nutr_graph()