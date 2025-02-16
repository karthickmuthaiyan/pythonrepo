import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


##################################################
# Solution for Case study 1 problem 1
##################################################
# You are given a dataset, which is present in the LMS, containing the number of 
#hurricanes occurring in the United States along the coast of the Atlantic. Load the 
#data from the dataset into your program and plot a Bar Graph of the data, taking 
#the Year as the x-axis and the number of hurricanes occurring as the Y-axis. 

# Read the three csv files which contains the score of same students in term1 for each Subject
df1 = pd.read_csv("775_m6_datasets_v1.0/Hurricanes.csv")

print(df1.head(5))
x=df1["Year"]
y=df1["Hurricanes"]
# Create a bar plot with the number of hurricanes per year , where x is the year and y is the number of hurricanes
plt.bar(x, y, color='blue')
plt.title("Number of Hurricanes per Year")
plt.xlabel("Year")
plt.ylabel("Number of Hurricanes")
plt.legend()
plt.show()


##################################################
# Solution for Case study 1 problem 2
##################################################
#The dataset given, records data of city temperatures over the years 2014 and 
#2015. Plot the histogram of the temperatures over this period for the cities of 
#San Francisco and Moscow. 

# Read the CityTemps.csv file
df2 = pd.read_csv("775_m6_datasets_v1.0/CityTemps.csv")
print(df2.head(5))  # Display the first 5 rows of the DataFrame

#plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow
# Filter the data for San Francisco and Moscow
sf_temps = df2[['San Francisco']]
print(sf_temps)
moscow_temps = df2.loc[:, 'Moscow']
print(moscow_temps)


# Plot the histogram
plt.hist(sf_temps, bins=20, alpha=0.5, label='San Francisco')
plt.hist(moscow_temps, bins=20, alpha=0.5, label='Moscow')
plt.title("Temperature Distribution for San Francisco and Moscow (2014-2015)")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.legend()
plt.show()

##################################################
# Solution for Case study 1 problem 3
##################################################
#Plot a pie-chart of the number of models released by every manufacturer, 
#recorded in the data provide. Also mention the name of the manufacture with 
#the largest releases. 

# Read the CarManufacturers.csv file
df3 = pd.read_csv("775_m6_datasets_v1.0/Cars2015.csv")
#print(df3.info())  # Display the first 5 rows of the DataFrame

# Count the number of models released by each manufacturer
model_counts = df3['Make'].value_counts()
print(model_counts.index)


# Plot the pie chart
plt.figure(figsize=(10, 8))
plt.pie(model_counts, labels=model_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Number of Models Released by Each Manufacturer in 2015")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Identify the manufacturer with the largest releases
largest_manufacturer = model_counts.idxmax()
print(f"The manufacturer with the largest releases is: {largest_manufacturer}")


##################################################
# Solution for Case study 1 problem 4
##################################################

#read the csv file
df4 = pd.read_csv("case_study_data.csv")

#describe the data on the basis of unit price
print(df4['unit price'].describe())
#print(df4.head())

# Create a new DataFrame with columns 'name', 'net_price', and 'date'
df5 = df4[['name','net_price','Date']]
print(df5.head(5))

# Create a new DataFrame with columns 'name', 'net_price', and 'date'
df5 = df4[['name', 'net_price', 'Date']]

# Group all the records according to 'name'
grouped_df = df5.groupby('name').aggregate({'net_price': 'sum'})
#print(grouped_df)
#grouped_df.info()
#print(grouped_df.index)

#Plot the graph after calculating total sales by each customer. Customer name should be on x axis and total sales in y axis. 
# Create a bar plot with the total sales by each customer

plt.figure(figsize=(10, 8)) 
plt.bar(x=grouped_df.index, height=grouped_df['net_price'] ,color='red')
plt.title("Total Sales by Customer")
plt.xlabel("Customer Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)
plt.legend()
plt.show()

##################################################
# Solution for Case study 1 problem 5
##################################################
#Let the x axis data points and y axis data points are 
X = [1,2,3,4] 
y = [20, 21, 20.5, 20.8]

#5.1: Draw a Simple plot
plt.plot(X, y)
plt.show()

#Configure the line and markers in simple plot
plt.plot(X, y, linestyle='--', marker='o', color='r')
plt.show()


# define width, height as figsize=(4,5) DPI and adjust plot dpi=100
plt.figure(figsize=(8,8), dpi=100)

# configure the axes
plt.xlabel("X-axis", fontsize=14)
plt.ylabel("Y-axis", fontsize=14)

# Give title of Graph & labels of x axis and y axis 
plt.title("Simple Plot")

# Give error bar if  y_error = [0.12, 0.13, 0.2, 0.1] 
y_error = [0.12, 0.13, 0.2, 0.1]
plt.errorbar(X, y, yerr=y_error, fmt='o')
plt.show()

# Draw a scatter graph of any 50 random values of x and y axis 
plt.figure(figsize=(8,8), dpi=100)
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)


#Create a dataframe from following data 
data={'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],  
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],  
'female': [0, 1, 1, 0, 1], 
'age': [42, 52, 36, 24, 73],  
'preTestScore': [4, 24, 31, 2, 3], 
'postTestScore': [25, 94, 57, 62, 70],
'sex': ['0', '1', '1', '0', '1']}
df = pd.DataFrame(data)
print(df)

#Draw a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age 
plt.figure(figsize=(8,8), dpi=100)
plt.scatter(df['preTestScore'], df['postTestScore'], s=df['age']*10)
plt.title("Scatter Plot of preTestScore and postTestScore")
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
plt.show()

# Draw a Scatterplot of preTestScore and postTestScore, with the size of each point set to 300 and color determined by sex
plt.figure(figsize=(8,8), dpi=100)
clrs = df['sex'].map({'0': 'blue', '1': 'red'})
print(clrs)
plt.scatter(df['preTestScore'], df['postTestScore'], s=300, c=clrs)
plt.title("Scatter Plot of preTestScore and postTestScore with Color by Sex")
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
plt.show()


