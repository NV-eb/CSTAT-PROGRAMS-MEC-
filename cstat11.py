import pandas as pd

data={
    'Name': ['A', 'B', 'C', 'D'],
    'Department': ['IT', 'HR', 'IT', 'HR'],
    'Salary': [50000, 45000, 60000, 55000]
}

df=pd.DataFrame(data)

print(df)

pivot=pd.pivot_table(df, index="Department", values="Salary", aggfunc="mean")

print("Pivot Table:")
print(pivot)

crosstble=pd.crosstab(df['Department'], df['Name'])

print("Crosstab:")
print(crosstble)