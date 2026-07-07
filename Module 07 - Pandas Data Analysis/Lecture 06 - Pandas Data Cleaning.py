# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 05 - Data Cleaning
# =====================================================

# Data Cleaning means finding and correcting
# incorrect, incomplete or duplicate data.
#
# Before applying Machine Learning algorithms,
# data should always be cleaned.

import pandas as pd
import numpy as np

# =====================================================
# Example 01 - Creating a DataFrame
# =====================================================

students = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara","Ali",None],

    "Marks":[82,np.nan,91,82,70],

    "Department":["CS","AI","SE","CS",None]

})

print(students)

# =====================================================
# Example 02 - Detect Missing Values
# =====================================================

# isnull() returns True where data is missing.

print(students.isnull())

# =====================================================
# Example 03 - Count Missing Values
# =====================================================

# sum() counts the total missing values.

print(students.isnull().sum())

# =====================================================
# Example 04 - Check if Any Missing Value Exists
# =====================================================

# any() checks whether missing values exist.

print(students.isnull().any())

# =====================================================
# Example 05 - Remove Rows Containing Missing Values
# =====================================================

# dropna() removes rows containing missing values.

new_students = students.dropna()

print(new_students)

# =====================================================
# Example 06 - Remove Columns Containing Missing Values
# =====================================================

# axis=1 removes columns instead of rows.

new_students = students.dropna(axis=1)

print(new_students)

# =====================================================
# Example 07 - Fill Missing Values
# =====================================================

# fillna() replaces missing values.

new_students = students.fillna("Unknown")

print(new_students)

# =====================================================
# Example 08 - Fill Numeric Missing Values
# =====================================================

new_students = students.copy()

new_students["Marks"] = new_students["Marks"].fillna(0)

print(new_students)

# =====================================================
# Example 09 - Fill Missing Values using Mean
# =====================================================

mean_marks = students["Marks"].mean()

students["Marks"] = students["Marks"].fillna(mean_marks)

print(students)

# =====================================================
# Example 10 - Detect Duplicate Rows
# =====================================================

# duplicated() returns True for duplicate rows.

print(students.duplicated())

# =====================================================
# Example 11 - Remove Duplicate Rows
# =====================================================

# drop_duplicates() removes duplicate rows.

students = students.drop_duplicates()

print(students)

# =====================================================
# Example 12 - Convert Data Types
# =====================================================

marks = pd.Series(["80","75","90"])

print(marks)

print(marks.dtype)

marks = marks.astype(int)

print(marks)

print(marks.dtype)

# =====================================================
# Example 13 - Convert Float to Integer
# =====================================================

numbers = pd.Series([82.5,74.2,91.8])

print(numbers)

numbers = numbers.astype(int)

print(numbers)

# =====================================================
# Example 14 - Replace Specific Values
# =====================================================

# replace() replaces one value with another.

students["Department"] = students["Department"].replace(

    "AI",

    "Artificial Intelligence"

)

print(students)

# =====================================================
# Example 15 - Rename Columns
# =====================================================

# rename() changes column names.

students = students.rename(

    columns={

        "Marks":"Student Marks"

    }

)

print(students)

# =====================================================
# Example 16 - Remove a Column
# =====================================================

# drop() removes rows or columns.

students = students.drop(

    columns=["Department"]

)

print(students)

# =====================================================
# Example 17 - Practical Example
# =====================================================

student_data = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara","Ahmed",None],

    "Marks":[82,np.nan,91,74,60],

    "Department":["CS","AI","SE","AI",None]

})

print("Original Data")

print(student_data)

print()

# Remove duplicate rows.

student_data = student_data.drop_duplicates()

# Replace missing names.

student_data["Name"] = student_data["Name"].fillna("Unknown")

# Replace missing departments.

student_data["Department"] = student_data["Department"].fillna("Not Assigned")

# Replace missing marks with average.

average_marks = student_data["Marks"].mean()

student_data["Marks"] = student_data["Marks"].fillna(average_marks)

