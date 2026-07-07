# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 03 - Bar Charts, Histograms & Pie Charts
# =====================================================

# Matplotlib provides many types of charts for
# visualizing data.
#
# In this lecture we will learn:
# 1. Bar Charts
# 2. Histograms
# 3. Pie Charts
#
# These charts are commonly used in Data Analysis,
# Machine Learning and Artificial Intelligence.


# if you get error for plotting the graph then uncomment following two line of code.
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

# =====================================================
# Example 01 - Simple Bar Chart
# =====================================================

# A Bar Chart compares values of different categories.

students = ["Ali", "Ahmed", "Sara", "Bilal"]

marks = [82, 74, 91, 68]

plt.bar(

    students,

    marks

)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()

# =====================================================
# Example 02 - Bar Chart with Color
# =====================================================

# color changes the color of bars.

plt.bar(

    students,

    marks,

    color="green"

)

plt.title("Green Bar Chart")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()

# =====================================================
# Example 03 - Bar Chart with Width
# =====================================================

# width changes the thickness of bars.

plt.bar(

    students,

    marks,

    width=0.4

)

plt.title("Bar Width Example")

plt.show()

# =====================================================
# Example 04 - Horizontal Bar Chart
# =====================================================

# barh() creates horizontal bars.

plt.barh(

    students,

    marks,

    color="orange"

)

plt.title("Horizontal Bar Chart")

plt.xlabel("Marks")

plt.ylabel("Students")

plt.show()

# =====================================================
# Example 05 - Histogram
# =====================================================

# A Histogram shows the distribution
# (frequency) of numerical data.

student_marks = [

    82,74,91,68,77,83,95,

    88,79,81,73,66,92,85

]

plt.hist(

    student_marks

)

plt.title("Histogram of Student Marks")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.show()

# =====================================================
# Example 06 - Histogram with Bins
# =====================================================

# bins divides the data into intervals.

plt.hist(

    student_marks,

    bins=5

)

plt.title("Histogram with 5 Bins")

plt.show()

# =====================================================
# Example 07 - Histogram with Color
# =====================================================

plt.hist(

    student_marks,

    bins=5,

    color="purple"

)

plt.title("Colored Histogram")

plt.show()

# =====================================================
# Example 08 - Pie Chart
# =====================================================

# A Pie Chart shows the percentage
# contribution of each category.

departments = [

    "CS",

    "AI",

    "SE",

    "DS"

]

students_count = [

    40,

    25,

    20,

    15

]

plt.pie(

    students_count,

    labels=departments

)

plt.title("Students by Department")

plt.show()

# =====================================================
# Example 09 - Pie Chart with Percentages
# =====================================================

# autopct displays percentages.

plt.pie(

    students_count,

    labels=departments,

    autopct="%1.1f%%"

)

plt.title("Department Percentage")

plt.show()

# =====================================================
# Example 10 - Exploding a Pie Slice
# =====================================================

# explode separates a slice from others.

explode = [

    0,

    0.2,

    0,

    0

]

plt.pie(

    students_count,

    labels=departments,

    explode=explode,

    autopct="%1.1f%%"

)

plt.title("Exploded Pie Chart")

plt.show()

# =====================================================
# Example 11 - Shadow Effect
# =====================================================

# shadow=True adds a shadow.

plt.pie(

    students_count,

    labels=departments,

    autopct="%1.1f%%",

    shadow=True

)

plt.title("Pie Chart with Shadow")

plt.show()

# =====================================================
# Example 12 - Practical Example
# =====================================================

subjects = [

    "Python",

    "NumPy",

    "Pandas",

    "Matplotlib"

]

students = [

    45,

    38,

    30,

    22

]

# -----------------------------
# Bar Chart
# -----------------------------

plt.bar(

    subjects,

    students,

    color="skyblue"

)

plt.title("Students Learning Different Topics")

plt.xlabel("Topics")

plt.ylabel("Number of Students")

plt.show()

# -----------------------------
# Histogram
# -----------------------------

marks = [

    55,60,65,70,72,

    75,78,80,82,84,

    86,88,90,92,95

]

plt.hist(

    marks,

    bins=5,

    color="green"

)

plt.title("Distribution of Marks")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.show()

# -----------------------------
# Pie Chart
# -----------------------------

plt.pie(

    students,

    labels=subjects,

    autopct="%1.1f%%"

)

plt.title("Topic Distribution")

plt.show()

# =====================================================
# Useful Functions Used in This Lecture
# =====================================================

# bar()        -> Creates a vertical bar chart.
#
# barh()       -> Creates a horizontal bar chart.
#
# hist()       -> Creates a histogram.
#
# pie()        -> Creates a pie chart.
#
# title()      -> Adds chart title.
#
# xlabel()     -> Labels X-axis.
#
# ylabel()     -> Labels Y-axis.
#
# show()       -> Displays the chart.
#
# color        -> Changes chart color.
#
# width        -> Changes bar width.
#
# bins         -> Divides histogram into intervals.
#
# labels       -> Displays category names.
#
# autopct      -> Displays percentages on pie chart.
#
# explode      -> Separates pie slices.
#
# shadow       -> Adds shadow to pie chart.

# =====================================================
# Summary
# =====================================================

# In this lecture we learned:
#
# 1. Creating Bar Charts
# 2. Horizontal Bar Charts
# 3. Histograms
# 4. Histogram Bins
# 5. Pie Charts
# 6. Pie Chart Percentages
# 7. Exploding Pie Slices
# 8. Shadow Effect
# 9. Practical Examples
#
# These charts are widely used for
# comparing categories, understanding
# data distribution and showing percentages.

# |-----------------------------------------------------------------------|
# |               DIFFERENCE BETWEEN BAR, HISTOGRAM & PIE                 |
# |-----------------------------------------------------------------------|
# | Chart Type | Used For                                                 |
# |------------|----------------------------------------------------------|
# | Bar Chart  | Compare values of different categories                   |
# | Histogram  | Show frequency distribution of numerical data            |
# | Pie Chart  | Show percentage contribution of each category            |
# |-----------------------------------------------------------------------|

# |-----------------------------------------------------------------------|
# |                 COMMONLY USED FUNCTIONS                               |
# |-----------------------------------------------------------------------|
# | Function     | Purpose                                                |
# |--------------|--------------------------------------------------------|
# | bar()        | Vertical Bar Chart                                     |
# | barh()       | Horizontal Bar Chart                                   |
# | hist()       | Histogram                                               |
# | pie()        | Pie Chart                                               |
# | show()       | Display Graph                                           |
# | title()      | Graph Title                                             |
# | xlabel()     | X-axis Label                                            |
# | ylabel()     | Y-axis Label                                            |
# |-----------------------------------------------------------------------|