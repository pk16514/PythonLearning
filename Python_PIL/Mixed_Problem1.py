from PIL import Image

img1 = Image.open('goldygopher.png')
img2 = Image.open('img1.jpg')

img2_resize = img2.resize(img1.size)

contact_sheet = Image.new('RGB', (2 * img1.width, img1.height))

contact_sheet.paste(img1, (0, 0))
contact_sheet.paste(img2_resize, (img1.size[0], 0))

contact_sheet.save('goldygopher_in_Taiwan.jpg')
img3 = Image.open('goldygopher_in_Taiwan.jpg')

img3.show()
