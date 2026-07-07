# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 09 - Pivot Tables
# =====================================================

# A Pivot Table summarizes large amounts
# of data into a small table.
#
# It helps us answer questions such as:
#
# Average Marks of each Department
# Total Sales by City
# Average Salary by Designation
#
# Pivot Tables are widely used in
# Excel, Pandas and Business Analytics.

import pandas as pd

students = pd.DataFrame({

    "Department":["CS","CS","AI","AI","SE","SE"],

    "Gender":["M","F","M","F","M","F"],

    "Marks":[82,75,91,60,87,78]

})

print(students)

# =====================================================
# Example 01 - Basic Pivot Table
# =====================================================

print(

students.pivot_table(

values="Marks",

index="Department"

)

)

# =====================================================
# Example 02 - Mean
# =====================================================

print(

students.pivot_table(

values="Marks",

index="Department",

aggfunc="mean"

)

)

# =====================================================
# Example 03 - Sum
# =====================================================

print(

students.pivot_table(

values="Marks",

index="Department",

aggfunc="sum"

)

)

# =====================================================
# Example 04 - Two-Level Pivot
# =====================================================

print(

students.pivot_table(

values="Marks",

index="Department",

columns="Gender"

)

)