import pandas as pd
import pdb
pdb.set_trace()

# 1. Create

# 1.1 create from a CSV
df = pd.read_csv('telco_churn.csv')

# 1.2 Create from a Dictionary
tempdict = {'co11': [1, 2, 3], 'co12': [4, 5, 6], 'co13': [7, 8, 9]}
dictdf = pd.DataFrame.from_dict(tempdict)


# 2.Read

# 2.1 Shop Top 5 and Bottom 5 Rows

print(df.head(10))


dictdf.head()

df.tail(15)

# 2.2 Show Columns and Data Type
df.columns

df.dtypes

# 2.3 Summary Stats
df.describe()

df.describe(include='object')

# 2.4 filtering Columns

df.State

df['international plan']

df[['State', 'International plan']]

df.Churn.unique()

# 2.5 Filtering on Rows
df.head()

df[df['International plan'] == 'No']

df[(df['International plan'] == 'No') & (df['Churn'] == True)]

# 2.6 Indexing with iloc

df.iloc[14]

df.iloc[14, -1]


df.iloc[22:33]

# 2.7 Indexing with loc
state = df.copy()
state.set_index('State', inplace=True)

state.head()

state.loc['OH']

# 3.Update

# 3.1 Dropping Rows
df.isnull().sum()

df.dropna(inplace=True)

df.isnull().sum()

# 3.2 Dropping Columns

df.drop('Area code', axis=1)

# 3.3 Creating Calculated Columns
df['New Column'] = df['Total night minutes'] + df['Total intl minutes']
df.head()

# 3.4 Updating an Entire Column
df['New Column'] = 100
df.head()

# 3.5 Updating a single value
df.iloc[0, -1] = 10
df.head()

# 3.6 Condition based Updating using Apply
df['Churn Binary'] = df['Churn'].apply(lambda x: 1 if x == True else 0)
df[df['Churn'] == True].head()

# 4. DELETE/OUTPUT

# 4.1 Output to CSV
df.to_csv('output.csv')

# 4.2 Output to JSON
df.to_json()

# 4.4 Delete a DataFrame
del df
