import pprint
from _6_1_generalizing_vectors import Vector
from utils import average_of_tuple_lists, averaged_tuple_lists
from math import *
from PIL import Image

pp = pprint.PrettyPrinter(indent=2)

class ImageVector(Vector):
    size = (300, 300)

    def __init__(self, input):
        try:
            # The constructor accepts the name of an image file.
            # We create an Image object with PIL, resize it to 300x300, and then extract its list of pixels with the getdata() method.
            # Each pixel is a triple consisting of red, green, and blue values.
            img = Image.open(input).resize(ImageVector.size)
            self.pixels = img.getdata()
        except:
            #  The constructor also accepts a list of pixels directly.
            self.pixels = input

    def image(self):
        '''
        This method returns the underlying PIL image,
        reconstructed from the pixels stored as an attribute on the class.
        The values must be converted to integers to create a displayable image.
        '''
        img = Image.new('RGB', ImageVector.size)
        img.putdata([(int(r), int(g), int(b)) for (r, g, b) in self.pixels])
        return img

    def blurred_image(self, block_size=10):
        '''
        this method blurs an image based on the given block size
        '''
        block_count = int((ImageVector.size[0]/block_size)*(ImageVector.size[1]/block_size))
        groups = []
        group = []
        pixels_rgb_count = self.get_pixels_in_picture()
        pixels_count_row = ImageVector.size[0]
        block_per_row = int(pixels_count_row / block_size)
        add_to_pixel_on_row_mutliplier = 0

        def log_block_creation(block, pixel_on_row_index, pixel_on_col_index, pixel_on_block_index):
            print(
                f'block {block} | pixel_on_row_index {pixel_on_row_index} | pixel_on_col_index {pixel_on_col_index} | pixel_on_block_index {pixel_on_block_index}'
            )

        def get_col_index(block, block_size, col, pixels_count_row):
            return ((block*block_size) + col) % pixels_count_row

        def get_row_index(row, pixels_count_row, add_to_pixel_on_row_mutliplier):
            return pixels_count_row * (row + add_to_pixel_on_row_mutliplier)

        for b in range(block_count):
            for row in range(block_size):
                for col in range(block_size):
                    pixel_on_row_index = get_row_index(row, pixels_count_row, add_to_pixel_on_row_mutliplier)
                    pixel_on_col_index = get_col_index(b, block_size, col, pixels_count_row)
                    pixel_on_block_index = pixel_on_col_index + pixel_on_row_index

                    group.append(self.pixels[pixel_on_block_index])

            groups.append(group)
            group = []

            if (b + 1) % block_per_row == 0:
                add_to_pixel_on_row_mutliplier += block_size

        block_averages = [average_of_tuple_lists(block) for block in groups]

        add_to_pixel_on_row_mutliplier = 0
        new_image = [None for _ in range(pixels_rgb_count)]

        for b in range(block_count):
            for row in range(block_size):
                for col in range(block_size):
                    pixel_on_row_index = get_row_index(row, pixels_count_row, add_to_pixel_on_row_mutliplier)
                    pixel_on_col_index = get_col_index(b, block_size, col, pixels_count_row)
                    pixel_on_block_index = pixel_on_col_index + pixel_on_row_index
                    new_image[pixel_on_block_index] = block_averages[b]

            if (b + 1) % block_per_row == 0:
                add_to_pixel_on_row_mutliplier += block_size

        return ImageVector(new_image)

    def gray_scaled_image(self, light=1):
        return ImageVector(averaged_tuple_lists(self.pixels)).scale(light)

    def add(self, img2):
        '''
        performs vector addition for images by adding the respective red, green, and blue
        values for each pixel
        '''
        return ImageVector(
            [
                (r1+r2, g1+g2, b1+b2)
                for ((r1, g1, b1), (r2, g2, b2))
                in zip(self.pixels, img2.pixels)
            ]
        )

    def scale(self, scalar):
        '''
        Performs scalar multiplication by multiplying every red, green, and blue
        value for every pixel by the given scalar
        '''
        return ImageVector(
            [(scalar*r, scalar*g, scalar*b) for (r, g, b) in self.pixels]
        )

    @ classmethod
    def zero(cls):
        '''
        The zero image has zero red, green, or blue content at any pixel.
        '''
        total_pixels = cls.size[0] * cls.size[1]
        return ImageVector([(0, 0, 0) for _ in range(0, total_pixels)])

    def _repr_png_(self):  # 8
        '''
        Jupyter notebooks can display PIL images inline, 
        as long as we pass the implementation of the function 
        _repr_png_ from the underlying image.
        '''
        return self.image()._repr_png_()

    def get_pixels_in_picture(self):
        return len([pixel_rgb for pixel_rgb in self.pixels])
