# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 03 - NumPy Indexing & Slicing
# =====================================================

# Indexing is used to access one or more elements
# from a NumPy array.
#
# Slicing is used to access multiple elements.
#
# NumPy also provides:
# 1. Fancy Indexing
# 2. Boolean Indexing
#
# These techniques allow us to manipulate datasets
# without writing loops.

import numpy as np

# =====================================================
# Example 01 - One-Dimensional Indexing
# =====================================================

numbers = np.array([10,20,30,40,50])

print(numbers)

print(numbers[0])

print(numbers[2])

print(numbers[4])

# =====================================================
# Example 02 - Negative Indexing
# =====================================================

# Negative indexing starts from the end.

print(numbers[-1])

print(numbers[-2])

print(numbers[-3])

# =====================================================
# Example 03 - Modifying Elements
# =====================================================

numbers[1] = 100

print(numbers)

# =====================================================
# Example 04 - One-Dimensional Slicing
# =====================================================

print(numbers[1:4])

print(numbers[:3])

print(numbers[2:])

print(numbers[:])

# =====================================================
# Example 05 - Step Slicing
# =====================================================

print(numbers[::2])

print(numbers[1::2])

print(numbers[::-1])

# =====================================================
# Example 06 - Two-Dimensional Indexing
# =====================================================

matrix = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(matrix)

print(matrix[0,0])

print(matrix[1,2])

print(matrix[2,1])

# =====================================================
# Example 07 - Two-Dimensional Slicing
# =====================================================

print(matrix[0:2,0:2])

print(matrix[:,1])

print(matrix[1,:])

print(matrix[:,0])

# =====================================================
# Example 08 - Three-Dimensional Indexing
# =====================================================

array3d = np.array([

    [
        [10,20],
        [30,40]
    ],

    [
        [50,60],
        [70,80]
    ]

])

print(array3d)

print(array3d[0,0,0])

print(array3d[1,0,1])

print(array3d[1,1,0])

# =====================================================
# Example 09 - Three-Dimensional Slicing
# =====================================================

print(array3d[0])

print(array3d[1])

print(array3d[:,0,:])

# =====================================================
# Example 10 - Fancy Indexing
# =====================================================

# Fancy indexing allows us to select multiple
# elements using index numbers.

numbers = np.array([10,20,30,40,50,60])
print(numbers)

print(numbers[[0,2,5]])

# =====================================================
# Example 11 - Fancy Indexing in 2D Array
# =====================================================

print(matrix[[0,2]])

print(matrix[:,[0,2]])

# =====================================================
# Example 12 - Boolean Indexing
# =====================================================

marks = np.array([82,45,91,38,76,59])
print(marks)


print(marks > 50)

print(marks[marks > 50])

# =====================================================
# Example 13 - Boolean Indexing
# =====================================================

print(marks < 50)

print(marks[marks < 50])

# =====================================================
# Example 14 - Modifying Values without Loops
# =====================================================

marks[marks < 50] = 50

print(marks)

# =====================================================
# Example 15 - Multiple Conditions
# =====================================================

numbers = np.array([10,20,30,40,50,60,70])

print(numbers[(numbers >= 30) & (numbers <= 60)])

# =====================================================
# Example 16 - Using Logical OR
# =====================================================

print(numbers[(numbers < 20) | (numbers > 60)])

# =====================================================
# Example 17 - where()
# =====================================================

# where() returns the indices where
# the condition becomes True.

print(np.where(numbers > 40))

# =====================================================
# Example 18 - where() with Replacement
# =====================================================

results = np.where(numbers >= 40,"Pass","Fail")

print(results)

# =====================================================
# Example 19 - nonzero()
# =====================================================

numbers = np.array([10,0,20,0,30,40])

print(np.nonzero(numbers))

# =====================================================
# Example 20 - Practical Example
# =====================================================

student_marks = np.array([82,74,91,45,38,88,95])

print(student_marks)

# Display only passed students.

print(student_marks[student_marks >= 50])

# Give grace marks to failed students.

student_marks[student_marks < 50] = student_marks[student_marks < 50] + 10

print(student_marks)

# =====================================================
# Example 21 - Practical Example
# =====================================================

student_names = np.array([
    "Ali",
    "Ahmed",
    "Sara",
    "Ayesha",
    "Bilal"
])

student_marks = np.array([82,45,91,67,38])

print(student_names[student_marks >= 50])

print(student_marks[student_marks >= 50])

# =====================================================
# Example 22 - Selecting Rows and Columns
# =====================================================

matrix = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

# First Row
print(matrix[0,:])

# Last Row
print(matrix[-1,:])

# First Column
print(matrix[:,0])

# Last Column
print(matrix[:,-1])

# Center Element
print(matrix[1,1])

# =====================================================
# Example 23 - Boolean Mask
# =====================================================

marks = np.array([82,45,91,38,76])

mask = marks >= 50

print(mask)

print(marks[mask])