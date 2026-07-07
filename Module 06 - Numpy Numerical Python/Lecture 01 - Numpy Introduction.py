# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 01 - Introduction to NumPy
# =====================================================

# NumPy stands for Numerical Python.
#
# It is one of the most popular Python libraries used for
# Numerical Computing, Data Analysis, Machine Learning,
# Deep Learning and Artificial Intelligence.
#
# NumPy provides a special data structure called ndarray
# which is faster and more memory efficient than Python lists.

# =====================================================
# Installing NumPy
# =====================================================

# If NumPy is not installed on your computer,
# open Command Prompt or Terminal and type:

# use one of them
# pip install numpy
# conda install numpy

# =====================================================
# Importing NumPy
# =====================================================

# By convention, NumPy is imported using the alias np.

import numpy as np

print("NumPy Imported Successfully.")

# =====================================================
# Example 01 - Python List
# =====================================================

# A normal Python list.

numbers = [10, 20, 30, 40, 50]

print(numbers)

print(type(numbers))

# =====================================================
# Example 02 - NumPy ndarray
# =====================================================

# array() converts a Python list into a NumPy ndarray.

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

print(type(numbers))

# =====================================================
# Example 03 - Accessing Elements
# =====================================================

print(numbers[0])

print(numbers[2])

print(numbers[-1])

# =====================================================
# Example 04 - Modifying Elements
# =====================================================

numbers[1] = 100

print(numbers)

# =====================================================
# Example 05 - Shape of ndarray
# =====================================================

# shape tells us the dimensions of the array.

print(numbers.shape)

# =====================================================
# Example 06 - Data Type of ndarray
# =====================================================

print(numbers.dtype)

# =====================================================
# Example 07 - Size of ndarray
# =====================================================

# size tells the total number of elements.

print(numbers.size)

# =====================================================
# Example 08 - Number of Dimensions
# =====================================================

print(numbers.ndim)

# =====================================================
# Example 09 - Creating Another ndarray
# =====================================================

marks = np.array([82, 75, 91, 68])

print(marks)

print(type(marks))

# =====================================================
# Example 10 - Performance Comparison
# =====================================================

# NumPy performs numerical operations much faster
# than Python lists.

import numpy as np
import time

# Python List
numbers = list(range(1000000))

start = time.time()

new_numbers = []

for number in numbers:

    new_numbers.append(number * 2)

end = time.time()

print("Python List Time:", end - start)

# -----------------------------------------------------

# NumPy Array

numbers = np.array(range(1000000))

start = time.time()

new_numbers = numbers * 2

end = time.time()

print("NumPy Array Time:", end - start)

# =====================================================
# Example 11 - Practical Example
# =====================================================

student_marks = np.array([82, 74, 91, 68, 88])

print("Marks:", student_marks)

print("Highest Marks:", student_marks.max())

print("Lowest Marks:", student_marks.min())

print("Average Marks:", student_marks.mean())


# |------------------------------------------------------------------------|
# |            DIFFERENCE BETWEEN PYTHON LIST AND NUMPY ARRAYS             |
# |------------------------------------------------------------------------|
# | Feature                 | Python List         | NumPy ndarray          |
# | ----------------------- | ------------------- | ---------------------- |
# | Stores Data             | Yes                 | Yes                    |
# | Speed                   | Slower              | Faster                 |
# | Memory Usage            | More                | Less                   |
# | Mathematical Operations | Limited             | Very Efficient         |
# | Machine Learning        | Rarely Used         | Widely Used            |
# | Data Type               | Mixed Types Allowed | Usually Same Data Type |
# | Used In                 | General Programming | AI, ML, Data Science   |
# |------------------------------------------------------------------------|
