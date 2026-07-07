# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 10 - Applying Functions
# =====================================================

# Sometimes we want to perform the same
# operation on every row or every value.
#
# Pandas provides:
#
# apply()
# map()
# lambda functions
#
# These functions allow us to modify
# data without writing loops.

import pandas as pd

students = pd.DataFrame({

    "Name":["Ali","Ahmed","Sara"],

    "Marks":[82,74,91]

})

print(students)

# =====================================================
# Example 01 - apply()
# =====================================================

# apply() applies a function
# to every value in a column.

students["Marks"] = students["Marks"].apply(

lambda x:x+5

)

print(students)

# =====================================================
# Example 02 - map()
# =====================================================

# map() replaces each value
# according to a function.

students["Result"] = students["Marks"].map(

lambda x:"Pass" if x>=50 else "Fail"

)

print(students)

# =====================================================
# Example 03 - Lambda Function
# =====================================================

# A lambda function is an
# anonymous (unnamed) function.
#
# It is mostly used with
# apply() and map().

square = lambda x:x*x

print(square(5))

# =====================================================
# Example 04 - apply() on Multiple Columns
# =====================================================

students["Percentage"] = students["Marks"].apply(

lambda x:x/100*100

)

print(students)

# =====================================================
# Example 05 - Practical Example
# =====================================================

students["Grade"] = students["Marks"].apply(

lambda x:

"A"

if x>=80

else

"B"

)

print(students)