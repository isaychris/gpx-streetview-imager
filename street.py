import os
import re
import urllib
import random
import sys

# Create a route from:
# https://www.plotaroute.com/routeplanner

GPX_FILE = open('brooklyn.gpx').read()
SAVE_PATH = "C:\Users\Chris\Desktop\street_images"
API_KEY = "&key=" + "API_KEY_HERE"

SIZE = "1200x800"   # currently limited to 600x600.

# Grab all of the "trkpt" elements
def getStreet(address, save_path):
    base = "https://maps.googleapis.com/maps/api/streetview?size=" + SIZE

    location = "&location=" + address
    heading = "&heading=" + str(random.randint(0, 360))  # random horizontal angle
    url = base + location + heading + API_KEY

    file_name = address + ".jpg"
    urllib.urlretrieve(url, os.path.join(save_path, file_name))

# parse gpx file for coordinates
matches = re.findall('<trkpt lat="([-0-9\.]+)" lon="([-0-9\.]+)">', GPX_FILE)

# create array of coordinates
coordinates = [lat + ',' + lon for lat, lon in matches]

# ==========================================================================================================

print('Running script ...')

start = 0
amount = len(coordinates)

for i in range(start, amount):
    getStreet(coordinates[i], SAVE_PATH)
    sys.stdout.write("\r" + "[" + str(i) + " / " + str(amount - 1) + "] " + "Location: " + coordinates[i])
    sys.stdout.flush()

print('\n Script completed ...')
