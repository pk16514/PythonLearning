from PIL import Image
img1 = Image.open('luther.jpg')
img2 = Image.open('goldygopher.png')
img1copy = img1.copy()
img2copy = img2.copy()
img1copy.paste(img2copy, (85, 80))
# (x, y) represents location
img1copy.save('luther_goldygopher.bmp')
