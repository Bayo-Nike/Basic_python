import pandas as pd
import seaborn as sns
# Sample data
data = {'Account Type': ['Savings', 'Savings', 'Checking', 'Checking',
'Credit', 'Credit', 'Loan', 'Loan'],
'Transaction Amount': [2000, 3000, 1500, 1600, 7000, 7200,
50000, 50500]}
df = pd.DataFrame(data)
# Plotting
sns.boxplot(x='Account Type', y='Transaction Amount', data=df)
# plt.title('Transaction Amount by Account Type')
# plt.show()