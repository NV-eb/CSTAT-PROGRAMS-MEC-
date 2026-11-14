import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv('./company_sales_data.csv')

print(df.head())

plt.plot(df['month_number'], df['total_profit'])

plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Company Profit per Month')
plt.show()

plt.plot(df['month_number'], df['total_profit'],color='green', marker='o', linestyle='--', linewidth=2)

plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Company Profit per Month')
plt.show()

plt.plot(df['month_number'],df['facecream'],label="faceream")
plt.plot(df['month_number'],df['facewash'],label="facewash")
plt.plot(df['month_number'],df['toothpaste'],label="toothpaste")
plt.plot(df['month_number'],df['bathingsoap'],label="bathingsoap")

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Sales data')
plt.legend()
plt.show()

product=['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']

sales=[df[p].sum() for p in product]

plt.pie(sales, labels=product, autopct='%1.1f%%')
plt.title('Sales data')
plt.show()

plt.scatter(df['month_number'], df['total_profit'], color='red')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Company Profit per Month')   
plt.show()

plt.bar(df['month_number'], df['total_profit'], color='orange')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Company Profit per Month')
plt.savefig('./barchart.png')
plt.show()

plt.hist(df['total_profit'], bins=5, color='blue', edgecolor='black')
plt.xlabel('Total Profit')
plt.ylabel('Frequency')
plt.title('Distribution of Total Profit')
plt.show()

plt.figure(figsize=(10,6))

plt.subplot(2, 2, 1)
plt.bar(df['month_number'], df['facecream'], color='blue')
plt.title('Face Cream Sales per Month')

plt.subplot(2, 2, 2)
plt.scatter(df['month_number'], df['facewash'], color='green')
plt.title('Face Wash Sales per Month')

plt.subplot(2, 2, 3)
plt.plot(df['month_number'], df['toothpaste'], color='red', marker='o', linestyle='--')
plt.title('Toothpaste Sales per Month')

plt.subplot(2, 2, 4)
plt.hist(df['bathingsoap'], bins=5, color='purple', edgecolor='black')
plt.title('Bathing Soap Sales Distribution')

plt.tight_layout()
plt.show()

plt.stackplot(df['month_number'], df['facecream'], df['facewash'], df['toothpaste'], df['bathingsoap'], labels=['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap'], colors=['blue', 'green', 'red', 'purple'])

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Sales data')

plt.legend(loc='upper left')
plt.show()

