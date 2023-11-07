#!/usr/bin/python3

# copy table from: https://en.vedur.is/earthquakes-and-volcanism/earthquakes#view=table
# paste to head of file: 'raw/2023.csv' and run "./clean_table.sh" on file.
# execute: 'python3 iceland_table2geojson.py'
# generate 3dplotly with: 'python3 iceland3d.py' or 'python3 iceland3d.py --input_file raw/2023-11-07.csv.geojson'

import argparse
import geojson
import datetime



parser = argparse.ArgumentParser(description='earthquakes')
parser.add_argument('--input_file', default="raw/2023.csv", help='input.csv')
args = parser.parse_args()

# Define the input file name
input_file = args.input_file

# Initialize a list to store earthquake features
earthquake_features = []

# Read earthquake data from the input file
with open(input_file, "r") as file:
	lines = file.readlines()

# Remove header and whitespace lines
lines = [line.strip() for line in lines if line.strip()]

# Loop through the earthquake data and create GeoJSON Features
for line in lines:
	parts = line.split('\t')
	print(parts)
	date_str = parts[0]
	time_str = parts[1]
	latitude = float(parts[2])
	longitude = float(parts[3])
	depth = float(parts[4].strip('km'))
	magnitude = float(parts[5])
	quality = float(parts[6])
	location = ' '.join(parts[7:])

	# Parse date and time into a single datetime object
	date_time = datetime.datetime.strptime(date_str + " " + time_str, "%d.%m.%Y %H:%M:%S")

	# Create a GeoJSON Feature
	feature = geojson.Feature(
		geometry=geojson.Point((longitude, latitude, depth)),
		properties={
			"Date": date_time.strftime("%Y-%m-%d"),
			"Time": date_time.strftime("%H:%M:%S"),
			"Magnitude": magnitude,
			"Quality": quality,
			"Location": location,
		},
	)

	earthquake_features.append(feature)

# Create a GeoJSON FeatureCollection
feature_collection = geojson.FeatureCollection(earthquake_features)

# Write the GeoJSON data to a file
outfile = input_file + ".geojson"
with open(outfile, "w") as geojson_file:
	geojson.dump(feature_collection, geojson_file, indent=2)
	print("GeoJSON data has been written to:", outfile)
