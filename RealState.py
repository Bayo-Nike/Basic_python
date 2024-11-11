import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn import preprocessing
import seaborn as sns

# Import data
df=pd.read_csv('Real-estate1.csv')
print(df.head())

# preprocessing data

df.dropna(inplace=True) # Removing missing values
print(df.head())
print(df.columns)

# Plotting some parts of data understand the data
sns.scatterplot(x='X4 number of convenience stores',
                y='Y house price of unit area',data=df)

# create feature variables
X=df.drop('Y house price of unit area',axis=1)
y=df['Y house price of unit area']
print(X)
print(y)


 # creating train and test sets
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.3, random_state=101)

# creating a regression model
model = LinearRegression()

# fitting the model
model.fit(X_train,y_train)

# making predictions
predictions = model.predict(X_test)

# Model Evaluation
print('mean_squared_error : ', mean_squared_error(y_test, predictions))
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))
