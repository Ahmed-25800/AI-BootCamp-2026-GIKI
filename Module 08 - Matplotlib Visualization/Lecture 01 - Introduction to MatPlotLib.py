# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 01 - Introduction to Matplotlib
# =====================================================

# Matplotlib is one of the most popular Python libraries
# used for Data Visualization.
#
# It allows us to represent data graphically
# using different types of charts.
#
# Matplotlib is widely used in:
# 1. Data Analysis
# 2. Machine Learning
# 3. Artificial Intelligence
# 4. Scientific Computing
# 5. Business Analytics
#
# Matplotlib works very well with NumPy
# and Pandas.

# =====================================================
# Installing Matplotlib
# =====================================================

# If Matplotlib is not installed on your computer,
# open Command Prompt or Terminal and type:

# use one of them
# pip install matplotlib
# conda install matplotlib

# =====================================================
# Importing Matplotlib
# =====================================================

# By convention, pyplot is imported using
# the alias plt.

# if you get error for plotting the graph then uncomment following two line of code.
import matplotlib
matplotlib.use("TkAgg")
# TkAgg A backend is the software GUI component responsible for rendering and displaying plots.


import matplotlib.pyplot as plt

print("Matplotlib Imported Successfully.")

# =====================================================
# Example 01 - Creating a Simple Line Plot
# =====================================================

# plot() draws a line graph.

x = [1,2,3,4,5]

y = [10,20,15,25,30]

plt.plot(x,y)

plt.show()

# =====================================================
# Example 02 - Adding a Title
# =====================================================

# title() displays the title of the graph.

plt.plot(x,y)

plt.title("Student Performance")

plt.show()

# =====================================================
# Example 03 - X-axis Label
# =====================================================

# xlabel() displays the label of X-axis.

plt.plot(x,y)

plt.xlabel("Test Number")

plt.show()

# =====================================================
# Example 04 - Y-axis Label
# =====================================================

# ylabel() displays the label of Y-axis.

plt.plot(x,y)

plt.ylabel("Marks")

plt.show()

# =====================================================
# Example 05 - Complete Plot
# =====================================================

# Adding title and both axis labels.

plt.plot(x,y)

plt.title("Student Performance")

plt.xlabel("Test Number")

plt.ylabel("Marks")

plt.show()

# =====================================================
# Example 06 - Changing Line Color
# =====================================================

plt.plot(

    x,

    y,

    color="red"

)

plt.title("Red Line")

plt.show()

# =====================================================
# Example 07 - Changing Line Style
# =====================================================

plt.plot(

    x,

    y,

    linestyle="--"

)

plt.title("Dashed Line")

plt.show()

# =====================================================
# Example 08 - Changing Line Width
# =====================================================

plt.plot(

    x,

    y,

    linewidth=4

)

plt.title("Thick Line")

plt.show()

# =====================================================
# Example 09 - Displaying Grid
# =====================================================

# grid() makes graphs easier to read.

plt.plot(x,y)

plt.grid()

plt.show()

# =====================================================
# Example 10 - Practical Example
# =====================================================

student_marks = [82,74,91,68,88]

tests = [1,2,3,4,5]

plt.plot(

    tests,

    student_marks,

    color="blue",

    linewidth=2

)

plt.title("Student Marks")

plt.xlabel("Test Number")

plt.ylabel("Marks")

plt.grid()

plt.show()

# =====================================================
# Anatomy of a Plot
# =====================================================

# Every Matplotlib graph consists of several parts.

#                Title
# -----------------------------------
# |                                 |
# |             Plot Area           |
# |                                 |
# |                                 |
# |                                 |
# -----------------------------------
#        X-axis Label
#
# Y-axis Label appears on the left.

# Plot Components:
#
# Figure
# Entire window containing the graph.
#
# Axes
# The area where data is plotted.
#
# X-axis
# Horizontal axis.
#
# Y-axis
# Vertical axis.
#
# Title
# Heading of the graph.
#
# Labels
# Describe X-axis and Y-axis.
#
# Grid
# Helps read values easily.

# =====================================================
# Useful Functions Used in This Lecture
# =====================================================

# plot()       -> Draws a line graph.
#
# show()       -> Displays the graph.
#
# title()      -> Adds graph title.
#
# xlabel()     -> Labels X-axis.
#
# ylabel()     -> Labels Y-axis.
#
# grid()       -> Displays grid lines.
#
# color        -> Changes line color.
#
# linestyle    -> Changes line style.
#
# linewidth    -> Changes line thickness.

# =====================================================
# Summary
# =====================================================

# In this lecture we learned:
#
# 1. What is Matplotlib?
# 2. Installing Matplotlib
# 3. Importing pyplot
# 4. Creating a Line Plot
# 5. Adding Titles
# 6. Adding Axis Labels
# 7. Changing Line Color
# 8. Changing Line Style
# 9. Changing Line Width
# 10. Displaying Grid
# 11. Anatomy of a Plot
#
# Matplotlib is the foundation of data
# visualization in Python and is widely used
# in Data Science, Machine Learning and AI.

# |-----------------------------------------------------------------------|
# |              ANATOMY OF A MATPLOTLIB PLOT                             |
# |-----------------------------------------------------------------------|
# | Component            | Purpose                                        |
# |----------------------|------------------------------------------------|
# | Figure               | Complete graph window                          |
# | Axes                 | Area where data is plotted                     |
# | X-axis               | Horizontal axis                                |
# | Y-axis               | Vertical axis                                  |
# | Title                | Graph heading                                  |
# | X-axis Label         | Describes horizontal values                    |
# | Y-axis Label         | Describes vertical values                      |
# | Grid                 | Makes graph easier to read                     |
# | Line                 | Represents relationship between values         |
# |-----------------------------------------------------------------------|