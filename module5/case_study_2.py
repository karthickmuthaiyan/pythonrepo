import numpy as np
import pandas as pd

#Read the three csv files which contains the score of same students in term1 for each Subject
#MathScoreTerm1.csv, PhysicsScoreTerm1.csv, DSSScoreTerm1.csv
course1=pd.read_csv("775_m5_datasets_v1.0/MathScoreTerm1.csv")
course2= pd.read_csv("775_m5_datasets_v1.0/PhysicsScoreTerm1.csv")
course3= pd.read_csv("775_m5_datasets_v1.0/DSScoreTerm1.csv")

# Convert ethnicity to numerical value
#ethnicity_mapping = {ethnicity: idx for idx, ethnicity in enumerate(course1['Ethinicity'].unique(), start=1)}
#course1['Ethinicity'] = course1['Ethinicity'].map(ethnicity_mapping)
#course2['Ethinicity'] = course2['Ethinicity'].map(ethnicity_mapping)
#course3['Ethinicity'] = course3['Ethinicity'].map(ethnicity_mapping)
#print(course1.head(5))


# Remove the name and ethnicity column (to ensure confidentiality)  - use the iloc method
course1 = course1.drop(columns=['Name', 'Ethinicity'])
course2 = course2.drop(columns=['Name', 'Ethinicity'])
course3 = course3.drop(columns=['Name', 'Ethinicity'])

#Fill the missing score for a student to the average of the class 
course1.fillna(course1['Score'].mean(), inplace=True)
course2.fillna(course2['Score'].mean(), inplace=True)
course3.fillna(course3['Score'].mean(), inplace=True)

# Fill missing score data with zero
#course1 = course1.fillna(0)
#course2 = course2.fillna(0)
#course3 = course3.fillna(0)


# Merge the three files
merged_courses = pd.merge(course1, course2, on=['ID', 'Sex','Age'])
merged_courses = pd.merge(merged_courses, course3, on=['ID', 'Sex','Age'])


# Change Sex(M/F) Column to 1/2 for further analysis
merged_courses['Sex'] = merged_courses['Sex'].map({'M':1,'F':2})

merged_courses=merged_courses.iloc[:, [4,1,3,2,0,6,5,8,7]]
merged_courses.columns = ['ID','Age','Sex', 'Subject_x','Math_Score','Subject_y', 'Physics_score', 'Subject_z', 'DS_score']
print(merged_courses.head(5))

# Store the data in new file – ScoreFinal.csv
merged_courses.to_csv("775_m5_datasets_v1.0\ScoreFinal.csv", index=False)
print("Data stored in ScoreFinal.csv file")
print(merged_courses.head(5))
