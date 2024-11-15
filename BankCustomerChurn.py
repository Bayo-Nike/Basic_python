# Import necessary libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset using pandas
data=pd.read_csv('Churn_Modelling.csv')
# Begin Analysis of data
print(data.head())

print(data.info()) # 10000 rows, and 14 columns.3 Object(categorical variables need to Encoding)
# Count duplicated CustomerId values
duplicate_count = data.duplicated('CustomerId').sum()
print(f"Number of duplicated CustomerId values: {duplicate_count}")

# Part 1: Data Loading and Basic Python Operations
def calculate_age_group_balance(data):
    # Create age groups using conditional statements
    data['age_group'] = None
    for idx in data.index:
        age = data.loc[idx, 'Age']
        if age < 30:
            data.loc[idx, 'age_group'] = 'Young'
        elif age < 50:
            data.loc[idx, 'age_group'] = 'Middle-aged'
        else:
            data.loc[idx, 'age_group'] = 'Senior'
    # Calculate average balance per age group
    return data.groupby('age_group')['balance'].mean()

print("Data Loading")
#  Part 2: Data Structure Manipulation
# Example list comprehension
high_value_customers = [
    customer_id for customer_id, balance in zip(data['CustomerId'], data['Balance'])
    if balance > 100000
]
 # Example dictionary creation
country_stats = {
    country: {
        'avg_balance': data[data['Geography'] == country]['Balance'].mean(),
        'churn_rate': data[data['Geography'] == country]['Exited'].mean() * 100
    }
    for country in data['Geography'].unique()
}

# Data Structure Manipulation
print("Data Structure Manipulation")

# set the 'CustomerId' column as the new index
data=data.set_index('CustomerId')
# Display the modified DataFrame
print("\nDataFrame after setting 'CustomerId' as index:")
data.info()

# Encoding

print(data['Geography'].value_counts())
data.replace({'Geography':{'France':2,'Germany':1,'Spain':0}},inplace=True)
print(data['Gender'].value_counts())
data.replace({'Gender':{'Male':0,'Female':1}},inplace=True)
print(data['NumOfProducts'].value_counts())
data.replace({'NumOfProducts':{'1':0,'2':1,'3':1,'4':1}},inplace=True)
print(data['HasCrCard'].value_counts())
print(data['IsActiveMember'].value_counts())
print(data.loc[(data['Balance']==0),'Exited'].value_counts())
# Create a new column 'Zero Balance' based on the condition
data['Zero Balance'] = np.where(data['Balance'] > 0, 1, 0)
# Plot the histogram
data['Zero Balance'].hist()
# Show the plot
plt.title('Histogram of Zero Balance')
plt.xlabel('Zero Balance')
plt.ylabel('Frequency')
plt.show()
# Group By Exited & Geography
print(data.groupby(['Exited','Geography']).count())

# Define Label and Features
print(data.columns)
# Cleansing
X=data.drop(['Surname','Exited'],axis=1)
y=data['Exited']
print(X.shape,y.shape)
# Create a count plot
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
sns.countplot(x='Exited', data=data)

# Add title and labels
plt.title('Count of Churned Customers')
plt.xlabel('Churned (1 = Yes, 0 = No)')
plt.ylabel('Count')
# Show the plot
plt.show()

print(X.shape,y.shape) 
print(y.value_counts())


# Handling Imbalance Data. Oversampling and undersampling
print(data['Exited'].value_counts())



# Part 3: Data Cleaning and Preparation
def prepare_data(data):
    # Handle missing values
    data['Balance'].fillna(data['Balance'].mean(), inplace=True)
    # Create new features
    data['balance_per_product'] = data['Balance'] / data['NumOfProducts']
    data['is_high_value'] = data['Balance'] > data['Balance'].mean()
    # Convert categorical variables
    data = pd.get_dummies(data, columns=['Gender', 'Geography'])
    return data

print("Data Cleaning and Preparation")
print(prepare_data(data))  # Prepare the Data

#  Part 4: Exploratory Data Analysis and Visualization
def create_visualizations(data):
    # Set up the matplotlib figure
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Age distribution
    sns.histplot(data, x='Age', hue='Exited', ax=axes[0, 0], multiple="stack")
    axes[0, 0].set_title('Age Distribution by Churn Status')
    
    # Balance by product number
    sns.boxplot(data, x='NumOfProducts', y='Balance', ax=axes[0, 1])
    axes[0, 1].set_title('Balance Distribution by Product Number')
    
    # Correlation heatmap
    numeric_cols = ['Age', 'Balance', 'CreditScore', 'Tenure']
    sns.heatmap(data[numeric_cols].corr(), annot=True, ax=axes[1, 0], cmap='coolwarm')
    axes[1, 0].set_title('Correlation Heatmap')
    
    # Churn rate by credit score range
    sns.barplot(data, x='CreditScore', y='Exited', ax=axes[1, 1])
    axes[1, 1].set_title('Churn Rate by Credit Score Range')
    
    plt.tight_layout()  # Adjusts subplot params to give specified padding.
    return fig  # Return the figure object for further use
    
# data = pd.read_csv('Churn_Modelling.csv')  # Load your data
fig = create_visualizations(data)
plt.show()  # Display the visualizations

def calculate_age_group_balance(data):
    # Create age groups using conditional statements
    data['age_group'] = None
    for idx in data.index:
        age = data.loc[idx, 'age']
        if age < 30:
            data.loc[idx, 'age_group'] = 'Young'
        elif age < 50:
            data.loc[idx, 'age_group'] = 'Middle-aged'
        else:
            data.loc[idx, 'age_group'] = 'Senior'
    # Calculate average balance per age group
    return data.groupby('age_group')['balance'].mean()
print("Hello")