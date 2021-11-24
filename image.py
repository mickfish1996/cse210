from PIL import Image

image = Image.open("./final/assets/block.png")
image = image.resize((50,50),Image.ANTIALIAS)

image.save(fp="block1.png")
