# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 01 - Introduction to Pandas
# =====================================================

# Pandas is one of the most popular Python libraries
# used for Data Analysis, Data Cleaning,
# Data Manipulation and Machine Learning.
#
# Pandas provides powerful data structures for
# storing and analyzing tabular data.
#
# The two most important data structures are:
# 1. Series
# 2. DataFrame

# =====================================================
# Installing Pandas
# =====================================================

# If Pandas is not installed on your computer,
# open Command Prompt or Terminal and type:

# use one of them
# pip install pandas
# conda install pandas

# =====================================================
# Importing Pandas
# =====================================================

# By convention, Pandas is imported using the alias pd.

import pandas as pd

print("Pandas Imported Successfully.")

# =====================================================
# Example 01 - Creating a Series
# =====================================================

# A Series is a one-dimensional data structure.

marks = pd.Series([82, 74, 91, 68, 88])

print(marks)

# =====================================================
# Example 02 - Type of Series
# =====================================================

print(type(marks))

# =====================================================
# Example 03 - Accessing Series Elements
# =====================================================

print(marks[0])

print(marks[2])

print(marks[4])

# =====================================================
# Example 04 - Creating a DataFrame
# =====================================================

# A DataFrame is a two-dimensional table
# containing rows and columns.

students = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara","Ayesha"],

    "Marks":[82,74,91,68]

})

print(students)

# =====================================================
# Example 05 - Type of DataFrame
# =====================================================

print(type(students))

# =====================================================
# Example 06 - Rows and Columns
# =====================================================

print("Rows and Columns")

print(students.shape)

# =====================================================
# Example 07 - Columns
# =====================================================

# columns returns the names of all columns.

print(students.columns)

# =====================================================
# Example 08 - Index
# =====================================================

# index returns the row numbers.

print(students.index)

# =====================================================
# Example 09 - Accessing One Column
# =====================================================

print(students["Name"])

print(students["Marks"])

# =====================================================
# Example 10 - Accessing Multiple Columns
# =====================================================

print(students[["Name","Marks"]])

# =====================================================
# Example 11 - Adding a New Column
# =====================================================

students["Department"] = ["CS","AI","SE","DS"]

print(students)

# =====================================================
# Example 12 - Modifying a Column
# =====================================================

students["Marks"] = [85,76,95,70]

print(students)

# =====================================================
# Example 13 - Information about DataFrame
# =====================================================

# info() displays information about the DataFrame.

students.info()

# =====================================================
# Example 14 - Statistical Summary
# =====================================================

# describe() displays statistical information.

print(students.describe())

# =====================================================
# Example 15 - Practical Example
# =====================================================

student_data = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara","Ayesha"],

    "Marks":[82,74,91,68],

    "Department":["CS","AI","SE","DS"]

})

print(student_data)

print("Student Names")

print(student_data["Name"])

print("Student Marks")

print(student_data["Marks"])

print("Total Students")

print(len(student_data))

# |-----------------------------------------------------------------------|
# |            DIFFERENCE BETWEEN SERIES AND DATAFRAME                    |
# |-----------------------------------------------------------------------|
# | Feature              | Series                 | DataFrame             |
# |----------------------|------------------------|-----------------------|
# | Dimensions           | One-Dimensional        | Two-Dimensional       |
# | Stores               | Single Column          | Multiple Columns      |
# | Rows                 | Yes                    | Yes                   |
# | Columns              | No                     | Yes                   |
# | Index                | Yes                    | Yes                   |
# | Data Types           | Usually One            | Multiple Allowed      |
# | Similar To           | Python List            | Excel Table           |
# |-----------------------------------------------------------------------|

# |-----------------------------------------------------------------------|
# |            DIFFERENCE BETWEEN NUMPY ARRAY AND PANDAS DATAFRAME        |
# |-----------------------------------------------------------------------|
# | Feature              | NumPy ndarray          | Pandas DataFrame      |
# |----------------------|------------------------|-----------------------|
# | Data Type            | Numerical Data         | Tabular Data          |
# | Rows & Columns       | No Labels              | Named Rows & Columns  |
# | Column Names         | Not Available          | Available             |
# | Index                | Numeric Only           | Custom Index Possible |
# | Data Types           | Usually Same Type      | Multiple Types        |
# | Speed                | Faster                 | Slightly Slower       |
# | Used In              | Numerical Computing    | Data Analysis         |
# | Machine Learning     | Yes                    | Yes                   |
# |-----------------------------------------------------------------------|