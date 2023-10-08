import os  # Add the 'os' module import

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium as fl

# 1. Load Data
csv_file_path = "/Users/muhammadfauzy/Documents/1. FOLDER KERJAAN/1. Data Analyst /2. DataSet/DataSet - CRIME IN LA PROJECT/crime_in_la.csv"
delimiter = ','
data = pd.read_csv(csv_file_path, sep=delimiter)

# 2. Display After Load
print("First 5 rows of the DataFrame:")
print(data.head(5))

summary_stats = data.describe(percentiles=[0.25, 0.5, 0.75])
print(summary_stats)

missing_values = data.isna().sum()
print("Missing Values:")
print(missing_values)

data_types = data.dtypes
print("Data Types:")
print(data_types)

# 3. Remove Missing rows
data_cleaned = data.dropna(subset=["Premis Desc"])
print("First 5 rows of the cleaned DataFrame:")
print(data_cleaned.head(5))

missing_values_cleaned = data_cleaned.isna().sum()
print("Missing Values in Cleaned Data:")
print(missing_values_cleaned)

# 4. Data Visualization
plt.hist(data['Vict Age'], bins=20, edgecolor='k')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Victim Ages')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='AREA NAME', data=data, order=data['AREA NAME'].value_counts().index)
plt.xticks(rotation=90)
plt.xlabel('Area Name')
plt.ylabel('Crime Count')
plt.title('Crime Counts by Area')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(data['LON'], data['LAT'], alpha=0.5, c='b')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Crime Locations in LA')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='AREA NAME', y='Crm Cd', data=data)
plt.xticks(rotation=90)
plt.xlabel('Area Name')
plt.ylabel('Crime Code')
plt.title('Crime Code Distribution by Area')
plt.show()

import os
import pandas as pd
import folium
from folium.plugins import HeatMap

# Load the data
csv_file_path = "/Users/muhammadfauzy/Documents/1. FOLDER KERJAAN/1. Data Analyst /2. DataSet/DataSet - CRIME IN LA PROJECT/crime_in_la.csv"
delimiter = ','
data = pd.read_csv(csv_file_path, sep=delimiter)

# Calculate crime counts by location (latitude and longitude)
crime_counts = data.groupby(['LAT', 'LON']).size().reset_index(name='CrimeCount')

# Sort the locations by crime counts in descending order
top_10_locations = crime_counts.sort_values(by='CrimeCount', ascending=False).head(10)

# Create a base map
m = folium.Map(location=[34.0522, -118.2437], zoom_start=10)

# Create a HeatMap for the top 10 crime locations
heat_data = [[row['LAT'], row['LON'], row['CrimeCount']] for index, row in top_10_locations.iterrows()]
HeatMap(heat_data, gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'orange', 1: 'red'}).add_to(m)

# Save the map to an HTML file
map_html_file = "top_10_crime_heatmap.html"
m.save(map_html_file)

print("Top 10 crime heatmap has been saved to", map_html_file)


import os
import pandas as pd
import folium

# Filter the data for the Harbor area
harbor_data = data[data['AREA NAME'] == 'Harbor']

# Calculate crime counts by location (latitude and longitude) in the Harbor area
crime_counts = harbor_data.groupby(['LAT', 'LON']).size().reset_index(name='CrimeCount')

# Sort the locations by crime counts in descending order
top_30_locations = crime_counts.sort_values(by='CrimeCount', ascending=False).head(30)

# Create a base map centered around Harbor
m = folium.Map(location=[33.7544, -118.2786], zoom_start=12)

# Add pin markers for the top 30 locations
for index, row in top_30_locations.iterrows():
    folium.Marker(
        location=[row['LAT'], row['LON']],
        popup=f"Location: {row['LAT']}, {row['LON']}<br>Crime Count: {row['CrimeCount']}",
        icon=folium.Icon(color='red', icon='glyphicon glyphicon-map-marker')
    ).add_to(m)

# Save the map to an HTML file
map_html_file = "top_30_crime_locations_in_harbor.html"
m.save(map_html_file)

print("Top 30 crime locations in Harbor have been saved to", map_html_file)
