# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 06 - NumPy Mathematical & Statistical Functions
# =====================================================

# NumPy provides many built-in mathematical and
# statistical functions.
#
# These functions perform calculations on entire arrays
# without using loops.

import numpy as np

numbers = np.array([10,20,30,40,50])

# =====================================================
# Example 01 - sum()
# =====================================================

# Returns the sum of all elements.

print(np.sum(numbers))

# =====================================================
# Example 02 - min()
# =====================================================

# Returns the smallest element.

print(np.min(numbers))

# =====================================================
# Example 03 - max()
# =====================================================

# Returns the largest element.

print(np.max(numbers))

# =====================================================
# Example 04 - mean()
# =====================================================

# Returns the average value.

print(np.mean(numbers))

# =====================================================
# Example 05 - median()
# =====================================================

# Returns the middle value.

print(np.median(numbers))

# =====================================================
# Example 06 - std()
# =====================================================

# Returns the standard deviation.

print(np.std(numbers))

# =====================================================
# Example 07 - var()
# =====================================================

# Returns the variance.

print(np.var(numbers))

# =====================================================
# Example 08 - sqrt()
# =====================================================

# Returns the square root of every element.

print(np.sqrt(numbers))

# =====================================================
# Example 09 - square()
# =====================================================

# Returns the square of every element.

print(np.square(numbers))

# =====================================================
# Example 10 - power()
# =====================================================

# Raises every element to the given power.

print(np.power(numbers,2))

print(np.power(numbers,3))

# =====================================================
# Example 11 - abs()
# =====================================================

numbers = np.array([-10,-20,30,-40,50])

print(np.abs(numbers))

# =====================================================
# Example 12 - round()
# =====================================================

numbers = np.array([2.45,3.67,5.23])

print(np.round(numbers))

# =====================================================
# Example 13 - ceil()
# =====================================================

numbers = np.array([2.1,3.2,4.8])

print(np.ceil(numbers))

# =====================================================
# Example 14 - floor()
# =====================================================

numbers = np.array([2.1,3.9,4.8])

print(np.floor(numbers))

# =====================================================
# Example 15 - exp()
# =====================================================

numbers = np.array([1,2,3])

print(np.exp(numbers))

# =====================================================
# Example 16 - log()
# =====================================================

numbers = np.array([1,10,100])

print(np.log(numbers))

# =====================================================
# Example 17 - sin()
# =====================================================

angles = np.array([0,np.pi/2,np.pi])

print(np.sin(angles))

# =====================================================
# Example 18 - cos()
# =====================================================

print(np.cos(angles))

# =====================================================
# Example 19 - tan()
# =====================================================

print(np.tan(angles))

# =====================================================
# Example 20 - argmax()
# =====================================================

# Returns the index of the largest element.

numbers = np.array([25,80,45,90,65])

print(np.argmax(numbers))

# =====================================================
# Example 21 - argmin()
# =====================================================

# Returns the index of the smallest element.

print(np.argmin(numbers))

# =====================================================
# Example 22 - unique()
# =====================================================

numbers = np.array([10,20,20,30,40,40,50])

print(np.unique(numbers))

# =====================================================
# Example 23 - sort()
# =====================================================

numbers = np.array([50,10,30,20,40])

print(np.sort(numbers))

# =====================================================
# Example 24 - percentile()
# =====================================================

numbers = np.array([10,20,30,40,50])

print(np.percentile(numbers,50))

# =====================================================
# Example 25 - Two-Dimensional Array
# =====================================================

marks = np.array([
    [82,75,90],
    [65,88,79],
    [91,84,86]
])

print(marks)

print("Sum:",np.sum(marks))

print("Mean:",np.mean(marks))

print("Maximum:",np.max(marks))

print("Minimum:",np.min(marks))

# =====================================================
# Example 26 - Row-wise Sum
# =====================================================

print(np.sum(marks,axis=1))

# =====================================================
# Example 27 - Column-wise Sum
# =====================================================

print(np.sum(marks,axis=0))

# =====================================================
# Example 28 - Row-wise Average
# =====================================================

print(np.mean(marks,axis=1))

# =====================================================
# Example 29 - Column-wise Average
# =====================================================

print(np.mean(marks,axis=0))

# =====================================================
# Example 30 - Practical Example
# =====================================================

student_marks = np.array([82,74,91,68,88])

print(student_marks)

print("Highest Marks :",np.max(student_marks))

print("Lowest Marks :",np.min(student_marks))

print("Average Marks :",np.mean(student_marks))

print("Total Marks :",np.sum(student_marks))

print("Standard Deviation :",np.std(student_marks))