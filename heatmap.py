import pandas as pd
df = pd.read_csv('Booking Records - BookingDataAnon.csv')

sample_df = df.head(10)
# sample_df.to_csv('sample_df.csv')

import numpy as np

# Simulating latitude and longitude for each record based on the city.
# This is a simplified approximation for demonstration purposes.
np.random.seed(42)  # For reproducibility

# Generate random latitudes and longitudes within a plausible range for demonstration
# Assuming the dataset is from a specific region (e.g., around Tennessee based on the city names)
latitudes = np.random.uniform(low=35.0, high=36.0, size=len(sample_df))
longitudes = np.random.uniform(low=-85.5, high=-84.5, size=len(sample_df))

# Adding these coordinates to the dataframe
sample_df['Latitude'] = latitudes
sample_df['Longitude'] = longitudes

# Display the updated dataframe with latitudes and longitudes
sample_df[['CITY', 'ZIP_CODE', 'Latitude', 'Longitude']].head()

import folium
from folium.plugins import HeatMap

# Create a base map
m = folium.Map(location=[35.5, -85.0], zoom_start=10)

# Add the heatmap layer
HeatMap(sample_df[['Latitude', 'Longitude']]).add_to(m)

# Save the heatmap to an HTML file (for visualization purposes)
heatmap_file_path = 'crime_heatmap.html'
m.save(heatmap_file_path)

heatmap_file_path

