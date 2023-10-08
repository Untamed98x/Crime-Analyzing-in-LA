# Import necessary libraries/modules
import os  # Import the 'os' module for working with file paths and directories
import pandas as pd  # Import the 'pandas' library for data manipulation
import matplotlib.pyplot as plt  # Import 'matplotlib.pyplot' for data visualization
import seaborn as sns  # Import 'seaborn' for enhanced data visualization
import folium as fl  # Import 'folium' for creating interactive maps

# 1. Load Data
csv_file_path = "/Users/muhammadfauzy/Documents/1. FOLDER KERJAAN/1. Data Analyst /2. DataSet/DataSet - CRIME IN LA PROJECT/crime_in_la.csv"
delimiter = ','  # Define the delimiter used in the CSV file
data = pd.read_csv(csv_file_path, sep=delimiter)  # Read the CSV data into a Pandas DataFrame

# 2. Display After Load
print("First 5 rows of the DataFrame:")
print(data.head(5))  # Display the first 5 rows of the loaded DataFrame

# Calculate summary statistics
summary_stats = data.describe(percentiles=[0.25, 0.5, 0.75])
print(summary_stats)  # Display summary statistics of the data

# Identify missing values
missing_values = data.isna().sum()
print("Missing Values:")
print(missing_values)  # Display the count of missing values in each column

# Check data types
data_types = data.dtypes
print("Data Types:")
print(data_types)  # Display data types of columns

# 3. Remove Missing rows
data_cleaned = data.dropna(subset=["Premis Desc"])  # Remove rows with missing values in the "Premis Desc" column
print("First 5 rows of the cleaned DataFrame:")
print(data_cleaned.head(5))  # Display the first 5 rows of the cleaned DataFrame

# Check missing values in the cleaned data
missing_values_cleaned = data_cleaned.isna().sum()
print("Missing Values in Cleaned Data:")
print(missing_values_cleaned)  # Display missing values in the cleaned data

# 4. Data Visualization
# Create a histogram of victim ages
plt.hist(data['Vict Age'], bins=20, edgecolor='k')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Victim Ages')
plt.show()

# Create a countplot of crime counts by area name
plt.figure(figsize=(12, 6))
sns.countplot(x='AREA NAME', data=data, order=data['AREA NAME'].value_counts().index)
plt.xticks(rotation=90)
plt.xlabel('Area Name')
plt.ylabel('Crime Count')
plt.title('Crime Counts by Area')
plt.show()

# Create a scatter plot of crime locations
plt.figure(figsize=(10, 6))
plt.scatter(data['LON'], data['LAT'], alpha=0.5, c='b')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Crime Locations in LA')
plt.show()

# Create a boxplot of crime code distribution by area name
plt.figure(figsize=(12, 6))
sns.boxplot(x='AREA NAME', y='Crm Cd', data=data)
plt.xticks(rotation=90)
plt.xlabel('Area Name')
plt.ylabel('Crime Code')
plt.title('Crime Code Distribution by Area')
plt.show()

# Continue with additional code...
