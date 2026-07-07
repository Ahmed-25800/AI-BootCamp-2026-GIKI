# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 05 - NumPy Reshaping Arrays
# =====================================================

# Reshaping changes the dimensions of an array
# without changing its data.
#
# NumPy provides several functions to reshape arrays:
# 1. reshape()
# 2. flatten()
# 3. ravel()
# 4. resize()
# 5. transpose()
# 6. T
# 7. squeeze()
# 8. expand_dims()
# 9. newaxis

import numpy as np

# =====================================================
# Example 01 - reshape()
# =====================================================

# Convert a one-dimensional array into
# a two-dimensional array.

numbers = np.arange(1,13)

print(numbers)

matrix = numbers.reshape(3,4)

print(matrix)

# =====================================================
# Example 02 - reshape() into Different Shape
# =====================================================

matrix = numbers.reshape(2,6)

print(matrix)

# =====================================================
# Example 03 - reshape() using -1
# =====================================================

# NumPy automatically calculates the missing dimension.

matrix = numbers.reshape(4,-1)

print(matrix)

# =====================================================
# Example 04 - Three-Dimensional Array
# =====================================================

array3d = numbers.reshape(2,2,3)

print(array3d)

# =====================================================
# Example 05 - flatten()
# =====================================================

# flatten() converts a multidimensional array
# into a one-dimensional array.

matrix = np.array([
    [10,20,30],
    [40,50,60]
])

print(matrix)

numbers = matrix.flatten()

print(numbers)

# =====================================================
# Example 06 - ravel()
# =====================================================

numbers = matrix.ravel()

print(numbers)

# =====================================================
# Example 07 - Difference between flatten() and ravel()
# =====================================================

numbers = matrix.ravel()

numbers[0] = 100

print(matrix)

print(numbers)

# =====================================================
# Example 08 - resize()
# =====================================================

numbers = np.array([10,20,30,40])

print(numbers)

numbers.resize(2,2)

print(numbers)

# =====================================================
# Example 09 - transpose()
# =====================================================

matrix = np.array([
    [10,20,30],
    [40,50,60]
])

print(matrix)

print(matrix.transpose())

# =====================================================
# Example 10 - T
# =====================================================

# T is a shortcut for transpose().

print(matrix.T)

# =====================================================
# Example 11 - squeeze()
# =====================================================

# Removes dimensions of size 1.

array = np.array([[[10,20,30]]])

print(array.shape)

array = np.squeeze(array)

print(array)

print(array.shape)

# =====================================================
# Example 12 - expand_dims()
# =====================================================

numbers = np.array([10,20,30])

print(numbers.shape)

numbers = np.expand_dims(numbers,axis=0)

print(numbers)

print(numbers.shape)

# =====================================================
# Example 13 - expand_dims() using axis=1
# =====================================================

numbers = np.array([10,20,30])

numbers = np.expand_dims(numbers,axis=1)

print(numbers)

print(numbers.shape)

# =====================================================
# Example 14 - newaxis
# =====================================================

numbers = np.array([10,20,30])

print(numbers.shape)

row = numbers[np.newaxis,:]

print(row)

print(row.shape)

# =====================================================
# Example 15 - newaxis (Column Vector)
# =====================================================

column = numbers[:,np.newaxis]

print(column)

print(column.shape)

# =====================================================
# Example 16 - Reshape Student Marks
# =====================================================

student_marks = np.array([80,75,90,65,70,85])

print(student_marks)

student_marks = student_marks.reshape(2,3)

print(student_marks)

# =====================================================
# Example 17 - Reshape Back into One Dimension
# =====================================================

student_marks = student_marks.flatten()

print(student_marks)

# =====================================================
# Example 18 - Practical Example
# =====================================================

marks = np.arange(10,100,10)

print(marks)

marks = marks.reshape(3,3)

print(marks)

print("First Row")

print(marks[0])

print("Second Column")

print(marks[:,1])

print("Transpose")

print(marks.T)

# =====================================================
# Example 19 - Practical Example
# =====================================================

student_names = np.array([
    "Ali",
    "Ahmed",
    "Sara",
    "Ayesha",
    "Bilal",
    "Usman"
])

student_names = student_names.reshape(2,3)

print(student_names)

print(student_names.T)

# =====================================================
# Example 20 - Practical Example
# =====================================================

numbers = np.arange(1,25)

print(numbers)

array3d = numbers.reshape(2,3,4)

print(array3d)

print(array3d.shape)

print(array3d.flatten())

# =====================================================
# Example 21 - Row Vector and Column Vector
# =====================================================

numbers = np.array([10,20,30,40])

print(numbers.shape)

row_vector = numbers.reshape(1,-1)

print(row_vector)

print(row_vector.shape)

column_vector = numbers.reshape(-1,1)

print(column_vector)

print(column_vector.shape)

# | Function        | Purpose                                               |
# | --------------- | ----------------------------------------------------- |
# | `reshape()`     | Changes the shape of an array                         |
# | `flatten()`     | Converts to a 1D array (returns a copy)               |
# | `ravel()`       | Converts to a 1D array (returns a view when possible) |
# | `resize()`      | Changes the shape of the original array               |
# | `transpose()`   | Swaps rows and columns                                |
# | `.T`            | Shortcut for transpose                                |
# | `squeeze()`     | Removes dimensions of size 1                          |
# | `expand_dims()` | Adds a new dimension                                  |
# | `newaxis`       | Adds a new axis using indexing syntax                 |
