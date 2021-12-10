import PIL.Image
from PIL import Image
import glob

# Create the frames
frames = []
imgs = glob.glob("../data/video/*.jpg")

# Put the frames in order from numbers
imgs.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))


for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
    print(i)

# Save into a GIF file that loops forever
frames[0].save('../data/video/video.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=0.1, loop=0)
