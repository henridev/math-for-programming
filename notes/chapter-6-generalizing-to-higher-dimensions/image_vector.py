from vector import Vector
from PIL import Image

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
        This method returns the underlying PIL image, reconstructed from the pixels stored as an attribute on the class.
        The values must be converted to integers to create a displayable image.
        '''
        img = Image.new('RGB', ImageVector.size)  # 4
        img.putdata([(int(r), int(g), int(b)) for (r, g, b) in self.pixels])
        return img

    def add(self, img2):
        '''
        performs vector addition for images by adding the respective red, green, and blue values for each pixel
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
        Performs scalar multiplication by multiplying every red, green, and blue value for every pixel by the given scalar
        '''
        return ImageVector(
            [(scalar*r, scalar*g, scalar*b) for (r, g, b) in self.pixels]
        )

    @classmethod
    def zero(cls):
        '''
        The zero image has zero red, green, or blue content at any pixel.
        '''
        total_pixels = cls.size[0] * cls.size[1]
        return ImageVector([(0, 0, 0) for _ in range(0, total_pixels)])

    def _repr_png_(self):  # 8
        '''
        Jupyter notebooks can display PIL images inline, as long as we pass the implementation of the function _repr_png_ from the underlying image.
        '''
        return self.image()._repr_png_()
