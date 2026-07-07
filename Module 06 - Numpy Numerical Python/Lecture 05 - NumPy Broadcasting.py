# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 06 - NumPy Broadcasting
# =====================================================

# Broadcasting allows NumPy to perform mathematical
# operations on arrays having different shapes.
#
# Broadcasting removes the need to write loops.
#
# Common Types:
# 1. Scalar Broadcasting
# 2. Row Broadcasting
# 3. Column Broadcasting
# 4. Matrix Broadcasting

# | Broadcasting Type       | Description                                                                              | Example         |
# | ----------------------- | -----------------------------------------------------------------------------------------| --------------- |
# | Scalar Broadcasting   | A single value is applied to every element of an array.                                    | `(4,) + scalar` |
# | Row Broadcasting      | A 1D row vector is repeated across all rows of a 2D array.                                 | `(3,3) + (3,)`  |
# | Column Broadcasting   | A column vector `(n,1)` is repeated across all columns of a 2D array.                      | `(3,3) + (3,1)` |
# | Matrix Broadcasting   | Two arrays with compatible shapes are automatically expanded along dimensions of size `1`. | `(3,1) + (1,3)` |


import numpy as np

# =====================================================
# Example 01 - Scalar Broadcasting (Addition)
# =====================================================

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

result = numbers + 5

print(result)

# =====================================================
# Example 02 - Scalar Broadcasting (Multiplication)
# =====================================================

numbers = np.array([10, 20, 30, 40, 50])

result = numbers * 2

print(result)

# =====================================================
# Example 03 - Scalar Broadcasting (Division)
# =====================================================

numbers = np.array([10, 20, 30, 40, 50])

result = numbers / 10

print(result)

# =====================================================
# Example 04 - Row Broadcasting
# =====================================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

row = np.array([1, 2, 3])

print(matrix)

print(row)

result = matrix + row

print(result)

# =====================================================
# Example 05 - Another Row Broadcasting
# =====================================================

matrix = np.array([
    [5, 10, 15],
    [20, 25, 30]
])

row = np.array([100, 200, 300])

print(matrix + row)

# =====================================================
# Example 06 - Column Broadcasting
# =====================================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

column = np.array([
    [1],
    [2],
    [3]
])

print(matrix)

print(column)

result = matrix + column

print(result)

# =====================================================
# Example 07 - Column Broadcasting using reshape()
# =====================================================

column = np.array([10, 20, 30]).reshape(3, 1)

print(column)

print(matrix + column)

# =====================================================
# Example 08 - Matrix Broadcasting
# =====================================================

matrix1 = np.array([
    [10, 20],
    [30, 40]
])

matrix2 = np.array([
    [1, 2],
    [3, 4]
])

print(matrix1)

print(matrix2)

print(matrix1 + matrix2)

# =====================================================
# Example 09 - Matrix Multiplication by Scalar
# =====================================================

matrix = np.array([
    [2, 4],
    [6, 8]
])

print(matrix * 5)

# =====================================================
# Example 10 - Broadcasting with One Row
# =====================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix)

print(matrix + [10, 20, 30])

# =====================================================
# Example 11 - Broadcasting with One Column
# =====================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix + np.array([[100], [200], [300]]))

# =====================================================
# Example 12 - Broadcasting in Two Arrays
# =====================================================

array1 = np.array([10, 20, 30])

array2 = np.array([2, 4, 6])

print(array1 + array2)

print(array1 * array2)

# =====================================================
# Example 13 - Using Broadcasting to Convert Marks
# =====================================================

marks = np.array([60, 70, 80, 90])

# Add grace marks to every student.

updated_marks = marks + 5

print(updated_marks)

# =====================================================
# Example 14 - Practical Example
# =====================================================

student_marks = np.array([
    [82, 75, 90],
    [65, 88, 79],
    [91, 84, 86]
])

# Bonus marks for each subject.

bonus = np.array([2, 3, 5])

print(student_marks)

print(student_marks + bonus)

# =====================================================
# Example 15 - Practical Example
# =====================================================

sales = np.array([
    [100, 120, 150],
    [200, 180, 220],
    [300, 280, 350]
])

# Tax for each branch.

tax = np.array([
    [10],
    [20],
    [30]
])

print(sales)

print(sales + tax)

# =====================================================
# Example 16 - Broadcasting Rules
# =====================================================

# Rule 1:
# If two arrays have exactly the same shape,
# broadcasting is possible.

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [10, 20],
    [30, 40]
])

print(a + b)

# =====================================================
# Example 17 - Broadcasting Rules
# =====================================================

# Rule 2:
# If one array has only one value,
# it is broadcast to every element.

numbers = np.array([10, 20, 30])

print(numbers + 100)

# =====================================================
# Example 18 - Broadcasting Rules
# =====================================================

# Rule 3:
# If one dimension is 1,
# NumPy stretches that dimension automatically.

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

row = np.array([1, 2, 3])

print(matrix + row)

# =====================================================
# Example 19 - Incompatible Shapes
# =====================================================

# Broadcasting is not possible because
# the shapes are incompatible.

a = np.array([10, 20, 30])

b = np.array([1, 2])

# Uncomment the following statement
# to see the error.

# print(a + b)

# =====================================================
# Example 20 - Practical Example
# =====================================================

student_marks = np.array([
    [80, 75, 90],
    [65, 60, 70],
    [95, 92, 88]
])

# Add 5 marks to every student.

student_marks = student_marks + 5

print(student_marks)

# Multiply every mark by 2.

print(student_marks * 2)

# =====================================================
# Example 21 - Normalizing Student Marks
# =====================================================

marks = np.array([
    [82, 75, 90],
    [65, 88, 79],
    [91, 84, 86]
])

# Maximum marks of each subject.

maximum = np.array([100, 100, 100])

percentage = (marks / maximum) * 100

print(percentage)

# This is a realistic use of broadcasting: a 1×3 array (maximum) is automatically broadcast across all rows of the
# marks matrix. It will give you an early glimpse of how broadcasting is used to normalize datasets before training
# machine learning models. This example naturally bridges to future topics in Pandas, scikit-learn, and deep learning.
