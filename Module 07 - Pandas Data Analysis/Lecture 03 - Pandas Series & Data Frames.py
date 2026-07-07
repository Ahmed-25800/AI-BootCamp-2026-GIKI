# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 03 - Creating Pandas Series & DataFrames
# =====================================================

# Pandas provides two important data structures:
# 1. Series
# 2. DataFrame
#
# A Series stores one-dimensional labeled data.
# A DataFrame stores two-dimensional tabular data.

import pandas as pd
import numpy as np

# =====================================================
# Creating Pandas Series
# =====================================================

# =====================================================
# Example 01 - Series from a List
# =====================================================

# Series() converts a Python list into a Pandas Series.

marks = pd.Series([82,74,91,68,88])

print(marks)

# =====================================================
# Example 02 - Series with Custom Index
# =====================================================

# index assigns custom labels to each value.

marks = pd.Series(

    [82,74,91],

    index=["Ali","Ahmed","Sara"]

)

print(marks)

# =====================================================
# Example 03 - Accessing Series Elements
# =====================================================

# Elements can be accessed using labels or indexes.

print(marks["Ali"])

print(marks["Sara"])

print(marks[1])

# =====================================================
# Example 04 - Modifying Series Elements
# =====================================================

marks["Ahmed"] = 80

print(marks)

# =====================================================
# Example 05 - Series from Dictionary
# =====================================================

# Dictionary keys become indexes.

marks = pd.Series({

    "Ali":82,

    "Ahmed":74,

    "Sara":91

})

print(marks)

# =====================================================
# Example 06 - Series using NumPy Array
# =====================================================

numbers = np.array([10,20,30,40])

series = pd.Series(numbers)

print(series)

# =====================================================
# Example 07 - Creating Empty Series
# =====================================================

series = pd.Series(dtype=int)

print(series)

# =====================================================
# Example 08 - Series with Same Value
# =====================================================

series = pd.Series(

    100,

    index=["A","B","C","D"]

)

print(series)

# =====================================================
# Example 09 - Series Properties
# =====================================================

marks = pd.Series(

    [82,74,91],

    index=["Ali","Ahmed","Sara"]

)

print("Index")

print(marks.index)

print("Values")

print(marks.values)

print("Size")

print(marks.size)

print("Shape")

print(marks.shape)

print("Dimensions")

print(marks.ndim)

print("Data Type")

print(marks.dtype)

# =====================================================
# Example 10 - Practical Example
# =====================================================

student_marks = pd.Series(

    [82,74,91,68,88],

    index=["Ali","Ahmed","Sara","Bilal","Usman"]

)

print(student_marks)

print("Highest Marks:", student_marks.max())

print("Lowest Marks:", student_marks.min())

print("Average Marks:", student_marks.mean())

print("Total Marks:", student_marks.sum())

# =====================================================
# Creating DataFrames
# =====================================================

# =====================================================
# Example 11 - DataFrame from Dictionary
# =====================================================

students = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara"],

    "Marks":[82,74,91]

})

print(students)

# =====================================================
# Example 12 - DataFrame with Multiple Columns
# =====================================================

students = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara"],

    "Marks":[82,74,91],

    "Department":["CS","AI","SE"],

    "Semester":[3,5,7]

})

print(students)

# =====================================================
# Example 13 - DataFrame from List of Lists
# =====================================================

students = pd.DataFrame(

    [

        ["Ali",82,"CS"],

        ["Ahmed",74,"AI"],

        ["Sara",91,"SE"]

    ],

    columns=["Name","Marks","Department"]

)

print(students)

# =====================================================
# Example 14 - DataFrame from List of Dictionaries
# =====================================================

students = pd.DataFrame(

    [

        {"Name":"Ali","Marks":82},

        {"Name":"Ahmed","Marks":74},

        {"Name":"Sara","Marks":91}

    ]

)

print(students)

# =====================================================
# Example 15 - DataFrame using NumPy Array
# =====================================================

data = np.array([

    [1,"Ali",82],

    [2,"Ahmed",74],

    [3,"Sara",91]

])

students = pd.DataFrame(

    data,

    columns=["ID","Name","Marks"]

)

print(students)

# =====================================================
# Example 16 - DataFrame with Custom Index
# =====================================================

students = pd.DataFrame(

    {

        "Name":["Ali","Ahmed","Sara"],

        "Marks":[82,74,91]

    },

    index=["Student1","Student2","Student3"]

)

print(students)

# =====================================================
# Example 17 - DataFrame Properties
# =====================================================

print("Shape")

print(students.shape)

print("Dimensions")

print(students.ndim)

print("Size")

print(students.size)

print("Columns")

print(students.columns)

print("Index")

print(students.index)

print("Data Types")

print(students.dtypes)

# =====================================================
# Example 18 - Display Information
# =====================================================

# info() displays information about the DataFrame.

students.info()

# =====================================================
# Example 19 - Statistical Summary
# =====================================================

# describe() generates statistical summary.

print(students.describe())

# =====================================================
# Example 20 - Practical Example
# =====================================================

student_data = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara","Bilal","Usman"],

    "Marks":[82,74,91,68,88],

    "Department":["CS","AI","SE","CS","AI"]

})

print(student_data)

print()

print("Total Students")

print(len(student_data))

print()

print("Highest Marks")

print(student_data["Marks"].max())

print()

print("Lowest Marks")

print(student_data["Marks"].min())

print()

print("Average Marks")

print(student_data["Marks"].mean())

print()

print("Student Names")

print(student_data["Name"])

print()

print("Student Marks")

print(student_data["Marks"])

# |-----------------------------------------------------------------------|
# |            DIFFERENCE BETWEEN SERIES AND DATAFRAME                    |
# |-----------------------------------------------------------------------|
# | Feature              | Series                 | DataFrame             |
# |----------------------|------------------------|-----------------------|
# | Dimensions           | One                    | Two                   |
# | Stores               | Single Column          | Multiple Columns      |
# | Rows                 | Yes                    | Yes                   |
# | Columns              | No                     | Yes                   |
# | Index                | Yes                    | Yes                   |
# | Shape                | (n,)                   | (rows, columns)       |
# | Similar To           | Python List            | Excel Sheet           |
# | Used For             | Single Variable        | Complete Dataset      |
# |-----------------------------------------------------------------------|