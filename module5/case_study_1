import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#=====================================
# Solution for Case study 1 problem 1
#=====================================
# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("775_m5_datasets_v1.0'\'SalaryGender.csv") 
#print(df.to_string(index=False))

# Display the first 5 rows of the DataFrame 
print(df.head(2))

Salary_array = df["Salary"]
Gender_array =df["Gender"]
Age_array=df["Age"]
Phd_array=df["PhD"]

#=====================================
# Solution for Case study 1 problem 2
#=====================================
# Find the number of men with a PhD
num_men_with_phd = df[(df["Gender"] == 1) & (df["PhD"] == 1)].shape[0]
print(f"Number of men with PhD: {num_men_with_phd}")

# Find the number of women with a PhD
num_women_with_phd=df[(df["Gender"] == 0) & (df["PhD"] == 1)].shape[0]
print(f"number of women with PhD: {num_women_with_phd}")

#=====================================
# Solution for Case study 1 problem 3
#=====================================
# Store the “Age” and “PhD” columns in one DataFrame
age_phd_df = df[["Age","PhD"]]
print("DataFrame with Age and PhD columns:")
print(age_phd_df.head(2))


# Delete the data of all people who don’t have a PhD
df_with_phd = df[df["PhD"] == 1]
print("DataFrame with only people who have a PhD:")
print(df_with_phd.head(2))

#To write the DataFrame to a CSV file
df_with_phd.to_csv("775_m5_datasets_v1.0'\'people_with_phd.csv", index=False)

#=====================================
# Solution for Case study 1 problem 4
#=====================================
#Calculate the total number of people who have a PhD degree from SalaryGender CSV file. 
total_phd = df[df["PhD"] == 1].shape[0]
print(f"Total number of people with a PhD: {total_phd}")


#=====================================
# Solution for Case study 1 problem 5
#=====================================
#How do you Count The Number Of Times Each Value Appears In An Array Of Integers? 
# Example array of integers
array_of_integers = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Count the number of times each value appears in the array
import numpy as np

arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
# Using np.bincount
counts = np.bincount(arr)
print(counts)

unique_values,count = np.unique(arr, return_counts=True)
print("Unique values:",unique_values)
print("Count of unique values:",count)


#=====================================
# Solution for Case study 1 problem 6
#=====================================
#Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements greater than 5.
# Create a numpy array
array = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

# Filter the elements greater than 5
filtered_elements = array[array > 5]
print("Elements greater than 5:", filtered_elements)


#=====================================
# Solution for Case study 1 problem 7
#=====================================
#Create a numpy array having NaN (Not a Number) and print it. 
#array([ nan,   1.,   2.,  nan,   3.,   4.,   5.]) 
#Print the same array omitting all elements which are nan

# Create a numpy array with NaN values
nan_array = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print("Array with NaN values:", nan_array)

# Print the array omitting all elements which are NaN 
nan_array_without_nan = nan_array[~np.isnan(nan_array)]
print("Array without NaN values:", nan_array_without_nan)


#=====================================
# Solution for Case study 1 problem 8
#=====================================
# Create a 10x10 array with random values
random_array = np.random.rand((10, 10))

# Find the minimum and maximum values in the array
min_value = np.min(random_array)
max_value = np.max(random_array)

print("10x10 array with random values:")
print(random_array)
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")


#=====================================
# Solution for Case study 1 problem 9
#=====================================
#Create a random vector of size 30 and find the mean value
random_vector = np.random.rand(30)
mean_value = np.mean(random_vector)
print("Random vector of size 30:")
print(random_vector)
print(f"Mean value: {mean_value}")


#=====================================
# Solution for Case study 1 problem 10
#=====================================
#Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9
# Create a numpy array with elements from 0 to 10
array = np.arange(11)

# Negate all the elements between 3 and 9
array[(array >= 3) & (array <= 9)] *= -1

print("Array with elements 0 to 10, with elements between 3 and 9 negated:")
print(array)


#=====================================
# Solution for Case study 1 problem 11
#=====================================
#Create a random array of 3 rows and 3 columns and sort it according to 1st column, 2nd column or 3rd column.
# Create a random array of 3 rows and 3 columns
random_array_3x3 = np.random.randint(0,10,(3,3))
print("Original array:")
print(random_array_3x3)

