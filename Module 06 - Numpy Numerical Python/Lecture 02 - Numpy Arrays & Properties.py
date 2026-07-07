# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 02 - Creating NumPy Arrays & Their Properties
# =====================================================

# NumPy provides several functions to create arrays.
# These functions save time and make coding easier.

import numpy as np

# =====================================================
# Example 01 - array()
# =====================================================

# array() converts a Python list into a NumPy array.

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

# =====================================================
# Example 02 - zeros()
# =====================================================

# Creates an array filled with zeros.

numbers = np.zeros(5)

print(numbers)

# =====================================================
# Example 03 - ones()
# =====================================================

# Creates an array filled with ones.

numbers = np.ones(5)

print(numbers)

# =====================================================
# Example 04 - full()
# =====================================================

# Creates an array filled with the same value.

numbers = np.full(5, 100)

print(numbers)

# =====================================================
# Example 05 - empty()
# =====================================================

# Creates an empty array.
# The values are random because memory is not initialized.

numbers = np.empty(5)

print(numbers)

# =====================================================
# Example 06 - eye()
# =====================================================

# Creates an identity matrix.

matrix = np.eye(4)

print(matrix)

# =====================================================
# Example 07 - identity()
# =====================================================

matrix = np.identity(4)

print(matrix)

# =====================================================
# Example 08 - arange()
# =====================================================

# Similar to Python range().

numbers = np.arange(1, 11)

print(numbers)

numbers = np.arange(0, 21, 5)

print(numbers)

# =====================================================
# Example 09 - linspace()
# =====================================================

# Creates equally spaced values.

print("Line Space")
numbers = np.linspace(0, 10, 5)

print(numbers)

# =====================================================
# Example 10 - logspace()
# =====================================================

# Creates logarithmically spaced values.

numbers = np.logspace(1, 3, 5)

print(numbers)

# =====================================================
# Example 11 - Random Arrays
# =====================================================

# Random decimal numbers between 0 and 1.

numbers = np.random.rand(5)

print(numbers)

# Random integers.

numbers = np.random.randint(1, 101, 10)

print(numbers)

# =====================================================
# Example 12 - Copying Arrays
# =====================================================

marks = np.array([80, 75, 90])

new_marks = marks.copy()

print(marks)

print(new_marks)

new_marks[0] = 100

print(marks)

print(new_marks)

# =====================================================
# Example 13 - Practical Example
# =====================================================

student_marks = np.random.randint(50, 101, 10)

print(student_marks)

# =====================================================
# NumPy Array Properties
# =====================================================

import numpy as np

numbers = np.array([10,20,30,40,50])

# =====================================================
# Example 01 - shape
# =====================================================

# Returns the dimensions of the array.

print(numbers.shape)

# =====================================================
# Example 02 - ndim
# =====================================================

# Returns the number of dimensions.

print(numbers.ndim)

# =====================================================
# Example 03 - size
# =====================================================

# Returns the total number of elements.

print(numbers.size)

# =====================================================
# Example 04 - dtype
# =====================================================

# Returns the data type of the elements.

print(numbers.dtype)

# =====================================================
# Example 05 - itemsize
# =====================================================

# Returns the size (in bytes) of one element.

print(numbers.itemsize)

# =====================================================
# Example 06 - nbytes
# =====================================================

# Returns total memory occupied by the array.

print(numbers.nbytes)

# =====================================================
# Example 07 - Two-Dimensional Array
# =====================================================
import numpy as np
matrix = np.array([
    [10,20,30],
    [40,50,60]
])

print(matrix)

print("Shape:", matrix.shape)

print("Dimensions:", matrix.ndim)

print("Size:", matrix.size)

print("Data Type:", matrix.dtype)

print("Item Size:", matrix.itemsize)

print("Total Bytes:", matrix.nbytes)

# =====================================================
# Example 08 - Practical Example
# =====================================================

student_marks = np.array([82,74,91,68,88])

print(student_marks)

print("Shape:", student_marks.shape)

print("Dimensions:", student_marks.ndim)

print("Total Students:", student_marks.size)

print("Data Type:", student_marks.dtype)

print("Memory Per Element:", student_marks.itemsize)

print("Total Memory:", student_marks.nbytes)

np.random.seed(10)

numbers = np.random.randint(1, 101, 5)

print(numbers)