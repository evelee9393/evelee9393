# Python vs. Pandas: Comparison using Kaggle Chipotle Data
While practicing with [recommended Kaggle Pandas Exercises](https://www.kaggle.com/discussions/getting-started/120274) to become more familiar with pandas, I was reminded when I first used pandas, and the Instructor say how much easier it is to compute via pandas than Python. This article is a result of my ramblings and comparison.
The whole completed practice is made possible with credit to Kaggle and https://github.com/justmarkham for sharing the dataset and materials.
The Jupyter Notebook for this Chipotle Pandas Exercise can be found here.

## Dataset
The [Chipotle dataset](https://www.kaggle.com/discussions/getting-started/120274) contains the sales data of a Chipotle restaurant, with which there are columns for:
1. order_id - identifier, indexed from 1 to 1834, for each order
2. quantity - quantity of each item in the order
3. item_name
4. choice_description - details of the order, such as the filling of a chicken bowl/taco and the flavor of the drink.
5. item_price - may vary depending on item and choice_description

There are in total 4622 rows.
Already, the information of this dataset was easily extracted using pandas built-in modules, such as '.shape[]', '.head()', '.info()'

## Task for Comparison
Step 9: Which was the most-ordered item
We shall see the difference between using Pandas and Python, using Step 9 as an example

## Pandas
pandas uses functions similar to SQL, which makes it useful in data analysis. In this case, the code is executed in the steps below to get the most-ordered item:
1. pandas performs groupby() method, used similarly to SQL's GROUP BY operations, on 'item_name'.
2. Aggregation is then used to get the sum of 'quantity' for each 'item_name'
3. The summed quantity of the items is sorted by descending order
4. Print the top 5 items
```
o = chipo.groupby("item_name")
o = o.sum()
o = o.sort_values(['quantity'], ascending=False)
o.head(5)
```

## Python using csv
Meanwhile, without using pandas, just using Python's csv would require the steps below:
1. a) Load and read the data from URL 
b) and create a dictionary to store the total quantity for each item
2. Read the data from the URL and parse the item_name and quantity with a for loop
3. Update the dictionary manually
4. Find the most ordered item
5. Print the most ordered item and its total quantity

```
import csv

# Step 1 a): Load and read the data from the URL
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

# Step 1 b):Use a  dictionary to store the total quantity for each item
item_orders = {}

# Step 2: Read the data from the URL and parse the item_name and quantity with a for loop
with open(url, 'r') as file:
    reader = csv.DictReader(file, delimiter='\t')
    
    for row in reader:
        item_name = row['item_name']
        quantity = int(row['quantity'])
        
        # Step 3: Update the dictionary manually
        if item_name in item_orders:
            item_orders[item_name] += quantity
        else:
            item_orders[item_name] = quantity

# Step 4: Find the most ordered item
most_ordered_item = max(item_orders.items(), key=lambda x: x[1])

# Print the most ordered item and its total quantity
print(f"The most ordered item is '{most_ordered_item[0]}' with a total of {most_ordered_item[1]} orders.")
```

## Conclusion
Reviewing this has made me realize that both methods are equally important because:
1. Python code may be a more arduous process, but it goes back to the basic concepts of coding and how the computer processes the data.
2. pandas will be useful when datasets get larger, and you can combine functions from different types of code (such as SQL).
Thank you for reading through this, as I take some time to record my learning journey. 
