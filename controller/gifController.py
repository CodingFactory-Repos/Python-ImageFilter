import PIL.Image
from PIL import Image
import glob

# Create the frames
frames = []
imgs = glob.glob("../data/output/*.jpg")

# Put the frames in order from numbers
imgs.sort()


for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
    print(i)

# Save into a GIF file that loops forever
frames[0].save('../data/output/video.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=0.1, loop=0)
