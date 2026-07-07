# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 12 - Preparing Datasets for Machine Learning
# =====================================================

# Before building a Machine Learning model, the dataset
# must be cleaned and prepared.
# Pandas helps inspect, clean and save datasets.

import pandas as pd

# Example 01 - Create CSV Dataset
with open('students.csv','w') as file:
    file.write('Name,Age,Department,StudyHours,Attendance,Marks\n')
    file.write('Ali,20,CS,4,90,82\n')
    file.write(' Ahmed,21,AI,3,85,74\n')
    file.write('Sara,20,SE,5,95,91\n')
    file.write('Bilal,,DS,2,75,68\n')
    file.write('Usman,22,cs,4,88,\n')
    file.write('Fatima,21,AI,6,96,93\n')
    file.write('Ali,20,CS,4,90,82\n')

students=pd.read_csv('students.csv')
print(students)

# Example 02 - Inspect Dataset
print(students.head())
print(students.info())
print(students.describe())

# Example 03 - Missing Values
print(students.isnull().sum())
students['Age']=students['Age'].fillna(students['Age'].mean())
students['Marks']=students['Marks'].fillna(students['Marks'].mean())

# Example 04 - Remove Duplicates
students=students.drop_duplicates()

# Example 05 - Standardize Text
students['Name']=students['Name'].str.strip().str.title()
students['Department']=students['Department'].str.upper()

# Example 06 - Convert Data Types
students['Age']=students['Age'].astype(int)
students['Marks']=students['Marks'].astype(int)

# Example 07 - Rename Column
students=students.rename(columns={'StudyHours':'Study_Hours'})

# Example 08 - Create New Feature
students['Result']=students['Marks'].apply(lambda x:'Pass' if x>=50 else 'Fail')

# Example 09 - Filter Data
print(students[students['Department']=='CS'])

# Example 10 - Sort Data
students=students.sort_values(by='Marks',ascending=False)

# Example 11 - Reset Index
students=students.reset_index(drop=True)

# Example 12 - Save Clean Dataset
students.to_csv('students_cleaned.csv',index=False)
print(pd.read_csv('students_cleaned.csv'))

# Useful Functions:
# read_csv(), to_csv(), head(), info(), describe(), isnull(), fillna(), drop_duplicates(), astype(), rename(), apply(), lambda, sort_values(), reset_index()

# Summary:
# Read, inspect, clean, transform and save a dataset ready for Machine Learning.
