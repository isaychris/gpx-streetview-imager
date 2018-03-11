import os
import getcolor

indir = "C:\Users\Chris\Desktop\street_images"

print("Location: " + indir)
option = raw_input("Are you sure you want to clean from this location? [y/n]: ")

if option == "y" or "Y":
    print("Running script ...")

    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            file_path = os.path.join(indir, f)
            color = getcolor.get_color(file_path)

            if color[0] == '#e3e2dd' or color[0] == "#e3e2de":
                os.remove(file_path)
                print(" - Deleting " + file_path)

    print("Script completed ...")
