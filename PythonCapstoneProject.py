# Import necessary libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

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
    return data.groupby('age_group')['Balance'].mean()

print("Calculate average balance per",calculate_age_group_balance(data))

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

print("Dictionary created: ",country_stats)

# Data Structure Manipulation

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
print("To see the Display visualizations wait a Moment")
fig = create_visualizations(data)
plt.show()  # Display the visualizations

# Part 5: Basic Predictive Analysis

# Prepare features for modeling
creditScore_X = data.drop(['CreditScore', 'Surname'], axis=1)  # Drop 'CreditScore' and 'Surname'
creditScore_y = data['CreditScore']

# Check data types for confirmation
print(creditScore_X.dtypes)

# Convert categorical variables to numerical using one-hot encoding
creditScore_X = pd.get_dummies(creditScore_X, drop_first=True)

# Check the processed features
print(creditScore_X.head())  # View the first few rows of the processed features
print(creditScore_y.head())   # View the first few values of the target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    creditScore_X, creditScore_y, test_size=0.3, random_state=101
)

# Create a simple prediction model
model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

# making predictions
predictions = model.predict(X_test)

# Model Evaluation
print('mean_squared_error CreditScore : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error CreditScore : ', mean_absolute_error(y_test, predictions))


# Prepare features and target variable
features = ['CreditScore', 'Age', 'Balance', 'NumOfProducts', 'IsActiveMember']
target = 'CreditScore'  # Assuming I want to predict the credit score

# Note: If 'IsActiveMember' is a boolean, ensure it's numerical (0 or 1)
data['IsActiveMember'] = data['IsActiveMember'].astype(int)

# Create feature DataFrame and target Series
X = data[features]
y = data[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101)

# Create a simple prediction model
model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')