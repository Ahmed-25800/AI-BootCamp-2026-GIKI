# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 05 - Figure Customization
# =====================================================

# Matplotlib provides many options to customize
# the appearance of graphs.
#
# Customizing graphs makes them more readable,
# attractive and suitable for presentations,
# reports and research papers.
#
# In this lecture we will learn:
# 1. Figure Size
# 2. Colors
# 3. Line Styles
# 4. Legends
# 5. Axis Limits
# 6. Tick Marks
# 7. Annotations
# 8. Saving Figures


# if you get error for plotting the graph then uncomment following two line of code.
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

# Sample Data

tests = [1,2,3,4,5]

ali_marks = [82,74,91,68,88]

ahmed_marks = [76,81,87,72,90]

# =====================================================
# Example 01 - Figure Size
# =====================================================

# figure() creates a new figure.
#
# figsize specifies:
# (Width, Height)

plt.figure(

    figsize=(8,5)

)

plt.plot(

    tests,

    ali_marks

)

plt.title("Figure Size Example")

plt.show()

# =====================================================
# Example 02 - Line Color
# =====================================================

# color changes the line color.

plt.plot(

    tests,

    ali_marks,

    color="red"

)

plt.title("Red Line")

plt.show()

# =====================================================
# Example 03 - Line Style
# =====================================================

# linestyle changes the style of the line.
#
# "-"  Solid
# "--" Dashed
# ":"  Dotted
# "-." Dash-Dot

plt.plot(

    tests,

    ali_marks,

    linestyle="--"

)

plt.title("Dashed Line")

plt.show()

# =====================================================
# Example 04 - Line Width
# =====================================================

# linewidth changes the thickness.

plt.plot(

    tests,

    ali_marks,

    linewidth=4

)

plt.title("Thick Line")

plt.show()

# =====================================================
# Example 05 - Marker Customization
# =====================================================

plt.plot(

    tests,

    ali_marks,

    marker="o",

    markersize=10,

    markerfacecolor="yellow",

    markeredgecolor="black"

)

plt.title("Customized Markers")

plt.show()

# =====================================================
# Example 06 - Legends
# =====================================================

# legend() identifies multiple graphs.

plt.plot(

    tests,

    ali_marks,

    label="Ali"

)

plt.plot(

    tests,

    ahmed_marks,

    label="Ahmed"

)

plt.title("Student Performance")

plt.legend()

plt.show()

# =====================================================
# Example 07 - Axis Limits
# =====================================================

# xlim() changes X-axis range.
#
# ylim() changes Y-axis range.

plt.plot(

    tests,

    ali_marks

)

plt.xlim(1,5)

plt.ylim(60,100)

plt.title("Axis Limits")

plt.show()

# =====================================================
# Example 08 - Tick Marks
# =====================================================

# xticks() changes X-axis values.
#
# yticks() changes Y-axis values.

plt.plot(

    tests,

    ali_marks

)

plt.xticks([1,2,3,4,5])

plt.yticks([60,70,80,90,100])

plt.title("Custom Tick Marks")

plt.show()

# =====================================================
# Example 09 - Grid
# =====================================================

plt.plot(

    tests,

    ali_marks

)

plt.grid()

plt.title("Grid Example")

plt.show()

# =====================================================
# Example 10 - Annotation
# =====================================================

# annotate() writes text on a graph.

plt.plot(

    tests,

    ali_marks,

    marker="o"

)

plt.annotate(

    "Highest Marks",

    xy=(5,88),

    xytext=(4,95),

    arrowprops=dict(

        arrowstyle="->"

    )

)

plt.title("Annotation Example")

plt.show()

# =====================================================
# Example 11 - Saving Figure
# =====================================================

# savefig() saves the graph as an image.
#
# The graph is saved in the current folder.

plt.plot(

    tests,

    ali_marks

)

plt.title("Saving Figure")

plt.savefig("student_marks.png")

plt.show()

