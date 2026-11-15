import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('./BankChurners.csv')

print(df.head())

df['Attrition_Flag'].value_counts().plot(kind='bar',color='blue',edgecolor='black')

plt.xlabel('Attrition Flag')
plt.ylabel('Count')
plt.title('Attrition Flag Distribution')
plt.show()

columns = ['Gender', 'Education_Level',
           'Marital_Status', 'Income_Category',
           'Card_Category']

for col in columns:
    df[col].value_counts().plot(kind='bar',color='blue',edgecolor='black')

    plt.xlabel(col)
    plt.ylabel('Count')
    plt.title(col + ' Distribution')

    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

sns.boxplot(data=df, x='Total_Relationship_Count', y='Customer_Age')
plt.title('Customer Age Distribution by Attrition Flag')
plt.show()

sns.boxplot(data=df[['Total_Amt_Chng_Q4_Q1',
                     'Months_on_book',
                     'Total_Trans_Ct']])

plt.xticks(rotation=45)
plt.title('Box Plot of Customer Data')
plt.show()


num=df[['Total_Relationship_Count', 'Months_Inactive_12_mon','Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal', 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct', 'Avg_Utilization_Ratio']]

corr=num.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title('Correlation Heatmap')
plt.show()