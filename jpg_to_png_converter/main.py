import sys
import os
from PIL import Image

# grab two folder arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# if second argument folder doesn't exist, create the folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through first argument folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')

    # convert all jpg to png
    if img.format == 'JPEG':
        only_name = os.path.splitext(filename)
        # save to the second argument folder
        img.save(f'{output_folder}{only_name[0]}.png', 'png')