print("Cleaned Data")

print(student_data)

# =====================================================
# Example 18 - Practical Example
# =====================================================

print()

print("Missing Values")

print(student_data.isnull().sum())

print()

print("Average Marks")

print(student_data["Marks"].mean())

print()

print("Highest Marks")

print(student_data["Marks"].max())

print()

print("Lowest Marks")

print(student_data["Marks"].min())

# =====================================================
# Example 19 - notnull()
# =====================================================

# notnull() returns True where data exists.

print(student_data.notnull())

# =====================================================
# Example 20 - Count Non-Missing Values
# =====================================================

# count() counts only non-missing values.

print(student_data.count())

# =====================================================
# Example 21 - Display Unique Values
# =====================================================

# unique() returns unique values.

print(student_data["Department"].unique())

# =====================================================
# Example 22 - Count Unique Values
# =====================================================

# nunique() counts unique values.

print(student_data["Department"].nunique())

# =====================================================
# Example 23 - Count Frequency
# =====================================================

# value_counts() counts occurrences of each value.

print(student_data["Department"].value_counts())

# =====================================================
# Example 24 - Sorting Data
# =====================================================

# sort_values() sorts DataFrame.

print(

student_data.sort_values(

    by="Marks"

)

)

# =====================================================
# Example 25 - Sorting in Descending Order
# =====================================================

print(

student_data.sort_values(

    by="Marks",

    ascending=False

)

)

# =====================================================
# Example 26 - Filling Missing Values Forward
# =====================================================

# ffill() copies previous value.

new_data = student_data.ffill()

print(new_data)

# =====================================================
# Example 27 - Filling Missing Values Backward
# =====================================================

# bfill() copies next value.

new_data = student_data.bfill()

print(new_data)

# =====================================================
# Example 28 - Practical Example
# =====================================================

student_data = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara","Ali",None],

    "Marks":[82,np.nan,91,82,70],

    "Department":["CS","AI","SE","CS",None]

})

print("Original Data")

print(student_data)

print()

# Remove duplicate rows.

student_data = student_data.drop_duplicates()

# Replace missing names.

student_data["Name"] = student_data["Name"].fillna("Unknown")

# Replace missing departments.

student_data["Department"] = student_data["Department"].fillna("Not Assigned")

# Replace missing marks using average.

student_data["Marks"] = student_data["Marks"].fillna(

    student_data["Marks"].mean()

)

# Sort marks.

student_data = student_data.sort_values(

    by="Marks",

    ascending=False

)

print("Cleaned Data")

print(student_data)

# =====================================================
# Useful Pandas Functions Used in This Lecture
# =====================================================

# isnull()           -> Detect missing values
# notnull()          -> Detect non-missing values
# sum()              -> Count missing values
# count()            -> Count non-missing values
# any()              -> Check if missing values exist
# dropna()           -> Remove missing values
# fillna()           -> Replace missing values
# ffill()            -> Forward fill missing values
# bfill()            -> Backward fill missing values
# duplicated()       -> Detect duplicate rows
# drop_duplicates()  -> Remove duplicate rows
# astype()           -> Convert data type
# replace()          -> Replace values
# rename()           -> Rename columns
# unique()           -> Display unique values
# nunique()          -> Count unique values
# value_counts()     -> Count frequency of values
# sort_values()      -> Sort DataFrame
# drop()             -> Remove rows or columns
# mean()             -> Average
# max()              -> Maximum
# min()              -> Minimum
# copy()             -> Create a copy

# =====================================================
# Summary
# =====================================================

# isnull()
# Detects missing values.

# dropna()
# Removes missing values.

# fillna()
# Replaces missing values.

# duplicated()
# Detects duplicate rows.

# drop_duplicates()
# Removes duplicate rows.

# astype()
# Converts data types.

# replace()
# Replaces existing values.

# rename()
# Renames columns.

# Data Cleaning is one of the most important
# steps before Data Analysis and Machine Learning.