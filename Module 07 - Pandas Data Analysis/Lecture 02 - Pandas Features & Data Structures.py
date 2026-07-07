# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 02 - Pandas Features & Data Structures & Differences
# =====================================================

# This lecture explains the important features of Pandas,
# its data structures, and why it is preferred over
# Python Lists, NumPy arrays and normal file handling.

import pandas as pd
import numpy as np

# =====================================================
# 1. Important Features of Pandas
# =====================================================

# Pandas Features:
# 1. Series              -> One-dimensional labeled data structure.
# 2. DataFrame           -> Two-dimensional table with rows and columns.
# 3. Indexing            -> Access data using labels or positions.
# 4. Automatic Alignment -> Aligns data using indexes.
# 5. Reading Files       -> Reads CSV, Excel, JSON, SQL etc.
# 6. Writing Files       -> Saves data to CSV, Excel, JSON etc.
# 7. Filtering           -> Select rows without loops.
# 8. Missing Values      -> Detects and fills missing values.
# 9. Sorting             -> Sort rows and columns.
# 10. Grouping           -> Summarize data using groupby().
# 11. Statistics         -> mean(), max(), min(), sum(), median() etc.
# 12. Data Cleaning      -> Remove duplicates and missing values.
# 13. NumPy Integration  -> Built on top of NumPy.
# 14. Visualization      -> Works with Matplotlib.
# 15. Machine Learning   -> Works with Scikit-learn, TensorFlow and PyTorch.

# =====================================================
# 2. Python List vs NumPy ndarray vs Pandas Series
# =====================================================

students = ["Ali","Ahmed","Sara"]
print(students)

numbers = np.array([82,74,91])
print(numbers)

marks = pd.Series([82,74,91], index=["Ali","Ahmed","Sara"])
print(marks)

# =====================================================
# 3. Series vs NumPy ndarray
# =====================================================

print(numbers[1])

print(marks["Sara"])

# NumPy uses numeric indexes.
# Pandas Series can use meaningful labels.

# =====================================================
# 4. When should we use Python Lists?
# =====================================================

# Use Lists for:
# - Small data
# - Learning Python
# - General Programming
# - Mixed Data Types
# - Simple Loops

students = ["Ali","Ahmed","Sara"]
print(students)

# =====================================================
# 5. When should we use NumPy Arrays?
# =====================================================

# Use NumPy for:
# - Numerical Computing
# - Mathematical Operations
# - Linear Algebra
# - Image Processing
# - Scientific Computing
# - Deep Learning

marks = np.array([82,74,91])

print(marks + 5)

# =====================================================
# 6. When should we use Pandas Series?
# =====================================================

# Use Series for:
# - Labeled Data
# - One Column of Data
# - CSV Files
# - Data Cleaning
# - Filtering
# - Statistics

marks = pd.Series(
    [82,74,91],
    index=["Ali","Ahmed","Sara"]
)

print(marks)

print(marks["Ahmed"])

# =====================================================
# 7. File Handling vs Pandas
# =====================================================

with open("students.csv","w") as file:
    file.write("Name,Marks,Department\n")
    file.write("Ali,82,CS\n")
    file.write("Ahmed,74,AI\n")
    file.write("Sara,91,SE\n")

print("\nUsing Normal File Handling")

with open("students.csv","r") as file:

    # next() skips the header.
    next(file)

    for line in file:

        # strip() removes newline.
        # split(',') converts string into list.

        data = line.strip().split(",")

        print(data[0],data[1],data[2])

print("\nUsing Pandas")

# read_csv() reads the CSV file and automatically
# creates a DataFrame.

students = pd.read_csv("students.csv")

print(students)

# =====================================================
# 8. Searching a Student
# =====================================================

print("\nSearching Using File Handling")

with open("students.csv","r") as file:

    next(file)

    for line in file:

        data = line.strip().split(",")

        if data[0] == "Ali":

            print(data)

print("\nSearching Using Pandas")

print(students[students["Name"]=="Ali"])

# =====================================================
# 9. Calculating Average
# =====================================================

print("\nAverage Using File Handling")

total = 0
count = 0

with open("students.csv","r") as file:

    next(file)

    for line in file:

        data = line.strip().split(",")

        total = total + int(data[1])

        count = count + 1

print(total/count)

print("\nAverage Using Pandas")

# mean() calculates average.

print(students["Marks"].mean())

# =====================================================
# 10. Filtering Passed Students
# =====================================================

print("\nPassed Students Using File Handling")

with open("students.csv","r") as file:

    next(file)

    for line in file:

        data = line.strip().split(",")

        marks = int(data[1])

        if marks >= 50:

            print(data)

print("\nPassed Students Using Pandas")

print(students[students["Marks"]>=50])

# =====================================================
# 11. Why Pandas is Essential for AI & ML
# =====================================================

# Imagine a CSV file containing millions of records.
#
# Using File Handling:
# - Read line by line
# - Split every line
# - Convert strings into numbers
# - Search using loops
# - Calculate statistics manually
# - Write many lines of code
#
# Using Pandas:
# - Read using one line
# - Filter without loops
# - Calculate statistics instantly
# - Handle missing values
# - Sort data
# - Group data
# - Prepare datasets for Machine Learning

big_data = pd.read_csv("students.csv")

print(big_data)

# =====================================================
# Summary
# =====================================================

# Python List
# - Small data
# - General programming

# NumPy Array
# - Numerical computing
# - Mathematical operations
# - Scientific computing

# Pandas Series / DataFrame
# - Data analysis
# - CSV files
# - Data cleaning
# - Machine Learning
