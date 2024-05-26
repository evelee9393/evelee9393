Excel Project 1: 2023 Income and Expenses Analysis
---
Inspired by my expenditure-recording app, I have decided to replicate something similar using functions and PivotTable on Excel.

Major Findings
---
1. <b>Income:</b>A salary bump and more frequent tutoring increased my salary by 6.6%, comparing the Jan-May and August-Dec salaries. (Summer is always a bit tricky since there is technically no "salary."
2. <b>Expenditure:</b> <u>Health</u> and <u>Travelling</u> expenditures took up a little more than half of my spendings, which is reflected in the higher monthly expenditures in January and October, when I paid for Japan's hotel/flight ticket and pilates lessons, respectively.
3. <b>Missing Data:</b> I neglected to record it, which is always a problem when cleaning and processing data, but I usually give my parents 10K per month as a part of filial piety. This shows that data integrity is very important.


Figures
---
![image](https://github.com/evelee9393/ProjectsinProgress/assets/166385908/96173308-5307-43bc-adf5-e99fbc3c0756)
Figure 1. Total Income for 2023
![image](https://github.com/evelee9393/ProjectsinProgress/assets/166385908/a1f9cd3d-6d96-4ad6-9aa1-c0ae7e51e031)
Figure 2. Total Expenditure and its Breakdown for 2023
![image](https://github.com/evelee9393/ProjectsinProgress/assets/166385908/194b7a93-9300-4598-af88-f6943a01757f)
Figure 2a. Slicer for Month
![image](https://github.com/evelee9393/ProjectsinProgress/assets/166385908/ce9dafc5-62ad-459b-b409-f4fc833ae8a3)
Figure 2b. Slicer for Category

Process and Methods
---
<b>1. Data Preparation and Cleaning</b>
- Import: CSV file was converted to Excel
- Fixed: Several entries had error due to using 2 lines in memo
- Separate: using <b>Filter function</b>, Income and Expenses data were separated into 2 sheets
- Column/Row deletions:
  a) INCEXP column deleted from both sheets
  b) Created another row for Month, so information more easily examined by month
  c) Income only had Salary as Category, so it was exempted

<b>2. Data Visualization Methods: PivotTable and Graphs</b>
- Using PivotTable, an overview is examined for both Income and Expenses
  1) Income
  -  PivotChart Choice - Stacked Line Bar + Line for grand total
  -  PivotChart Fields -
     a) Axis: Month
     b) Values (Primary Axis): 2023 Salary
     c) Legend: Account (Bank or Cash)
     d) Calculated Field (Secondary Axis): Grand Total for each month = Bank + Cash items
        -->calculated Grand Total was needed to create a Secondary Axis

  2) Expenses
  -  PivotChart Choice - Pie Chart + 2 Slicers --> more easily view different categories and types of spending
     a) Slicer 1: Month
  -  b) Slicer 2: Category
  -  PivotChart Fields -
     a) Axis: Month
     b) Values (Primary Axis): 2023 Salary
     c) Legend: Account (Bank or Cash)
     d) Calculated Field (Secondary Axis): Grand Total for each month = Bank + Cash items
        -->calculated Grand Total was needed to create a Secondary Axis

<b>3. Further Calculations and Exploration</b>
- highest earning months
- highest spendings
- mean mode average of each
     
Challenges
---
- Changing color scheme of graphs was really difficult. I wanted to use different colors that made sense for me. After much Googling (and eliminating options that were too difficult for me now), I ended up selecting custom colors, which somehow does not change the graph's color when you change the view/slicer or when you update the table.
- Even though I created the graphs, more in-depth analysis still had to be done separately, letting me experience the difficulty of a data analyst and how all this comes together
- Admittedly, this is my first time doing this, so perhaps I did not present that many Major Findings. This is a work in progress.

Improvements for Next Time
---
1. With this project, it was merely trying to mimic what the app already does (breakdown of salary and expenditures, etc.) An original attempt of new findings/questions could perhaps direct this project better.
2. Going along with the previous point, ALWAYS START A PROJECT WITH YOUR END GOAL IN SIGHT. This includes:
  - What question do you want answered?
  - What kind of data do you need?
  - What kind of data visualization would be helpful for this?
3. It could be planned better, but as it has been a while since I tinkered with Excel, this was a nice warm up project to get back into the groove of things.
4. Next time, perhaps I'll try a dataset with more variables (to find differences) as well as using more real-life job scenarios to see what I can do with the information.
