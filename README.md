# gpx-streetview-imager
This python script will pull google street images along a given path specified by a .gpx file

![Image](https://i.imgur.com/DJVnF7e.png)

# Prerequisites
- Python 2
- .gpx file (instructions below)
- Google API key from https://developers.google.com/maps/documentation/streetview/.

# Creating a path
Creating a path to use in the script is easy.
![Image](https://i.imgur.com/J8HoO1n.png)
1) Go to https://www.plotaroute.com/routeplanner
2) Enter the location you want to take streetview images from.
3) Change Auto Pilot to 'On Foot'
4) Enable Streetview Overlay.
5) Create your desired route along the blue streetview paths. The number of points plotted shown on the top right corner is a good indiction of how many images the script will pull.
6) Download and save as 'File type: GPX, File Format: GPX, GPX TYPE: Track'. 

# Running the script
1) Put your .gpx file in the same directory as the script.
2) Open the script and change the API_KEY, SAVE_PATH, and GPX_FILE variables.
3) Run the script
```Python
python street.py
```
