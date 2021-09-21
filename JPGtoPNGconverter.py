import sys
import os
from PIL import Image

'''commmand line args for the path and folder where the images are located'''

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')


