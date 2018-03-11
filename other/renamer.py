import os

indir = "C:\Users\Chris\Desktop\street_images"
name = "image"

print("Running script ...")

for root, dirs, filenames in os.walk(indir):
    for i, file in enumerate(filenames):
        file_path = os.path.join(indir, file)
        new_name = name + str(i) + ".jpg"

        os.rename(file_path, os.path.join(indir, new_name))
        print(" - renaming [" + file + "] to [" + new_name + "]")

print("Script completed ...")
