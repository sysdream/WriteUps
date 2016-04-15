
from PIL import Image, ImageFilter

if __name__ == '__main__':
    img = Image.open('H_line_1.png')

    img= img.filter(ImageFilter.GaussianBlur(radius=5))

    img.save('gblur_pil.png', 'PNG')

