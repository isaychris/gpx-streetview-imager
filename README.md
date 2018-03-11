# gpx-streetview-imager
This python script will pull google street images along a given path specified by a .gpx file

# Prerequisites
- Python 2
- .gpx file (instructions below)
- Google API key from https://developers.google.com/maps/documentation/streetview/.

# Creating a path
Creating a path to use in the script is easy.
1) Go to https://www.plotaroute.com/routeplanner
2) Enter the location you want to take streetview images from.
3) Change Auto Pilot to 'On Foot'
4) Enable Streetview Overlay.
5) Create your desired route along the blue streetview paths.
6) Download and save as 'File type: GPX, File Format: GPX, GPX TYPE: Track'. 

# Running the script
1) Get your .gpx file and put it in the same directory as the script.
2) Open the script and change the API_KEY, SAVE_PATH, and GPX_FILE variables.

3) Run the script
Usage: [python street.py]
