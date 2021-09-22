from image_vector import ImageVector
from vectors import scale


gray_50_light = ImageVector([scale(255*0.5, (1, 1, 1)) for _ in range(0, 300*300)])
# gray_50_light.image().show()


# print(len(groupBy(gray_50_light.pixels, 300)))


image_1 = ImageVector('cartman.jpg')

image_1.blurred_image(block_size=3).image().show()
