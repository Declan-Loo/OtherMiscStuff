#Found this code on Twitter. Decided to try it on a random photo.

from PIL import Image

color_image = Image.open("FOM2ODeXEAAqvR9.jpg")
gray_scale = color_image.convert("L")
gray_scale.save("gray_image.jpg")
