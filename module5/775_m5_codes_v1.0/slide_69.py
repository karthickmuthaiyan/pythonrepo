import pandas as pd
import sys


# Creating the first Dataframe using dictionary
df1 = df = pd.DataFrame({"a": [1, 2, 3, 4],
                         "b": [5, 6, 7, 8]})

# Append Dict as row to DataFrame
new_row = {"a": 10, "b": 10}
df2 = df1._append([pd.DataFrame([new_row])], ignore_index=False)

print(df2)
print(pd.DataFrame([new_row]))