# =====================================================
# Example 12 - Complete Customized Graph
# =====================================================

plt.figure(

    figsize=(9,5)

)

plt.plot(

    tests,

    ali_marks,

    color="blue",

    linestyle="-",

    linewidth=2,

    marker="o",

    label="Ali"

)

plt.plot(

    tests,

    ahmed_marks,

    color="red",

    linestyle="--",

    linewidth=2,

    marker="s",

    label="Ahmed"

)

plt.title("Student Marks Comparison")

plt.xlabel("Test Number")

plt.ylabel("Marks")

plt.xlim(1,5)

plt.ylim(60,100)

plt.grid()

plt.legend()

plt.show()

# =====================================================
# Example 13 - Practical Example
# =====================================================

months = [

    "Jan",

    "Feb",

    "Mar",

    "Apr",

    "May",

    "Jun"

]

sales = [

    120,

    135,

    150,

    145,

    170,

    190

]

plt.figure(

    figsize=(10,5)

)

plt.plot(

    months,

    sales,

    color="green",

    marker="o",

    linewidth=3,

    label="Sales"

)

plt.annotate(

    "Highest Sale",

    xy=("Jun",190),

    xytext=("Apr",200),

    arrowprops=dict(

        arrowstyle="->"

    )

)

plt.title("Monthly Sales Report")

plt.xlabel("Months")

plt.ylabel("Sales")

plt.grid()

plt.legend()

plt.savefig("monthly_sales.png")

plt.show()

# =====================================================
# Useful Functions Used in This Lecture
# =====================================================

# figure()       -> Creates a new figure.
#
# figsize        -> Changes figure size.
#
# plot()         -> Draws a line graph.
#
# color          -> Changes line color.
#
# linestyle      -> Changes line style.
#
# linewidth      -> Changes line thickness.
#
# marker         -> Displays markers.
#
# markersize     -> Changes marker size.
#
# markerfacecolor-> Changes marker color.
#
# markeredgecolor-> Changes marker border color.
#
# legend()       -> Displays graph legend.
#
# xlim()         -> Sets X-axis limits.
#
# ylim()         -> Sets Y-axis limits.
#
# xticks()       -> Sets X-axis tick marks.
#
# yticks()       -> Sets Y-axis tick marks.
#
# annotate()     -> Adds text and arrows.
#
# grid()         -> Displays grid lines.
#
# savefig()      -> Saves graph as image.
#
# show()         -> Displays graph.

# =====================================================
# Summary
# =====================================================

# In this lecture we learned:
#
# 1. Changing Figure Size
# 2. Line Colors
# 3. Line Styles
# 4. Line Width
# 5. Marker Customization
# 6. Legends
# 7. Axis Limits
# 8. Tick Marks
# 9. Grid
# 10. Annotations
# 11. Saving Figures
# 12. Complete Customized Graph
#
# These customization techniques help create
# professional-quality visualizations for
# Data Analysis, Machine Learning,
# Artificial Intelligence and Research.

# |-----------------------------------------------------------------------|
# |             COMMON FIGURE CUSTOMIZATION FUNCTIONS                     |
# |-----------------------------------------------------------------------|
# | Function         | Purpose                                            |
# |------------------|----------------------------------------------------|
# | figure()         | Creates a new figure                               |
# | figsize          | Changes figure size                                |
# | color            | Changes line color                                 |
# | linestyle        | Changes line style                                 |
# | linewidth        | Changes line thickness                             |
# | marker           | Displays markers                                   |
# | legend()         | Displays legend                                    |
# | xlim()           | Sets X-axis range                                  |
# | ylim()           | Sets Y-axis range                                  |
# | xticks()         | Sets X-axis tick marks                             |
# | yticks()         | Sets Y-axis tick marks                             |
# | annotate()       | Adds labels and arrows                             |
# | grid()           | Displays grid lines                                |
# | savefig()        | Saves graph as image                               |
# | show()           | Displays graph                                     |
# |-----------------------------------------------------------------------|