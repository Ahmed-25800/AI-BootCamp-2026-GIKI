# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 05 - Pandas Handling CSV Files
# =====================================================

# Data I/O means Data Input and Output.
#
# Input  -> Reading data from a file.
# Output -> Writing data into a file.
#
# Pandas provides built-in functions to easily
# read and write CSV files.

import pandas as pd

# =====================================================
# Example 01 - Creating a DataFrame
# =====================================================

print(
    """
=====================================================
Example 01 - Creating a DataFrame
=====================================================
"""
)

students = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara","Bilal"],

    "Marks":[82,74,91,68],

    "Department":["CS","AI","SE","DS"]

})

print(students)

# =====================================================
# Example 02 - Writing DataFrame to CSV
# =====================================================

# to_csv() writes a DataFrame into a CSV file.
#
# index=False prevents Pandas from writing
# row index numbers into the CSV file.
print(
    """
=====================================================
Example 02 - Writing DataFrame to CSV
=====================================================
"""
)

students.to_csv("students.csv", index=False)

print("CSV File Created Successfully.")

# =====================================================
# Example 03 - Reading CSV File
# =====================================================

# read_csv() reads a CSV file and
# creates a DataFrame automatically.

print(
    """
=====================================================
Example 03 - Reading CSV File
=====================================================
"""
)

students = pd.read_csv("students.csv")

print(students)

# =====================================================
# Example 04 - Display First Five Records
# =====================================================

# head() displays the first five rows.

print(
    """
=====================================================
Example 04 - Display First Five Records head() func
=====================================================
"""
)

print(students.head())

# =====================================================
# Example 05 - Display Last Five Records
# =====================================================

# tail() displays the last five rows.

print(
    """
=====================================================
Example 05 - Display Last Five Records tail() func
=====================================================
"""
)

print(students.tail())

# =====================================================
# Example 06 - Display Specific Number of Rows
# =====================================================

print(
    """
=====================================================
Example 06 - Display Specific Records using head & tail func
=====================================================
"""
)

print(students.head(2))

print(students.tail(2))

# =====================================================
# Example 07 - Display Column Names
# =====================================================

# columns returns all column names.
print(
    """
=====================================================
Example 07 - Display Column Names
=====================================================
"""
)

print(students.columns)

# =====================================================
# Example 08 - Display Row Index
# =====================================================

# index returns row indexes.
print(
    """
=====================================================
Example 08 - Display row indexes
=====================================================
"""
)

print(students.index)

# =====================================================
# Example 09 - Display Data Types
# =====================================================

# dtypes returns the data type of every column.

print(
    """
=====================================================
Example 09 - Display Data Types
=====================================================
"""
)

print(students.dtypes)

# =====================================================
# Example 10 - Display Information
# =====================================================

# info() displays information about the DataFrame.

print(
    """
=====================================================
Example 10 - Display Data-Frame Info using info func
=====================================================
"""
)

students.info()

# =====================================================
# Example 11 - Statistical Summary
# =====================================================

# describe() displays statistical information
# about numeric columns.

print(
    """
=====================================================
Example 11 - Display Statistical Summary using describe() func
=====================================================
"""
)

print(students.describe())

# =====================================================
# Example 12 - Reading Selected Columns
# =====================================================

# usecols reads only selected columns.

print(
    """
=====================================================
Example 12 - Reading Selected Columns
=====================================================
"""
)

students = pd.read_csv(

    "students.csv",

    usecols=["Name","Marks"]

)

print(students)

# =====================================================
# Example 13 - Reading Limited Rows
# =====================================================

# nrows reads only specified number of rows.

print(
    """
=====================================================
Example 13 - nrows reads only specified number of rows
=====================================================
"""
)

students = pd.read_csv(

    "students.csv",

    nrows=2

)

print(students)

# =====================================================
# Example 14 - Adding a New Student
# =====================================================

print(
    """
=====================================================
Example 14 - Adding new Student & combining two data frames using concat()
=====================================================
"""
)

students = pd.read_csv("students.csv")

new_student = pd.DataFrame({

    "Name":["Usman"],

    "Marks":[88],

    "Department":["CS"]

})

# concat() combines two DataFrames.

students = pd.concat(

    [students,new_student],

    ignore_index=True

)

print(students)

# =====================================================
# Example 15 - Saving Updated Data
# =====================================================

print(
    """
=====================================================
Example 15 - Saving Updated Data
=====================================================
"""
)

students.to_csv(

    "students.csv",

    index=False

)

print("Updated File Saved.")

# =====================================================
# Example 16 - Practical Example
# =====================================================

print(
    """
=====================================================
Example 16 - Practical Example
=====================================================
"""
)

students = pd.read_csv("students.csv")

print("Student Names")

print(students["Name"])

print()

print("Student Marks")

print(students["Marks"])

print()

print("Average Marks")

print(students["Marks"].mean())

print()

print("Highest Marks")

print(students["Marks"].max())

print()

print("Lowest Marks")

print(students["Marks"].min())

# =====================================================
# Example 17 - Practical Example
# =====================================================

