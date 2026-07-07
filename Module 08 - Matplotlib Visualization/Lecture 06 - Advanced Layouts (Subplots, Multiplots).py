# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 06 - Advanced Layouts (Subplots)
# =====================================================

# Sometimes we want to display multiple graphs
# inside a single figure.
#
# Matplotlib provides subplot() and subplots()
# for creating multi-panel figures.
#
# This helps us compare multiple datasets
# side by side.
#
# Advanced layouts are widely used in
# Data Analysis, Exploratory Data Analysis (EDA),
# Machine Learning and Research.


# if you get error for plotting the graph then uncomment following two line of code.
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

# Sample Data

tests = [1,2,3,4,5]

marks = [82,74,91,68,88]

attendance = [90,95,85,80,92]

subjects = ["Python","NumPy","Pandas","ML"]

students = [40,35,28,22]

# =====================================================
# Example 01 - Two Subplots (1 Row, 2 Columns)
# =====================================================

# subplot(rows, columns, position)

plt.subplot(1,2,1)

plt.plot(

    tests,

    marks,

    marker="o"

)

plt.title("Marks")

plt.subplot(1,2,2)

plt.plot(

    tests,

    attendance,

    marker="s"

)

plt.title("Attendance")

plt.tight_layout()

plt.show()

# =====================================================
# Example 02 - Three Subplots
# =====================================================

plt.subplot(1,3,1)

plt.plot(

    tests,

    marks

)

plt.title("Line")

plt.subplot(1,3,2)

plt.bar(

    subjects,

    students

)

plt.title("Bar")

plt.subplot(1,3,3)

plt.scatter(

    tests,

    marks

)

plt.title("Scatter")

plt.tight_layout()

plt.show()

# =====================================================
# Example 03 - Four Subplots (2 x 2)
# =====================================================

plt.subplot(2,2,1)

plt.plot(

    tests,

    marks

)

plt.title("Line")

plt.subplot(2,2,2)

plt.bar(

    subjects,

    students

)

plt.title("Bar")

plt.subplot(2,2,3)

plt.scatter(

    tests,

    marks

)

plt.title("Scatter")

plt.subplot(2,2,4)

plt.hist(

    marks

)

plt.title("Histogram")

plt.tight_layout()

plt.show()

# =====================================================
# Example 04 - Using subplots()
# =====================================================

# subplots() creates multiple Axes objects.

figure, axes = plt.subplots(

    1,

    2,

    figsize=(10,4)

)

axes[0].plot(

    tests,

    marks,

    marker="o"

)

axes[0].set_title("Marks")

axes[1].plot(

    tests,

    attendance,

    marker="s"

)

axes[1].set_title("Attendance")

plt.tight_layout()

plt.show()

# =====================================================
# Example 05 - Two Rows Two Columns using subplots()
# =====================================================

figure, axes = plt.subplots(

    2,

    2,

    figsize=(8,6)

)

axes[0,0].plot(

    tests,

    marks

)

axes[0,0].set_title("Line")

axes[0,1].bar(

    subjects,

    students

)

axes[0,1].set_title("Bar")

axes[1,0].scatter(

    tests,

    marks

)

axes[1,0].set_title("Scatter")

axes[1,1].hist(

    marks

)

axes[1,1].set_title("Histogram")

plt.tight_layout()

plt.show()

# =====================================================
# Example 06 - Shared X-axis
# =====================================================

# sharex=True shares the same X-axis.

figure, axes = plt.subplots(

    2,

    1,

    sharex=True,

    figsize=(7,6)

)

axes[0].plot(

    tests,

    marks

)

axes[0].set_title("Marks")

axes[1].plot(

    tests,

    attendance

)

axes[1].set_title("Attendance")

plt.tight_layout()

plt.show()

# =====================================================
# Example 07 - Shared Y-axis
# =====================================================

# sharey=True shares the same Y-axis.

figure, axes = plt.subplots(

    1,

    2,

    sharey=True,

    figsize=(8,4)

)

