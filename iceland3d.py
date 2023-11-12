import argparse
import datetime
import json
import os
import plotly.graph_objs as go
import plotly.offline as offline


parser = argparse.ArgumentParser(description='earthquakes')
parser.add_argument('--days', default=-1, type=int, help='last N days to render')
parser.add_argument('--data_file', default="raw/2023.csv.geojson", help='file.geojson')
args = parser.parse_args()

# Load earthquake data from the provided JSON data
with open(args.data_file, "r") as json_file:
	earthquake_data = json.load(json_file)

current_datetime = datetime.datetime.now()
gendate = current_datetime.strftime("%Y-%m-%dT%H:%M")

region = [
	{
		"name": "Grindavík",
		"longitude": -22.4348480127527,
		"latitude": 63.84358958190957,
	},
	{
		"name": "Grindavíkurkirkja eldri",
		"longitude": -22.438422498593873,
		"latitude": 63.837286012244014,
	},
	{
		"name": "Portið Grindavík",
		"longitude": -22.429859259439127,
		"latitude": 63.83793672960795,
	},
	{
		"name": "Hrafn Sveinbjarnarson III Ship Wreck",
		"longitude": -22.42317085222815,
		"latitude": 63.83148227026306,
	},
	{
		"name": "Naval Radio Transmitter Facility - Grindavik",
		"longitude": -22.43464288348724,
		"latitude": 63.850764739286134,
	},
	{
		"name": "BIOEFFECT Greenhouse",
		"longitude": -22.42069411012411,
		"latitude": 63.855415144648106,
	},
	{
		"name": "Bláa Lónið - Blue Lagoon",
		"longitude": -22.448767259207447,
		"latitude": 63.88107463521137,
	},
	{
		"name": "The Retreat at Blue Lagoon Iceland",
		"longitude":  -22.449755323363437,
		"latitude": 63.880195190088344,
	},
]

points_coordinates = {
	"region": region
}

points_coords = points_coordinates["region"]

# Extract earthquake information (coordinates x, y, z, and magnitude mag)
x_coords = []
y_coords = []
z_coords = []
magnitudes = []
datas = []
amt = 0
BOUNDS = {	"north": 66.5365,	"south": 63.3926,	"east": -13.4950,	"west": -24.5469}
#BOUNDS = {	"north": 64.35,	"south": 63.35,	"east": -22.0,	"west": -23.0}

for feature in earthquake_data["features"]:
	x_lon, y_lat, z = feature["geometry"]["coordinates"]
	mag = feature["properties"]["Magnitude"]
	edate1 = feature["properties"]["Date"]
	edate2 = feature["properties"]["Time"]
	if args.days > 0:
		time_obj = datetime.datetime.strptime(edate1, edate2, "%Y-%m-%dT%H:%M:%S.%f")
		# Calculate the date X days ago from the current date
		days_ago = datetime.datetime.now() - datetime.timedelta(days=args.days)
		if time_obj < days_ago:
			#print("The time is not within the last X days.")
			continue

	place = feature["properties"]["Location"]
	depth = float(z * -1)

	if (depth < -12.0) or \
		(x_lon < BOUNDS['west']) or \
		(x_lon > BOUNDS['east']) or \
		(y_lat < BOUNDS['south']) or \
		(y_lat > BOUNDS['north']):
		continue
	data = "Mag:" + str(mag) + " Date:" + edate1 + edate2 + " Place:"  + place
	datas.append(data)
	x_coords.append(x_lon)
	y_coords.append(y_lat)
	z_coords.append(depth)
	magnitudes.append(mag)
	amt += 1

print("DataPoints", str(amt))
if amt == 0:
	exit

# Create a 3D scatter plot
trace = go.Scatter3d(
	x=x_coords,
	y=y_coords,
	z=z_coords,
	mode="markers",
	marker=dict(size=5, color=magnitudes, colorscale="Viridis", opacity=0.8, colorbar=dict(title='Magnitude')),
	text=datas,
)

layout = go.Layout(
	scene=dict(
		xaxis=dict(title="Longitude", tickmode="linear", dtick = 0.25),
		yaxis=dict(title="Latitude", tickmode="linear", dtick = 0.25),
		zaxis=dict(title="Depth (km)", tickmode="linear", tick0 = 0.5, dtick = 0.5),
	),
	margin=dict(l=0, r=0, b=0, t=40),
	title="Earthquakes in Iceland Region: last " + str(args.days) + " days (generated: " + gendate +") DataPoints: "+str(amt),
	showlegend=False,
)

fig = go.Figure(data=[trace], layout=layout)

# Add points_coords as markers at height 0
for point in points_coords:
	fig.add_trace(
		go.Scatter3d(
			x=[point['longitude']],
			y=[point['latitude']],
			z=[0],  # Height 0
			mode='markers+text',
			marker=dict(
				size=2,
				color='red',  # You can choose a color for the markers
				symbol='circle',  # You can choose a marker symbol
			),
			text=point['name'],
			name=point['name']
		)
	)


# Save the plot to an HTML file and display it
file_name = os.path.basename(args.data_file)
html_file = "out/"+file_name+".html"
print("wrote: html_file:", html_file)
offline.plot(fig, filename=html_file, auto_open=False)
