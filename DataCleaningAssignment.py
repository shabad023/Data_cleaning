Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
... import numpy as np
... import matplotlib.pyplot as plt
... import seaborn as sns
... 
... np.random.seed(42)
... 
... data = {
...     'Player_Age': np.random.randint(18, 40, 100),
...     'Matches_Played': np.random.randint(1, 300, 100),
...     'Batting_Average': np.round(np.random.uniform(20, 60, 100), 2),
...     'Bowling_Average': np.round(np.random.uniform(15, 50, 100), 2),
...     'Strike_Rate': np.round(np.random.uniform(60, 200, 100), 2),
...     'Role': np.random.choice(['Batsman', 'Bowler', 'All-Rounder', 'Wicket-Keeper'], 100)
... }
... 
... df = pd.DataFrame(data)
... 
... df.loc[np.random.choice(df.index, 5, replace=False), 'Batting_Average'] = np.nan
... 
... df = df.append(df.iloc[:3], ignore_index=True)
... 
... df['Batting_Average'].fillna(df['Batting_Average'].median(), inplace=True)
... 
... df.drop_duplicates(inplace=True)
... 
... q1, q3 = df['Batting_Average'].quantile([0.25, 0.75])
... iqr = q3 - q1
... lower_bound = q1 - 1.5 * iqr
... upper_bound = q3 + 1.5 * iqr
... 
... filtered_df = df[(df['Batting_Average'] >= lower_bound) & (df['Batting_Average'] <= upper_bound)]
... 
... df['Role'] = df['Role'].str.strip().str.title()
... 
print("\nBasic Statistics of the Dataset:\n")
print(filtered_df.describe())

plt.figure(figsize=(10, 5))
sns.histplot(filtered_df['Player_Age'], bins=10, kde=True, color='skyblue')
plt.xlabel("Player Age")
plt.ylabel("Frequency")
plt.title("Age Distribution of Players")
plt.show()

plt.figure(figsize=(10, 5))
sns.scatterplot(x=filtered_df['Matches_Played'], y=filtered_df['Batting_Average'], hue=filtered_df['Role'], palette='viridis')
plt.xlabel("Matches Played")
plt.ylabel("Batting Average")
plt.title("Matches Played vs Batting Average")
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(filtered_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix of Cricket Statistics")
plt.show()

report = """
DATA CLEANING PROCESS:
- Filled missing values in Batting Average with the median to maintain data consistency.
- Removed duplicate entries to ensure unique records.
- Identified and filtered out extreme outliers in Batting Average using the IQR method.
- Standardized 'Role' names to keep the formatting uniform.

EXPLORATORY DATA ANALYSIS:
- Player ages vary widely, covering a broad range.
- Matches played don’t have a direct correlation with batting average.
- The correlation heatmap provides insights into how different statistics relate to each other.

CONCLUSION:
This dataset gives a clear picture of cricket player performance. Cleaning and analyzing the data helped uncover key patterns and trends, making it easier to interpret the relationships between different variables.
"""
print(report)
