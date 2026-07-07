# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 02 - Line Plots & Markers
# =====================================================

# A Line Plot is one of the most commonly used charts
# in Data Visualization.
#
# It is used to show how values change over time
# or how one variable changes with another variable.
#
# A Marker is a symbol displayed on each data point.
# It makes individual values easier to identify.


# if you get error for plotting the graph then uncomment following two line of code.
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

# =====================================================
# Example 01 - Simple Line Plot
# =====================================================

# plot() creates a simple line graph.

x = [1,2,3,4,5]

y = [10,20,15,25,30]

plt.plot(x, y)

plt.title("Simple Line Plot")

plt.show()

# =====================================================
# Example 02 - Line Plot with Markers
# =====================================================

# marker displays a symbol on each data point.

plt.plot(

    x,

    y,

    marker="o"

)

plt.title("Line Plot with Circle Markers")

plt.show()

# =====================================================
# Example 03 - Different Marker Styles
# =====================================================

# Some common markers:
# o -> Circle
# s -> Square
# ^ -> Triangle
# * -> Star
# x -> Cross
# D -> Diamond

plt.plot(

    x,

    y,

    marker="*"

)

plt.title("Star Marker")

plt.show()

# =====================================================
# Example 04 - Marker Size
# =====================================================

# markersize changes the size of markers.

plt.plot(

    x,

    y,

    marker="o",

    markersize=12

)

plt.title("Large Markers")

plt.show()

# =====================================================
# Example 05 - Marker Face Color
# =====================================================

# markerfacecolor changes the color inside markers.

plt.plot(

    x,

    y,

    marker="o",

    markerfacecolor="red"

)

plt.title("Marker Face Color")

plt.show()

# =====================================================
# Example 06 - Marker Edge Color
# =====================================================

# markeredgecolor changes the border color.

plt.plot(

    x,

    y,

    marker="o",

    markeredgecolor="blue"

)

plt.title("Marker Edge Color")

plt.show()

# =====================================================
# Example 07 - Marker Edge Width
# =====================================================

# markeredgewidth changes border thickness.

plt.plot(

    x,

    y,

    marker="o",

    markeredgewidth=3

)

plt.title("Marker Edge Width")

plt.show()

# =====================================================
# Example 08 - Line Color
# =====================================================

# color changes the color of the line.

plt.plot(

    x,

    y,

    color="green"

)

plt.title("Green Line")

plt.show()

# =====================================================
# Example 09 - Line Style
# =====================================================

# linestyle changes the style of the line.

# "-"  Solid
# "--" Dashed
# "-." Dash Dot
# ":"  Dotted

plt.plot(

    x,

    y,

    linestyle="--"

)

plt.title("Dashed Line")

plt.show()

# =====================================================
# Example 10 - Line Width
# =====================================================

# linewidth changes the thickness.

plt.plot(

    x,

    y,

    linewidth=4

)

plt.title("Thick Line")

plt.show()

# =====================================================
# Example 11 - Color, Marker and Line Together
# =====================================================

plt.plot(

    x,

    y,

    color="red",

    marker="o",

    linestyle="--",

    linewidth=2

)

plt.title("Customized Line Plot")

plt.xlabel("X Values")

plt.ylabel("Y Values")

plt.grid()

plt.show()

# =====================================================
# Example 12 - Multiple Lines
# =====================================================

# Multiple plot() calls draw multiple lines
# on the same graph.

marks1 = [82,74,91,68,88]

marks2 = [76,80,89,71,90]

tests = [1,2,3,4,5]

plt.plot(

    tests,

    marks1,

    marker="o"

)

plt.plot(

    tests,

    marks2,

    marker="s"

)

plt.title("Comparison of Two Students")

plt.xlabel("Test Number")

plt.ylabel("Marks")

plt.grid()

plt.show()

# =====================================================
# Example 13 - Adding Legends
# =====================================================

# legend() identifies each plotted line.

plt.plot(

    tests,

    marks1,

    marker="o",

    label="Ali"

)

plt.plot(

    tests,

    marks2,

    marker="s",

    label="Ahmed"

)

plt.title("Student Performance")

plt.xlabel("Test Number")

plt.ylabel("Marks")

plt.legend()

plt.grid()

plt.show()

# =====================================================
# Example 14 - Practical Example
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

plt.plot(

    months,

    sales,

    marker="o",

    color="blue",

    linewidth=2

)

plt.title("Monthly Sales")

plt.xlabel("Months")

plt.ylabel("Sales")

plt.grid()

plt.show()

# =====================================================
# Useful Functions Used in This Lecture
# =====================================================

# plot()             -> Draws a line graph.
#
# show()             -> Displays the graph.
#
# title()            -> Adds graph title.
#
# xlabel()           -> Labels X-axis.
#
# ylabel()           -> Labels Y-axis.
#
# grid()             -> Displays grid lines.
#
# legend()           -> Displays line labels.
#
# marker             -> Displays symbols.
#
# markersize         -> Changes marker size.
#
# markerfacecolor    -> Changes marker color.
#
# markeredgecolor    -> Changes marker border color.
#
# markeredgewidth    -> Changes border thickness.
#
# color              -> Changes line color.
#
# linestyle          -> Changes line style.
#
# linewidth          -> Changes line thickness.

# =====================================================
# Summary
# =====================================================

# In this lecture we learned:
#
# 1. Creating a Line Plot
# 2. Using Different Markers
# 3. Marker Size
# 4. Marker Colors
# 5. Marker Border
# 6. Line Color
# 7. Line Style
# 8. Line Width
# 9. Multiple Lines
# 10. Legends
# 11. Practical Example
#
# Line plots are widely used in
# Data Analysis, Machine Learning,
# Artificial Intelligence and Business Analytics.

# |-----------------------------------------------------------------------|
# |                  COMMON MARKERS IN MATPLOTLIB                         |
# |-----------------------------------------------------------------------|
# | Marker | Meaning                                                      |
# |--------|--------------------------------------------------------------|
# |  "o"   | Circle                                                       |
# |  "s"   | Square                                                       |
# |  "^"   | Triangle                                                     |
# |  "*"   | Star                                                         |
# |  "x"   | Cross                                                        |
# |  "D"   | Diamond                                                      |
# |-----------------------------------------------------------------------|

# |-----------------------------------------------------------------------|
# |                 COMMON LINE STYLES IN MATPLOTLIB                      |
# |-----------------------------------------------------------------------|
# | Style | Meaning                                                       |
# |-------|---------------------------------------------------------------|
# | "-"   | Solid Line                                                    |
# | "--"  | Dashed Line                                                   |
# | "-."  | Dash-Dot Line                                                 |
# | ":"   | Dotted Line                                                   |
# |-----------------------------------------------------------------------|