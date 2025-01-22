import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(df['A'] != 2)
# Remove rows where the value in column 'A' is equal to 2
df = df[df['A'] != 2]

print(df)