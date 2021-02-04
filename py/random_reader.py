#! /usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    if '-h' in sys.argv or '--help' in sys.argv:
        print("Usage: {} [-file filename]".format(sys.argv[0]))
        print()
        sys.exit(1)
        
    fname = None 
    
    if '-file' in sys.argv:
        p = sys.argv.index('-file')
        fname = sys.argv[p+1]
        
    if '-f' in sys.argv:
        p = sys.argv.index('-f')
        fname = sys.argv[p+1]
        
    if fname is None:
        
        print('Warning! No input file provided. Please specify an input file.')
        print("Usage: {} [-file filename]".format(sys.argv[0]))
        print()
        sys.exit(1)
        

    #reading in the data
    myx = np.loadtxt(fname)
    
    # the histogram of the data
    n, bins, patches = plt.hist(myx, 50, density=True, facecolor='g', alpha=0.75)

    plt.xlabel('x')
    plt.ylabel('Probability')
    plt.title('Uniform random number')
    plt.grid(True)
    plt.show()