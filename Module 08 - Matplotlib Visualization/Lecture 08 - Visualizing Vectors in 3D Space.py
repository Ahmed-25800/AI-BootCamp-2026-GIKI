# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 08 - Visualizing Vectors in 3D Space
# =====================================================

# A vector is a quantity that has
# both magnitude (length) and direction.
#
# In Machine Learning and Mathematics,
# vectors are used to represent:
#
# • Data points
# • Features
# • Images
# • Documents
# • Word Embeddings
# • Gradients
#
# A 3D vector has three components:
#
# (x, y, z)
#
# Example:
#
# v = (2,3,4)
#
# means
#
# Move
# 2 units along X-axis
# 3 units along Y-axis
# 4 units along Z-axis
#
# Every vector starts from an origin.
#
# Origin = (0,0,0)



# if you get error for plotting the graph then uncomment following two line of code.
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

# =====================================================
# Example 01 - Creating a Single Vector
# =====================================================

# Create a vector.

vector = np.array([2,3,4])

print(vector)

# =====================================================
# Example 02 - Plotting One Vector
# =====================================================

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

# quiver() draws an arrow.
#
# Syntax
#
# quiver(
#       x_start,
#       y_start,
#       z_start,
#
#       x_direction,
#       y_direction,
#       z_direction
# )

axes.quiver(

    0,0,0,

    vector[0],
    vector[1],
    vector[2],

    color="red"

)

axes.set_xlim(0,5)
axes.set_ylim(0,5)
axes.set_zlim(0,5)

axes.set_xlabel("X")
axes.set_ylabel("Y")
axes.set_zlabel("Z")

axes.set_title("Single Vector")

plt.show()

# =====================================================
# Example 03 - Two Vectors
# =====================================================

vector1 = np.array([2,3,4])

vector2 = np.array([4,2,1])

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.quiver(

    0,0,0,

    vector1[0],
    vector1[1],
    vector1[2],

    color="blue"

)

axes.quiver(

    0,0,0,

    vector2[0],
    vector2[1],
    vector2[2],

    color="green"

)

axes.set_xlim(0,5)
axes.set_ylim(0,5)
axes.set_zlim(0,5)

axes.set_title("Two Vectors")

plt.show()

# =====================================================
# Example 04 - Multiple Vectors
# =====================================================

vectors = np.array([

    [2,1,3],

    [4,3,2],

    [3,5,1],

    [1,2,4]

])

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

for vector in vectors:

    axes.quiver(

        0,0,0,

        vector[0],
        vector[1],
        vector[2]

    )

axes.set_xlim(0,6)
axes.set_ylim(0,6)
axes.set_zlim(0,6)

axes.set_title("Multiple Vectors")

plt.show()

# =====================================================
# Example 05 - Vector Addition
# =====================================================

# Vector A

A = np.array([2,1,3])

# Vector B

B = np.array([1,3,2])

# Resultant Vector

C = A + B

print(C)

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.quiver(

    0,0,0,

    A[0],
    A[1],
    A[2],

    color="red"

)

axes.quiver(

    0,0,0,

    B[0],
    B[1],
    B[2],

    color="green"

)

axes.quiver(

    0,0,0,

    C[0],
    C[1],
    C[2],

    color="blue"

)

axes.set_xlim(0,6)
axes.set_ylim(0,6)
axes.set_zlim(0,6)

axes.set_title("Vector Addition")

plt.show()

# =====================================================
# Example 06 - Mapping Data Points
# =====================================================

# Every row represents one point
# inside a three-dimensional feature space.

student_features = np.array([

    [82,75,91],

    [68,80,74],

    [91,90,89],

    [75,60,70]

])

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.scatter(

    student_features[:,0],

    student_features[:,1],

    student_features[:,2],

    s=80

)

axes.set_xlabel("Python")

axes.set_ylabel("NumPy")

axes.set_zlabel("Pandas")

axes.set_title("Students in Feature Space")

plt.show()

# =====================================================
# Example 07 - Feature Space
# =====================================================

# In Machine Learning,
# each column represents one feature.
#
# Every row becomes one point
# inside the feature space.

students = np.array([

    [170,65,22],

    [180,80,24],

    [165,55,20],

    [175,72,23]

])

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.scatter(

    students[:,0],

    students[:,1],

    students[:,2],

    s=80

)

axes.set_xlabel("Height")

axes.set_ylabel("Weight")

axes.set_zlabel("Age")

axes.set_title("Feature Space")

plt.show()

# =====================================================
# Practical Example
# =====================================================

# Imagine every student is represented
# by three exam marks.
#
# Therefore every student becomes
# one point in a 3D vector space.

students = np.array([

    [82,80,91],

    [74,78,70],

    [91,90,95],

    [68,72,75],

    [88,86,90]

])

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.scatter(

    students[:,0],

    students[:,1],

    students[:,2],

    s=100

)

axes.set_xlabel("Python")

axes.set_ylabel("NumPy")

axes.set_zlabel("Pandas")

axes.set_title("Student Feature Space")

plt.show()

# =====================================================
# Useful Functions Used in This Lecture
# =====================================================

# np.array()      -> Creates vectors
#
# quiver()        -> Draws vectors
#
# scatter()       -> Draws feature points
#
# figure()        -> Creates figure
#
# add_subplot()   -> Creates 3D axes
#
# projection="3d" -> Enables 3D plotting
#
# set_xlabel()    -> X-axis label
#
# set_ylabel()    -> Y-axis label
#
# set_zlabel()    -> Z-axis label
#
# set_xlim()      -> X-axis limits
#
# set_ylim()      -> Y-axis limits
#
# set_zlim()      -> Z-axis limits
#
# show()          -> Displays graph

# =====================================================
# Summary
# =====================================================

# In this lecture we learned:
#
# 1. What is a Vector
# 2. 3D Coordinates
# 3. Plotting One Vector
# 4. Plotting Multiple Vectors
# 5. Vector Addition
# 6. Feature Space
# 7. Mapping Data in 3D
#
# Understanding vectors is one of the
# most important concepts in Machine
# Learning, Deep Learning, Computer Vision,
# Robotics and Natural Language Processing.

# |-----------------------------------------------------------------------|
# |                 VECTOR VS DATA POINT                                  |
# |-----------------------------------------------------------------------|
# | Vector                         | Data Point                           |
# |--------------------------------|--------------------------------------|
# | Has magnitude and direction    | Represents one observation           |
# | Usually drawn as an arrow      | Usually shown as a dot               |
# | Starts from an origin          | Located at coordinates               |
# | Used in Linear Algebra         | Used in Machine Learning datasets    |
# |-----------------------------------------------------------------------|

# |-----------------------------------------------------------------------|
# |                 REAL-WORLD EXAMPLES OF 3D FEATURES                    |
# |-----------------------------------------------------------------------|
# | X-axis        | Y-axis         | Z-axis                              |
# |---------------|----------------|-------------------------------------|
# | Height        | Weight         | Age                                 |
# | Python Marks  | NumPy Marks    | Pandas Marks                        |
# | Income        | Experience     | Education                           |
# | RGB Red       | RGB Green      | RGB Blue                            |
# |-----------------------------------------------------------------------|