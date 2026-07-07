# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 04 - Scatter Plots, Box Plots & Subplots
# =====================================================

# Matplotlib provides many charts for understanding data.
#
# In this lecture we will learn:
# 1. Scatter Plot
# 2. Box Plot
# 3. Subplots
#
# These charts are widely used during
# Exploratory Data Analysis (EDA)
# before applying Machine Learning algorithms.


# if you get error for plotting the graph then uncomment following two line of code.
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

# =====================================================
# Example 01 - Scatter Plot
# =====================================================

# A Scatter Plot displays individual data points.
#
# It helps us understand the relationship
# between two numerical variables.

study_hours = [1,2,3,4,5,6,7]

marks = [45,55,60,70,78,88,95]

plt.scatter(

    study_hours,

    marks

)

plt.title("Study Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.show()

# =====================================================
# Example 02 - Scatter Plot with Color
# =====================================================

# color changes the color of points.

plt.scatter(

    study_hours,

    marks,

    color="red"

)

plt.title("Scatter Plot with Red Points")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.show()

# =====================================================
# Example 03 - Scatter Plot with Marker
# =====================================================

# marker changes the shape of points.

plt.scatter(

    study_hours,

    marks,

    marker="*",

    color="green"

)

plt.title("Scatter Plot with Star Marker")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.show()

# =====================================================
# Example 04 - Scatter Plot with Point Size
# =====================================================

# s changes the size of scatter points.

plt.scatter(

    study_hours,

    marks,

    s=150,

    color="blue"

)

plt.title("Large Scatter Points")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.show()

# =====================================================
# Example 05 - Box Plot
# =====================================================

# A Box Plot summarizes the distribution
# of numerical data.
#
# It helps identify:
# Minimum Value
# Maximum Value
# Median
# Quartiles
# Outliers

student_marks = [

    82,74,91,68,77,

    83,95,88,79,81,

    73,66,92,85

]

plt.boxplot(

    student_marks

)

plt.title("Student Marks Box Plot")

plt.ylabel("Marks")

plt.show()

# =====================================================
# Example 06 - Box Plot with Grid
# =====================================================

plt.boxplot(

    student_marks

)

plt.title("Box Plot with Grid")

plt.grid()

plt.show()

# =====================================================
# Example 07 - Creating Subplots
# =====================================================

# subplot(rows, columns, position)
#
# This creates multiple graphs inside
# one figure.

plt.subplot(1,2,1)

plt.plot(

    study_hours,

    marks

)

plt.title("Line Plot")

plt.subplot(1,2,2)

plt.scatter(

    study_hours,

    marks

)

plt.title("Scatter Plot")

plt.tight_layout()

plt.show()

# =====================================================
# Example 08 - Three Subplots
# =====================================================

plt.subplot(1,3,1)

plt.plot(

    study_hours,

    marks

)

plt.title("Line")

plt.subplot(1,3,2)

plt.bar(

    ["Ali","Ahmed","Sara"],

    [82,74,91]

)

plt.title("Bar")

plt.subplot(1,3,3)

plt.scatter(

    study_hours,

    marks

)

plt.title("Scatter")

plt.tight_layout()

plt.show()

# =====================================================
# Example 09 - Four Subplots
# =====================================================

plt.subplot(2,2,1)

plt.plot(

    study_hours,

    marks

)

plt.title("Line")

plt.subplot(2,2,2)

plt.scatter(

    study_hours,

    marks

)

plt.title("Scatter")

plt.subplot(2,2,3)

plt.bar(

    ["Ali","Ahmed","Sara"],

    [82,74,91]

)

plt.title("Bar")

plt.subplot(2,2,4)

plt.hist(

    student_marks

)

plt.title("Histogram")

plt.tight_layout()

plt.show()

# =====================================================
# Example 10 - Practical Example
# =====================================================

students = ["Ali","Ahmed","Sara","Bilal"]

marks = [82,74,91,68]

study_hours = [4,3,6,2]

plt.figure(figsize=(10,4))

# -----------------------------
# Scatter Plot
# -----------------------------

plt.subplot(1,2,1)

plt.scatter(

    study_hours,

    marks,

    color="red",

    s=120

)

plt.title("Study Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

# -----------------------------
# Box Plot
# -----------------------------

plt.subplot(1,2,2)

plt.boxplot(

    marks

)

plt.title("Marks Distribution")

plt.ylabel("Marks")

plt.tight_layout()

plt.show()

# =====================================================
# Useful Functions Used in This Lecture
# =====================================================

# scatter()       -> Creates a Scatter Plot.
#
# boxplot()       -> Creates a Box Plot.
#
# subplot()       -> Creates multiple graphs.
#
# figure()        -> Creates a new figure.
#
# tight_layout()  -> Adjusts spacing automatically.
#
# title()         -> Adds graph title.
#
# xlabel()        -> Labels X-axis.
#
# ylabel()        -> Labels Y-axis.
#
# show()          -> Displays the graph.
#
# color           -> Changes point color.
#
# marker          -> Changes point shape.
#
# s               -> Changes point size.
#
# grid()          -> Displays grid lines.

# =====================================================
# Summary
# =====================================================

# In this lecture we learned:
#
# 1. Creating Scatter Plots
# 2. Changing Point Color
# 3. Changing Marker Style
# 4. Changing Point Size
# 5. Creating Box Plots
# 6. Understanding Data Distribution
# 7. Creating Subplots
# 8. Displaying Multiple Charts Together
# 9. Practical Examples
#
# Scatter Plots help identify relationships
# between variables.
#
# Box Plots summarize data and detect outliers.
#
# Subplots allow multiple visualizations
# within a single figure.

# |-----------------------------------------------------------------------|
# |           DIFFERENCE BETWEEN SCATTER, BOX & SUBPLOTS                  |
# |-----------------------------------------------------------------------|
# | Chart Type    | Used For                                              |
# |---------------|-------------------------------------------------------|
# | Scatter Plot  | Relationship between two numerical variables          |
# | Box Plot      | Distribution, Median and Outliers                     |
# | Subplots      | Display multiple graphs in one figure                 |
# |-----------------------------------------------------------------------|

# |-----------------------------------------------------------------------|
# |                 COMMONLY USED FUNCTIONS                               |
# |-----------------------------------------------------------------------|
# | Function        | Purpose                                              |
# |-----------------|------------------------------------------------------|
# | scatter()       | Scatter Plot                                         |
# | boxplot()       | Box Plot                                             |
# | subplot()       | Multiple Graphs                                      |
# | figure()        | Creates Figure                                       |
# | tight_layout()  | Adjusts Layout                                       |
# | show()          | Displays Graph                                       |
# | title()         | Graph Title                                          |
# | xlabel()        | X-axis Label                                         |
# | ylabel()        | Y-axis Label                                         |
# |-----------------------------------------------------------------------|