
from PIL import Image,ImageFilter
#read image
im = Image.open('crossarm_crack.JPG')
#display
im.show()

from PIL import ImageEnhance
enh = ImageEnhance.Contrast(im)
enh.enhance(1.8).show("30% more contrast")