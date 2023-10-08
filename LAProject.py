# Import Library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium as fl  # Import folium library

# 1. Load Data

## Define file paths for CSV and latitude data
csv_file_path = "/Users/muhammadfauzy/Documents/1. FOLDER KERJAAN/1. Data Analyst /2. DataSet/DataSet - CRIME IN LA PROJECT/crime_in_la.csv"

# Load data from CSV
delimiter = ','
data = pd.read_csv(csv_file_path, sep=delimiter)

# 2. Display After Load

## Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(data.head(5))

# Data Exploration - Summary statistics with specific percentiles
summary_stats = data.describe(percentiles=[0.25, 0.5, 0.75])
print(summary_stats)

# Check Missing Values
missing_values = data.isna().sum()
print("Missing Values:")
print(missing_values)

# Check Data Types
data_types = data.dtypes
print("Data Types:")
print(data_types)

# 3. Remove Missing rows 

## Remove rows with missing values in the "Premis Desc" column
data_cleaned = data.dropna(subset=["Premis Desc"])

# Display the first 5 rows of the cleaned DataFrame
print("First 5 rows of the cleaned DataFrame:")
print(data_cleaned.head(5))

# Check if there are any missing values left in the cleaned data
missing_values_cleaned = data_cleaned.isna().sum()
print("Missing Values in Cleaned Data:")
print(missing_values_cleaned)

# 4. Data Visualization

## Create a histogram of victim ages
plt.hist(data['Vict Age'], bins=20, edgecolor='k')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Victim Ages')
plt.show()

## Create a bar chart of crime counts by area
plt.figure(figsize=(12, 6))
sns.countplot(x='AREA NAME', data=data, order=data['AREA NAME'].value_counts().index)
plt.xticks(rotation=90)
plt.xlabel('Area Name')
plt.ylabel('Crime Count')
plt.title('Crime Counts by Area')
plt.show()

## Create a scatter plot of latitude vs. longitude
plt.figure(figsize=(10, 6))
plt.scatter(data['LON'], data['LAT'], alpha=0.5, c='b')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Crime Locations in LA')
plt.show()

## Create a box plot of crime counts by area
plt.figure(figsize=(12, 6))
sns.boxplot(x='AREA NAME', y='Crm Cd', data=data)
plt.xticks(rotation=90)
plt.xlabel('Area Name')
plt.ylabel('Crime Code')
plt.title('Crime Code Distribution by Area')
plt.show()

## Create a correlation heatmap for numeric columns
numeric_columns = ['DR_NO', 'AREA', 'Rpt Dist No', 'Crm Cd', 'Vict Age', 'Weapon Used Cd', 'LAT', 'LON']
correlation_matrix = data[numeric_columns].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap for Numeric Columns')
plt.show()

# Create a base map centered around Los Angeles
m = fl.Map(location=[34.0522, -118.2437], zoom_start=10)

# Iterate through your dataset to add markers for each crime location
for index, row in data.iterrows():
    # Extract latitude and longitude
    lat, lon = row['LAT'], row['LON']
    
    # Create a popup message with additional information about the crime
    popup_text = f"Crime Code: {row['Crm Cd']}<br>Area: {row['AREA NAME']}"

    # Add a marker for each crime location
    fl.Marker([lat, lon], popup=popup_text).add_to(m)

# Display the map
m.save('crime_map.html')
