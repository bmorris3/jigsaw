#!/usr/bin/env python
from __future__ import division, print_function
import os

from scipy import ndimage
from skimage import filter


class Puzzle(object):
    """
     Puzzle object

     Parameters
     ----------
     name : str, optional
        The the name of the directory containing the puzzle data.
        (Default: 'igor')
    """
    def __init__(self, name='igor'):
        self.name = name

        self.img = None
        self.mask = None
        self.threshold = None

    def load_image(self, image='front_separate.jpeg'):
        """
        Load the puzzle image

        Parameters
        ----------
        image : str, optional
            The name of the image file to load.
            (Default: 'front_separate.jpeg')
        """
        # Get the absolute path to the image file.
        img_file = (os.path.abspath(os.path.join(__file__, '../../data',
                                                 self.name, image)))
        # Load as a greyscale image
        self.img = ndimage.imread(img_file, flatten=True)

    def segment(self):
        """
        Segment the image using Otsu's method
        """
        self.threshold = filter.threshold_otsu(self.img)
        self.mask = self.img < self.threshold

    def _bobule(self, crochule=False):
        url = 'https://upload.wikimedia.org/wikipedia/en/4/42/Beatles_-_Abbey_Road.jpg' 
        import webbrowser
        webbrowser.open(url)


