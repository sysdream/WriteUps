from PIL import Image

CHALL_PATH = 'moleman.png'

# Extracting the char "H" form the 4 first lines
CHAR_BOX_LINE_1 = (1100, 10, 1250, 130)
CHAR_BOX_LINE_2 = (500, 210, 650, 330)
CHAR_BOX_LINE_3 = (680, 410, 830, 530)
CHAR_BOX_LINE_4 = (500, 610, 650, 730)

if __name__ == '__main__':
    img = Image.open(CHALL_PATH)

    # Crop the char "H" from the first line
    print "[i] Retrieving the first line"
    img1 = img.crop(CHAR_BOX_LINE_1)
    #img1.show()
    img1.save('H_line_1.png', 'PNG')

    # Crop the char "H" from the second line
    print "[i] Retrieving the second line"
    img2 = img.crop(CHAR_BOX_LINE_2)
    #img2.show()
    img2.save('H_line_2.png', 'PNG') 

    # Crop the char "H" from the third line
    print "[i] Retrieving the third line"
    img3 = img.crop(CHAR_BOX_LINE_3)
    #img3.show()
    img3.save('H_line_3.png', 'PNG')

    # Crop the char "H" from the fourth line
    print "[i] Retrieving the fourth line"
    img4 = img.crop(CHAR_BOX_LINE_4)
    #img4.show()
    img4.save('H_line_4.png', 'PNG')