print(
    """
=====================================================
Example 17 - Practical Example
=====================================================
"""
)

students = pd.read_csv("students.csv")

print("Complete Dataset")

print(students)

students.to_csv(

    "student_backup.csv",

    index=False

)

print()

print("Backup File Created Successfully.")

# =====================================================
# Example 18 - Reading Specific Columns
# =====================================================

# usecols reads only the specified columns.

print(
    """
=====================================================
Example 18 - Reading Specific Columns
=====================================================
"""
)

students = pd.read_csv(

    "students.csv",

    usecols=["Name","Marks"]

)

print(students)

# =====================================================
# Example 19 - Reading Limited Rows
# =====================================================

# nrows reads only the required number of rows.

print(
    """
=====================================================
Example 19 - Reading Specific Rows
=====================================================
"""
)

students = pd.read_csv(

    "students.csv",

    nrows=3

)

print(students)

# =====================================================
# Example 20 - Skipping Rows
# =====================================================

# skiprows skips the specified rows.

print(
    """
=====================================================
Example 20 - Skipping Rows
=====================================================
"""
)

students = pd.read_csv(

    "students.csv",

    skiprows=2

)

print(students)

# =====================================================
# Example 21 - Reading Without Header
# =====================================================

# header=None tells Pandas that the file
# does not contain column names.

print(
    """
=====================================================
Example 21 - Reading Without Header
=====================================================
"""
)

students = pd.read_csv(

    "students.csv",

    header=None

)

print(students)

# =====================================================
# Example 22 - Assigning Column Names
# =====================================================

# names assigns new column names.

print(
    """
=====================================================
Example 22 - Assigns new column names.
=====================================================
"""
)

students = pd.read_csv(

    "students.csv",

    header=None,

    names=["Student Name","Marks","Department"]

)

print(students)

# =====================================================
# Example 23 -
# =====================================================

# index_col selects a column to become
# the row index.

print(
    """
=====================================================
Example 23 - Setting an Index Column
=====================================================
"""
)

students = pd.read_csv(

    "students.csv",

    index_col="Name"

)

print(students)

# =====================================================
# Example 24 - Reading Selected Data Types
# =====================================================

# dtype specifies the data type
# of columns.

print(
    """
=====================================================
Example 24 - Reading Selecte Data Types
=====================================================
"""
)

students = pd.read_csv(

    "students.csv",

    dtype={"Marks":float}

)

print(students)

print(students.dtypes)

# =====================================================
# Example 25 - Handling Missing Values
# =====================================================

# na_values converts specified values
# into NaN.

print(
    """
=====================================================
Example 25 - Handling Missing Values
=====================================================
"""
)

students = pd.read_csv(

    "students.csv",

    na_values=["NA"]

)

print(students)

# =====================================================
# Example 26 - Saving Without Index
# =====================================================

print(
    """
=====================================================
Example 26 - Saving Without Index
=====================================================
"""
)

students.to_csv(

    "students_copy.csv",

    index=False

)

print("File Saved.")

# =====================================================
# Example 27 -
# =====================================================

print(
    """
=====================================================
Example 27 - Saving Selected Columns
=====================================================
"""
)

students.to_csv(

    "student_marks.csv",

    columns=["Name","Marks"],

    index=False

)

print("Selected Columns Saved.")

# =====================================================
# Example 28 - Changing Separator
# =====================================================

# sep changes the separator.

print(
    """
=====================================================
Example 28 - Changing Separator
=====================================================
"""
)

students.to_csv(

    "students_semicolon.csv",

    sep=";",

    index=False

)

print("Semicolon Separated File Created.")

# =====================================================
# Example 29 - Practical Example
# =====================================================

print(
    """
=====================================================
Example 29 - Pracitcal Example
=====================================================
"""
)

students = pd.read_csv("students.csv")

print(students)

print()

print("Total Students")

print(len(students))

print()

print("Highest Marks")

print(students["Marks"].max())

print()

print("Lowest Marks")

print(students["Marks"].min())

print()

print("Average Marks")

print(students["Marks"].mean())

# =====================================================
# Useful Pandas Functions Used in This Lecture
# =====================================================

# read_csv()    -> Reads a CSV file
# to_csv()      -> Writes DataFrame into CSV
# head()        -> Displays first rows
# tail()        -> Displays last rows
# info()        -> Displays DataFrame information
# describe()    -> Displays statistical summary
# columns       -> Returns column names
# index         -> Returns row indexes
# dtypes        -> Returns data type of each column
# concat()      -> Combines DataFrames
# mean()        -> Calculates average
# max()         -> Returns maximum value
# min()         -> Returns minimum value

# =====================================================
# Summary
# =====================================================

# read_csv()
# Used to read CSV files.

# to_csv()
# Used to save DataFrames as CSV files.

# head()
# Displays first rows.

# tail()
# Displays last rows.

# info()
# Displays complete DataFrame information.

# describe()
# Displays statistical summary.

# concat()
# Combines multiple DataFrames.

# Pandas makes reading and writing CSV files
# much easier than normal Python file handling.