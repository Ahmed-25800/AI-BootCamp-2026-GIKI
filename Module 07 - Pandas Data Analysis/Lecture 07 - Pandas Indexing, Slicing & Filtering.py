# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 07 - Part - 1 Selecting, Indexing, Slicing
# =====================================================

# Selecting data means accessing rows or columns
# from a DataFrame.

# A DataFrame may contain thousands or even millions
# of rows and columns.
#
# In most situations, we do not need the complete data.
# Instead, we select only the required rows or columns.
#
# Pandas provides several ways to access data such as:
#
# 1. Selecting Columns
# 2. Selecting Rows
# 3. Indexing
# 4. Slicing
# 5. loc[]
# 6. iloc[]
#
# These techniques are heavily used in
# Data Analysis, Machine Learning and AI.


import pandas as pd

students = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara","Bilal","Usman"],

    "Marks":[82,74,91,68,87],

    "Department":["CS","AI","SE","DS","CS"]

})

print(students)

# =====================================================
# Example 01 - Selecting One Column
# =====================================================

print(students["Name"])

# =====================================================
# Example 02 - Selecting Multiple Columns
# =====================================================

print(

students[["Name","Marks"]]

)

# =====================================================
# Example 03 - Selecting First Row
# =====================================================

# iloc uses integer index.

print(

students.iloc[0]

)

# =====================================================
# Example 04 - Selecting Multiple Rows
# =====================================================

print(

students.iloc[0:3]

)

# =====================================================
# Example 05 - Selecting Specific Rows & Columns
# =====================================================

print(

students.iloc[0:3,0:2]

)

# =====================================================
# Example 06 - Selecting Rows using Labels
# =====================================================

students.index=["A","B","C","D","E"]

print(

students.loc["A"]

)

# =====================================================
# Example 07 - Selecting Multiple Labels
# =====================================================

print(

students.loc[["A","C","E"]]

)

# =====================================================
# Example 08 - Selecting Label Range
# =====================================================

print(

students.loc["A":"C"]

)

# =====================================================
# Example 09 - Column Slicing
# =====================================================

print(

students.loc[:,"Name":"Marks"]

)

# =====================================================
# Example 10 - Practical Example
# =====================================================

print(

students.iloc[1:4,[0,2]]

)

# =====================================================
# Useful Pandas Functions
# =====================================================

# []
# loc[]
# iloc[]


# ========================================================================
# Lecture 07 - Part 2 - Filtering Data
# ========================================================================

# Filtering means selecting only those rows
# that satisfy a given condition.
#
# Instead of using loops, Pandas allows us
# to filter data using simple conditions.
#
# Filtering is one of the most frequently
# used operations in Data Analysis,
# Machine Learning and Artificial Intelligence.

import pandas as pd

students = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara","Bilal","Usman"],

    "Marks":[82,74,91,68,87],

    "Department":["CS","AI","SE","DS","CS"]

})

print(students)

# =====================================================
# Example 01 - Marks Greater Than 80
# =====================================================

print(

students[students["Marks"]>80]

)

# =====================================================
# Example 02 - Marks Less Than 80
# =====================================================

print(

students[students["Marks"]<80]

)

# =====================================================
# Example 03 - Equal To
# =====================================================

print(

students[students["Department"]=="CS"]

)

# =====================================================
# Example 04 - AND Condition
# =====================================================

print(

students[

(students["Marks"]>80)

&

(students["Department"]=="CS")

]

)

# =====================================================
# Example 05 - OR Condition
# =====================================================

print(

students[

(students["Department"]=="AI")

|

(students["Department"]=="SE")

]

)

# =====================================================
# Example 06 - NOT Condition
# =====================================================

print(

students[

students["Department"]!="CS"

]

)

# =====================================================
# Example 07 - isin()
# =====================================================

print(

students[

students["Department"].isin(["CS","SE"])

]

)

# =====================================================
# Example 08 - between()
# =====================================================

print(

students[

students["Marks"].between(70,90)

]

)

# =====================================================
# Example 09 - Practical Example
# =====================================================

passed = students[students["Marks"]>=50]

print(passed)