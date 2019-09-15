'''

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


from PIL import Image
import glob, os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def PIL2array(img):
    return np.array(img.getdata(),
                    np.uint8).reshape(img.size[1], img.size[0], 3)

#convert the pdf into an image
pil_img = convert_from_path('testRubric.pdf',output_folder='/Users/titusjohn/Documents/GitHub/tmac',fmt='jpg')
'''


import glob, os
import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img=mpimg.imread('testRubric.jpg')

imgplot = plt.imshow(img)
plt.show()
