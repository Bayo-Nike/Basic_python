# Importing Pandas
import pandas as pd

# Sample data
balances = [1000, 2500, 4300, 1200, 5000]
# Creating a Series
balance_series = pd.Series(balances, name="Account Balance")
print(balance_series)