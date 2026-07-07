# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 08 - GroupBy & Aggregation
# =====================================================


# Sometimes we want to divide data into groups
# and calculate statistics for each group.
#
# For example,
#
# Average Marks of each Department
# Highest Salary in each Company
# Total Sales of each City
#
# groupby() creates groups,
# while aggregation functions such as
# mean(), sum(), max() and min()
# perform calculations on each group.

import pandas as pd

students = pd.DataFrame({

    "Department":["CS","CS","AI","AI","SE","SE"],

    "Marks":[82,75,91,60,87,78]

})

print(students)

# =====================================================
# Example 01 - groupby()
# =====================================================

print(

students.groupby("Department").sum()

)

# =====================================================
# Example 02 - Mean
# =====================================================

print(

students.groupby("Department").mean()

)

# =====================================================
# Example 03 - Maximum
# =====================================================

print(

students.groupby("Department").max()

)

# =====================================================
# Example 04 - Minimum
# =====================================================

print(

students.groupby("Department").min()

)

# =====================================================
# Example 05 - Count
# =====================================================

print(

students.groupby("Department").count()

)

# =====================================================
# Example 06 - Multiple Aggregations
# =====================================================

print(

students.groupby("Department").agg(

["min","max","mean","sum"]

)

)

