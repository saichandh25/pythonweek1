
import pandas as pd

# Importing the dataset 'train_preprocessed'
train_df = pd.read_csv('./train_preprocessed.csv')
z=train_df[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)
print(z)
x = train_df['Sex']
y= train_df['Survived']

print(x.corr(y))

