from PIL import Image, ImageFont, ImageChops, ImageDraw, ImageFilter
import cv2 
import numpy as np
import glob

# When creating an image, we use this size and this text position
WIDTH = 80
HEIGHT = 80
TEXT_POS = (10,10)

FOREGROUND = (255, 255, 255)
BG_COLOR = "#000000"
BACKGROUND = (0, 0, 0)

TEXT_SIZE_MAX = 50
TEXT_SIZE = 0

# Font directory to test
FONT_DIR = "/usr/share/fonts/truetype/freefont"

# Retrieving the chall file and extracting a char within in order to find the font
CHALL_PATH = 'moleman.png'
CHAR_BOX = (500, 10, 650, 150)

# Char used to find the font and the text size used
TEST_CHAR = "Z"

def create_image(text, font_path, text_size):
    '''
    Function used to create an image :
        - text = the text to add to this image
        - font_path = the font used
        - text_size = text size
    '''
    font = ImageFont.truetype(font_path, text_size)

    im = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(im)

    draw.text(TEXT_POS, text, font=font, fill=FOREGROUND)

    del draw

    #im.show()

    return im

def test_font(init_char, template):
    '''
    Function to test a font and a text size
        - init_char = A char from the challenge
        - template = our template to test

    For more informations see : http://docs.opencv.org/3.1.0/d4/dc6/tutorial_py_template_matching.html
    '''
    #init_char.show()
    #template.show()

    # Converting a PIL image to a cv2 image
    init_char2 = cv2.cvtColor(np.array(init_char), cv2.COLOR_RGB2BGR)
    template2 = cv2.cvtColor(np.array(template), cv2.COLOR_RGB2BGR)

    c,w,h = template2.shape[::-1]

    # All the 6 methods for comparison in a list
    # I wanted to be sure to find our template
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    #methods = ['cv2.TM_CCOEFF_NORMED']

    # Using comparison methods (matchTemplate) to find our template in the chall image
    for meth in methods:
        init_char_temp = init_char2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(init_char_temp,template2,method)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        box = (top_left[0], top_left[1], top_left[0]+w, top_left[1]+h)
        temp = init_char.crop(box)

        '''
        temp.show()
        template.show()
        ImageChops.difference(temp, template).show()
        '''

        pixels0 = temp.load()
        pixels1 = template.load()

        # The matchTemplate function do not test an exact image, it can be more or less the same.
        # So we have to test if the template is really where matchTemplate say.
        is_equal = True
        for i in range(w):
            for j in range(h):
                if pixels0[i,j] != pixels1[i,j] :
                    is_equal = False
                    break

        '''
        print is_equal
        print "#################"
        '''

        # If it's equal, we return True
        if is_equal:
            return True

    return False

def find_font(init_char):
    ''' 
    Function to test different fonts and sizes.
    '''

    for font_path in glob.glob('%s/*.ttf' % FONT_DIR): 
        for i in range(TEXT_SIZE_MAX):
            template = create_image(TEST_CHAR, font_path, i)    
            #template.show()

            if test_font(init_char, template):
                print "Font : %s; Text size : %d" % (font_path, i) 
                break

if __name__ == '__main__':
    # Crop a char not blurred:
    print "[i] Retrieving a char not blurred"
    init_char = Image.open(CHALL_PATH)
    init_char = init_char.crop(CHAR_BOX)
    #init_char.show()

    print "[i] Retrieving the font and size"
    find_font(init_char)

