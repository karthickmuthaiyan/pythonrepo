import pandas as pd

# Create a simple DataFrame
"""
data =pd.read_csv('data.csv')
new_df= data.copy()
x = new_df['Calories'].mode()[0]
new_df["Calories"].fillna(x, inplace = True)
"""

data =pd.read_csv('date.csv')
new_df= data.copy()

new_df["Date"]= pd.to_datetime(new_df["Date"])
new_df.dropna(subset=['Date'], inplace=True)
new_df.dropna(subset=['Calories'], inplace=True)
print(new_df.to_string())  


for x in new_df.index:
    if new_df.loc[x, "Duration"] > 100:
        new_df.loc[x, "Duration"] = 45
print(new_df.to_string())  
print(new_df.duplicated())  

if (round(1.1+2.2,1) == round(3.3,1) ):
    print("True")
else:
    print("False")