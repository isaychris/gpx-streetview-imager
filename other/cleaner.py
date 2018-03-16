import os

indir = "C:\Users\Chris\Desktop\street_images"

print("Running script ...")
clean_count = 0

for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        file_path = os.path.join(indir, f)
        image_size = os.path.getsize(file_path)

        if image_size < 9000:
            os.remove(file_path)
            print(" - Deleting " + file_path)
            clean_count += 1

print("Script completed ... Amount cleaned = " + str(clean_count))
