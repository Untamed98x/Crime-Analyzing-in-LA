Crime Data Analysis and Visualization

This code performs data analysis and visualization on a dataset related to crime in Los Angeles. It uses Python libraries such as Pandas, Matplotlib, Seaborn, and Folium to load, clean, explore, and visualize the data.

Step 1: Load Data
We start by importing the necessary libraries and loading the crime dataset from a CSV file using Pandas.
The dataset is loaded with specified delimiter and path.
Step 2: Data Overview
We provide an overview of the loaded data.
Display the first 5 rows of the DataFrame.
Calculate summary statistics (mean, standard deviation, quartiles).
Identify missing values in the dataset.
Check data types of columns.
Step 3: Data Cleaning
We clean the data by removing rows with missing values in the "Premis Desc" column.
The cleaned DataFrame is displayed along with the count of missing values in the cleaned data.
Step 4: Data Visualization
We create various data visualizations to gain insights into the dataset:
Histogram: Visualizes the distribution of victim ages.
Count Plot: Shows crime counts by area.
Scatter Plot: Displays crime locations on a map.
Box Plot: Explores the distribution of crime codes by area.
Step 5: Creating a Crime Heatmap (Folium)
We import the Folium library to create interactive maps.
Calculate crime counts by location (latitude and longitude), sort them, and select the top 10 locations.
Create an interactive heatmap using Folium, where colors represent crime counts.
Save the heatmap as an HTML file for further use.
Step 6: Creating Pinpoint Markers for Top Crime Locations in the Harbor Area (Folium)
We filter the data for the Harbor area and calculate crime counts.
Select the top 30 crime locations in the Harbor area based on crime count.
Create pinpoint markers for these locations using Folium, including location details and crime count.
Save the pinpoint marker map as an HTML file.
This code provides a comprehensive analysis of the crime dataset and showcases data visualization skills. The interactive maps created with Folium add a dynamic aspect to the analysis, making it suitable for presentations and sharing insights about crime in Los Angeles.
