# This program was made by github.com/HowardZHY and licensed under MIT.
# Imports
from PIL import Image

# Input file name
png = Image.open('in.png')

print('Format：', png.format)
print('Size：', png.size)
print('Width：', png.width)
print('Height：', png.height)

# Program
for x in range(png.width):
    for y in range(png.height):
        r, g, b, a = png.getpixel((x, y))
        # Remove more semi transparent pixels
        if a != 0 and a <= 100:
            png.putpixel((x, y), (r, g, b, 0))
        # Make more pixels opaque
        if a != 0 and a >= 101:
            png.putpixel((x, y), (r, g, b, 255))

# Output file name
png.save('out.png')
