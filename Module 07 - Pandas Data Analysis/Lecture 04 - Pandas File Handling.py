# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)

# =====================================================
# Lecture 04 - Pandas Data I_O (CSV, Excel & JSON)
# =====================================================

import pandas as pd

students = pd.DataFrame({
    "Name":["Ali","Ahmed","Sara"],
    "Marks":[82,74,91],
    "Department":["CS","AI","SE"]
})

print(students)

# Example 01 - to_csv()
students.to_csv("students.csv",index=False)
print(pd.read_csv("students.csv"))

# Example 02 - usecols
print(pd.read_csv("students.csv",usecols=["Name","Marks"]))

# Example 03 - nrows
print(pd.read_csv("students.csv",nrows=2))

# Example 04 - to_excel()
students.to_excel("students.xlsx",index=False)

# Example 05 - read_excel()
print(pd.read_excel("students.xlsx"))

# Example 06 - to_json()
students.to_json("students.json",orient="records",indent=4)

# Example 07 - read_json()
print(pd.read_json("students.json"))

# Example 08 - Statistics
df=pd.read_csv("students.csv")
print(df["Marks"].mean())
print(df["Marks"].max())
print(df["Marks"].min())

# Example 09 - Filtering
print(df[df["Marks"]>=80])

# Example 10 - Summary
# read_csv()   -> Reads CSV
# to_csv()     -> Writes CSV
# read_excel() -> Reads Excel
# to_excel()   -> Writes Excel
# read_json()  -> Reads JSON
# to_json()    -> Writes JSON
