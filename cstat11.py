import pandas as pd

# Sample data
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Department': ['IT', 'HR', 'IT', 'HR'],
    'Salary': [50000, 45000, 60000, 55000]
}

df = pd.DataFrame(data)

# Pivot table
pivot = pd.pivot_table(df,
                       values='Salary',
                       index='Department',
                       aggfunc='mean')

print("Pivot Table:")
print(pivot)
