# Earthquakes Visualization in 3D

# Iceland Grindavík - Event Nov 2023

This repository contains a Python script for visualizing earthquake data using Plotly.

The script reads earthquake data from a GeoJSON file and creates an interactive 3D scatter plot of earthquakes in the Iceland region.

You can customize the time period and data file to visualize earthquakes in a specific area and time frame.

## Usage

To use this script, follow these steps:

1. Clone this repository to your local machine or download the script directly.

2. Make sure you have Python installed on your system.

3. Install the required Python packages using pip:

```bash
pip install plotly
```

4. Run the script with the following command:

```bash
python iceland3d.py --data_file <path_to_geojson_file>
```

Replace `<number_of_days>` with the number of days you want to consider for earthquake data visualization and `<path_to_geojson_file>` with the path to the GeoJSON file containing earthquake data.

## Command-Line Arguments

- `--days`: Specify the number of days to consider for earthquake data visualization. By default, it is set to -1, which means it includes all available data.

- `--data_file`: Specify the path to the GeoJSON file containing earthquake data. By default, it is set to "raw/2023.csv.geojson".

## Visualization Features

The script provides the following features in the visualization:

- 3D scatter plot: Displays earthquake data on a 3D plot, with the x and y coordinates representing longitude and latitude, and the z coordinate representing the depth of the earthquake.

- Color-coded markers: The markers are color-coded based on the magnitude of the earthquakes, making it easier to identify their intensity.

- Interactive plot: You can interact with the plot by zooming in, panning, and hovering over data points to view additional information about each earthquake.

- Additional markers: The script also adds specific location markers in the Iceland region for reference.

## Output

The script generates an HTML file that contains the interactive earthquake visualization. You can open this file in a web browser to explore the earthquake data in 3D.

## Generated 3D Plotly for Iceland Region - Grindavík - Event Nov 2023:

- [2023-11-09](https://earthquake.batjorge.com/iceland/grindavik/2023-11-09.csv.geojson.html)
- [2023-11-08](https://earthquake.batjorge.com/iceland/grindavik/2023-11-08.csv.geojson.html)
- [2023-11-07](https://earthquake.batjorge.com/iceland/grindavik/2023-11-07.csv.geojson.html)
- [2023-11-06](https://earthquake.batjorge.com/iceland/grindavik/2023-11-06.csv.geojson.html)
- [2023-11-05](https://earthquake.batjorge.com/iceland/grindavik/2023-11-05.csv.geojson.html)
- [2023-11-04](https://earthquake.batjorge.com/iceland/grindavik/2023-11-04.csv.geojson.html)
- [Combined](https://earthquake.batjorge.com/iceland/grindavik/2023.csv.geojson.html)

## Note

The script filters earthquake data based on the provided time frame and geographical boundaries to ensure the plot only includes relevant information.

Feel free to customize the script's parameters to analyze earthquake data for different time periods and regions in Iceland.

**Author**: [earthquake.batjorge.com](https://earthquake.batjorge.com)

**License**: This project is licensed under the GNU GPLv3
