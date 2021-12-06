from types import NoneType
import folium
import csv
import time

#TEST
# The record of a catch. Replace with Mikkel's data model when GITHUB is working
class catch:
    # Attributes of a catch
    fish = ""
    time = time.time()
    latitude = 0
    longitude = 0
    weight = 0
    length = 0
    method = ""
    fisherman = "Gert Villemos"

    # Initi function used to create a catch object and set the attributes
    def __init__(self, iFish, iTime, iLatitude, iLongitude, iWeight, iLength, iMethod) :
        self.fish = iFish
        self.time = time.localtime(int(iTime))
        self.latitude = iLatitude
        self.longitude = iLongitude
        self.weight = iWeight
        self.length = iLength
        self.method = iMethod

# Class to read in a comma separate list file of cathes
class datastore :
    # Our list of all catches
    filename = "Catches.txt"
    data = []

    # Read in the catches from the file
    def read (self) :
        # Open the file
        with open(self.filename) as csv_file:
            # Read in all the rows. Split each row based on the ','
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Iterate through each row of the file
            for row in csv_reader:
                # If this is a comment line (i.e. starts with a '#') then ignore. Continue go back to the for loop
                if (row[0].startswith("#")) :
                    continue
                # Create a 'catch' object, parsing the values of the row to the __init__ function
                self.data.append(catch(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))    

# We use the 'Folium' module to show maps
# https://python-visualization.github.io/folium/quickstart.html

# Hardcoded position is Roervig :)
# In the future make this either the current position of the mobile phone or a selected position
position = [55.95705419727239, 11.77694151701307]
m = folium.Map(position)

# Create the data store and read in the data
store = datastore()
store.read()

# Dictionary for the colors of the markers 
# http://www.compciv.org/guides/python/fundamentals/dictionaries-overview/
# The color codes used for the markers on the map depending on fish type. If a Havoerred, then red... etc
markerColors = {"Havoerred":"red", "Hornfisk":"green", "Makrel":"blue","Fladfisk":"orange"}

# Iterate through all 'catch' objects in the data that we read in
for eineFang in store.data :
    # Format the time to be the format DD/DD/YYYY, HH:MM:SS
    atTime = time.strftime("%d/%m/%Y, %H:%M:%S", eineFang.time)

    # Set the color of the marker. If the fish is not found in the map of colors, use the color gray
    markerColor = markerColors.get(eineFang.fish)
    if markerColor == None :
        markerColor = "gray"

    # Add the market to the map
    folium.Marker(
        [eineFang.latitude, eineFang.longitude], 
        popup=f"<b>{eineFang.weight} g, {eineFang.length} cm, {atTime}</b>", 
        tooltip=f"{eineFang.fish}",
        icon = folium.Icon(color=markerColor, icon="info-sign"),
    ).add_to(m)

# Create the HTML file showing the markers
m.save("index.html")