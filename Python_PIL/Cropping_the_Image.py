from PIL import Image

im = Image.open('MichiganCoverPhoto.png')

cropped = im.crop((1, 2, 300, 300))
# (L, U, R, B) represents defining the left, upper, right, and lower pixel coordinate.
cropped.show()
