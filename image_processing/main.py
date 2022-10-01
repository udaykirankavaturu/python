from PIL import Image, ImageFilter
img = Image.open('./pokedex/pikachu.jpg')

# blur an image using blur filter
filtered_image = img.filter(ImageFilter.BLUR).save(
    './pokedex/blurred_pikachu.png', 'png')


# grey scale an image
greyscale_image = img.convert('L').save('./pokedex/grey_pikachu.png', 'png')

# resize img.resize
# crop img.crop
# use img.thumbnail to keep aspect ratio
img.thumbnail((400, 200))
img.save('./pokedex/thumbnail_pikachu.png')
