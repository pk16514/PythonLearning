from PIL import Image
image = Image.open('cy.png')
# image.show()
image.save('cy.jpg')
image1 = Image.open('cy.jpg')
image1.show()
