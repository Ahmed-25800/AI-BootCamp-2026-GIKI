# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 07 - 3D Plots in Matplotlib
# =====================================================

# Sometimes two dimensions (X and Y) are not enough
# to represent data.
#
# Matplotlib allows us to create three-dimensional
# graphs by adding a Z-axis.
#
# 3D plots are widely used in:
# • Data Science
# • Machine Learning
# • Artificial Intelligence
# • Engineering
# • Scientific Computing
# • Mathematics


# if you get error for plotting the graph then uncomment following two line of code.
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np

# Required for 3D plotting
from mpl_toolkits.mplot3d import Axes3D

# =====================================================
# Example 01 - Creating a 3D Figure
# =====================================================

# projection="3d" creates a 3D axis.

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

plt.show()

# =====================================================
# Example 02 - 3D Line Plot
# =====================================================

x = np.arange(1,11)

y = x * 2

z = x * 3

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.plot(

    x,

    y,

    z,

    marker="o"

)

axes.set_title("3D Line Plot")

axes.set_xlabel("X")

axes.set_ylabel("Y")

axes.set_zlabel("Z")

plt.show()

# =====================================================
# Example 03 - 3D Scatter Plot
# =====================================================

x = np.random.randint(1,20,20)

y = np.random.randint(1,20,20)

z = np.random.randint(1,20,20)

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.scatter(

    x,

    y,

    z

)

axes.set_title("3D Scatter Plot")

plt.show()

# =====================================================
# Example 04 - 3D Bar Chart
# =====================================================

x = np.arange(5)

y = np.zeros(5)

z = np.zeros(5)

dx = np.ones(5)

dy = np.ones(5)

dz = [4,7,2,8,5]

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.bar3d(

    x,

    y,

    z,

    dx,

    dy,

    dz

)

axes.set_title("3D Bar Chart")

plt.show()

# =====================================================
# Example 05 - 3D Surface Plot
# =====================================================

x = np.linspace(-5,5,30)

y = np.linspace(-5,5,30)

X,Y = np.meshgrid(x,y)

Z = np.sin(

    np.sqrt(X**2 + Y**2)

)

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.plot_surface(

    X,

    Y,

    Z

)

axes.set_title("3D Surface Plot")

plt.show()

# =====================================================
# Example 06 - 3D Wireframe Plot
# =====================================================

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.plot_wireframe(

    X,

    Y,

    Z

)

axes.set_title("3D Wireframe")

plt.show()

# =====================================================
# Example 07 - 3D Contour Plot
# =====================================================

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.contour3D(

    X,

    Y,

    Z,

    30

)

axes.set_title("3D Contour Plot")

plt.show()

# =====================================================
# Example 08 - 3D Surface with Color Map
# =====================================================

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.plot_surface(

    X,

    Y,

    Z,

    cmap="viridis"

)

axes.set_title("Colored Surface")

plt.show()

# =====================================================
# Example 09 - Changing Viewing Angle
# =====================================================

figure = plt.figure()

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.plot_surface(

    X,

    Y,

    Z,

    cmap="plasma"

)

# Change camera angle

axes.view_init(

    elev=40,

    azim=60

)

axes.set_title("Different View Angle")

plt.show()

# =====================================================
# Example 10 - Practical Example
# =====================================================

# Visualizing student marks
# in three subjects.

students = [

    "Ali",

    "Ahmed",

    "Sara",

    "Bilal"

]

python = [80,75,92,68]

numpy = [82,78,90,70]

pandas = [85,80,94,72]

figure = plt.figure(

    figsize=(8,6)

)

axes = figure.add_subplot(

    111,

    projection="3d"

)

axes.scatter(

    python,

    numpy,

    pandas,

    s=100

)

for i in range(len(students)):

    axes.text(

        python[i],

        numpy[i],

        pandas[i],

        students[i]

    )

axes.set_xlabel("Python")

axes.set_ylabel("NumPy")

axes.set_zlabel("Pandas")

axes.set_title("Student Performance")

plt.show()

# =====================================================
# Useful Functions Used in This Lecture
# =====================================================

# figure()          -> Creates figure
#
# add_subplot()     -> Creates subplot
#
# projection="3d"   -> Enables 3D plotting
#
# plot()            -> 3D Line Plot
#
# scatter()         -> 3D Scatter Plot
#
# bar3d()           -> 3D Bar Chart
#
# plot_surface()    -> Surface Plot
#
# plot_wireframe()  -> Wireframe Plot
#
# contour3D()       -> 3D Contour Plot
#
# meshgrid()        -> Creates coordinate grid
#
# view_init()       -> Changes camera angle
#
# set_xlabel()      -> X-axis label
#
# set_ylabel()      -> Y-axis label
#
# set_zlabel()      -> Z-axis label
#
# set_title()       -> Graph title
#
# show()            -> Displays graph

# =====================================================
# Summary
# =====================================================

# In this lecture we learned:
#
# 1. Creating 3D Axes
# 2. 3D Line Plot
# 3. 3D Scatter Plot
# 4. 3D Bar Chart
# 5. 3D Surface Plot
# 6. 3D Wireframe Plot
# 7. 3D Contour Plot
# 8. Color Maps
# 9. Viewing Angles
# 10. Practical Example
#
# 3D visualizations are useful for
# exploring relationships among three
# variables and are widely used in
# Engineering, AI, Machine Learning,
# Robotics and Scientific Research.

# |-----------------------------------------------------------------------|
# |                 COMMON 3D PLOTS IN MATPLOTLIB                         |
# |-----------------------------------------------------------------------|
# | Function           | Purpose                                          |
# |--------------------|--------------------------------------------------|
# | plot()             | 3D Line Plot                                    |
# | scatter()          | 3D Scatter Plot                                 |
# | bar3d()            | 3D Bar Chart                                    |
# | plot_surface()     | 3D Surface                                      |
# | plot_wireframe()   | 3D Wireframe                                    |
# | contour3D()        | 3D Contour                                      |
# | view_init()        | Changes viewing angle                           |
# | meshgrid()         | Creates coordinate grid                         |
# |-----------------------------------------------------------------------|