axes[0].plot(

    tests,

    marks

)

axes[0].set_title("Marks")

axes[1].plot(

    tests,

    attendance

)

axes[1].set_title("Attendance")

plt.tight_layout()

plt.show()

# =====================================================
# Example 08 - Figure Title
# =====================================================

# suptitle() adds one title for
# the complete figure.

figure, axes = plt.subplots(

    1,

    2,

    figsize=(9,4)

)

figure.suptitle(

    "Student Performance"

)

axes[0].plot(

    tests,

    marks

)

axes[0].set_title("Marks")

axes[1].plot(

    tests,

    attendance

)

axes[1].set_title("Attendance")

plt.tight_layout()

plt.show()

# =====================================================
# Example 09 - Practical Example
# =====================================================

# Display four different visualizations
# in one figure.

figure, axes = plt.subplots(

    2,

    2,

    figsize=(10,7)

)

# -----------------------------
# Line Plot
# -----------------------------

axes[0,0].plot(

    tests,

    marks,

    marker="o"

)

axes[0,0].set_title("Marks")

# -----------------------------
# Bar Chart
# -----------------------------

axes[0,1].bar(

    subjects,

    students,

    color="green"

)

axes[0,1].set_title("Students")

# -----------------------------
# Scatter Plot
# -----------------------------

axes[1,0].scatter(

    tests,

    attendance,

    color="red"

)

axes[1,0].set_title("Attendance")

# -----------------------------
# Histogram
# -----------------------------

axes[1,1].hist(

    marks,

    color="orange"

)

axes[1,1].set_title("Marks Distribution")

figure.suptitle(

    "Student Dashboard"

)

plt.tight_layout()

plt.show()

# =====================================================
# Useful Functions Used in This Lecture
# =====================================================

# subplot()      -> Creates one subplot.
#
# subplots()     -> Creates multiple subplots.
#
# figure()       -> Creates a new figure.
#
# figsize        -> Changes figure size.
#
# suptitle()     -> Adds title for entire figure.
#
# sharex         -> Shares X-axis.
#
# sharey         -> Shares Y-axis.
#
# tight_layout() -> Automatically adjusts spacing.
#
# set_title()    -> Adds title to individual subplot.
#
# plot()         -> Draws Line Plot.
#
# bar()          -> Draws Bar Chart.
#
# scatter()      -> Draws Scatter Plot.
#
# hist()         -> Draws Histogram.
#
# show()         -> Displays the figure.

# =====================================================
# Summary
# =====================================================

# In this lecture we learned:
#
# 1. Creating Multiple Subplots
# 2. subplot()
# 3. subplots()
# 4. Shared X-axis
# 5. Shared Y-axis
# 6. Figure Title
# 7. Individual Plot Titles
# 8. Practical Dashboard Example
#
# Advanced layouts help compare multiple
# datasets together and are commonly used
# in Machine Learning dashboards,
# Exploratory Data Analysis (EDA),
# Business Intelligence and Research.

# |-----------------------------------------------------------------------|
# |          DIFFERENCE BETWEEN subplot() AND subplots()                  |
# |-----------------------------------------------------------------------|
# | Function      | Purpose                                               |
# |---------------|-------------------------------------------------------|
# | subplot()     | Creates one subplot at a specific position            |
# | subplots()    | Creates multiple Axes objects together                |
# |-----------------------------------------------------------------------|

# |-----------------------------------------------------------------------|
# |               COMMON LAYOUT FUNCTIONS                                 |
# |-----------------------------------------------------------------------|
# | Function         | Purpose                                            |
# |------------------|----------------------------------------------------|
# | subplot()        | Create a subplot                                  |
# | subplots()       | Create multiple subplots                          |
# | suptitle()       | Figure title                                      |
# | set_title()      | Subplot title                                     |
# | tight_layout()   | Adjust spacing                                    |
# | sharex           | Share X-axis                                      |
# | sharey           | Share Y-axis                                      |
# | figsize          | Change figure size                                |
# |-----------------------------------------------------------------------|

