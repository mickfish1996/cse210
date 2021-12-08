from PIL import Image

image = Image.open("./assets/green_block1.png")

new_image = image.resize((50,50))

new_image.save("./assets/green_block.png")

