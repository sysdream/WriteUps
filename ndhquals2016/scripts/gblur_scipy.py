from scipy import misc, ndimage

# http://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.ndimage.filters.gaussian_filter.html

if __name__ == '__main__':
    img = misc.imread('H_line_1.png')

    gblur = ndimage.gaussian_filter(img, sigma=2)

    misc.imsave('gblur_scipy.png', gblur)

