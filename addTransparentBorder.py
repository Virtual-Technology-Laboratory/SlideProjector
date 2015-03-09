from __future__ import print_function

# Author: Roger Lew (rogerlew@vandals.uidaho.edu || rogerlew@gmail.com)
# Date: 1/6/2015
# License: Public Domain

import sys

import numpy as np
import scipy.misc 

def addTransparentBorder(src_fname, dst_fname):

    rgba = scipy.misc.imread(src_fname)

    w, h, n = rgba.shape

    if n == 3:
        alpha = np.ones((w,h,1), dtype=np.uint8) * 255
        rgba = np.concatenate((rgba, alpha), axis=2)

    rgba[0,:,3] = 0
    rgba[w-1,:,3] = 0
    rgba[:,0,3] = 0
    rgba[:,h-1,3] = 0

    scipy.misc.imsave(dst_fname, rgba)
    
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Expecting src and dst as arguments")
        sys.exit()
    
    src_fname = sys.argv[1]
    dst_fname = sys.argv[2]
    addTransparentBorder(src_fname, dst_fname)