# Sort the array according to the 1st column
sorted_by_first_column = random_array_3x3[random_array_3x3[:, 0].argsort()]
print("Array sorted by 1st column:")
print(sorted_by_first_column)

# Sort the array according to the 2nd column
sorted_by_second_column = random_array_3x3[random_array_3x3[:, 1].argsort()]
print("Array sorted by 2nd column:")
print(sorted_by_second_column)

# Sort the array according to the 3rd column
sorted_by_third_column = random_array_3x3[random_array_3x3[:, 2].argsort()]
print("Array sorted by 3rd column:")
print(sorted_by_third_column)



#=====================================
# Solution for Case study 1 problem 12
#=====================================
#Create a four dimensions array get sum over the last two axis at once. 
# Create a four-dimensional array
four_d_array = np.random.randint(0,10,(3, 3, 3, 3))
print("Original four-dimensional array:")
print(four_d_array)

# Get the sum over the last two axes at once
sum_over_last_two_axes = np.sum(four_d_array, axis=(-1, -2))
print("Sum over the last two axes:")
print(sum_over_last_two_axes, sum_over_last_two_axes.shape)


#=====================================
# Solution for Case study 1 problem 13
#=====================================
# Create a random array of 4 rows and 5 columns
random_array_4x5 = np.random.randint(0, 10, (4, 5))
print("Original array:")
print(random_array_4x5)

# Swap the first and last rows of the array
random_array_4x5[[0,1,2, 3]] = random_array_4x5[[3,1,2, 0]]
print("Array after swapping first and last rows:")
print(random_array_4x5)


#=====================================
# Solution for Case study 1 problem 14
#=====================================
# Create a random matrix of size 4x4
random_matrix = np.random.randint(0, 10, (4, 4))
print("Random matrix:")
print(random_matrix)

# Compute the rank of the matrix
matrix_rank = np.linalg.matrix_rank(random_matrix)
print(f"Rank of the matrix: {matrix_rank}")


#=====================================
# Solution for Case study 1 problem 15
#=====================================
# Analyze various school outcomes in Tennessee using pandas

# Load the dataset
school_data = pd.read_csv("775_m5_datasets_v1.0\middle_tn_schools.csv")

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(school_data.head())

# Descriptive statistics
print("Descriptive statistics of the dataset:")
print(school_data.describe())


# Check for missing values
print("Missing values in the dataset:")
print(school_data.isnull().sum())

#Isolates ‘reduced_lunch’ and groups the data by ‘school_rating’ using pandas groupby 
grouped_data = school_data.groupby('school_rating')['reduced_lunch']

# Apply the describe method on the grouped data
grouped_data_description = grouped_data.describe()
print("Descriptive statistics of 'reduced_lunch' grouped by 'school_rating':")
print(grouped_data_description)

# Calculate the correlation between 'reduced_lunch' and 'school_rating'
correlation = school_data['reduced_lunch'].corr(school_data['school_rating'])
print(f"Correlation between 'reduced_lunch' and 'school_rating': {correlation}")

# Scatter plot of school_rating vs reduced_lunch
plt.figure(figsize=(10, 6))
plt.scatter(school_data['reduced_lunch'], school_data['school_rating'], alpha=0.5)
plt.title('School Rating vs Reduced Lunch')
plt.xlabel('Percentage of Students on Reduced Lunch')
plt.ylabel('School Rating')
plt.show()

# Data visualization: Boxplot of reduced_lunch by school_rating
plt.figure(figsize=(10, 6))
school_data.boxplot(column='reduced_lunch', by='school_rating')
plt.title('Reduced Lunch by School Rating')
plt.xlabel('School Rating')
plt.ylabel('Percentage of Students on Reduced Lunch')
plt.show()

# Calculate the correlation matrix
   # One-hot encoding
school_data = pd.get_dummies(school_data, columns=['name','school_type'])
correlation_matrix = school_data.corr()

# Plot the correlation matrix
plt.figure(figsize=(12, 8))
plt.title('Correlation Matrix')
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.show()
