#! /usr/bin/env python

import sys
import numpy as np


class Random:
    """A random number generator class"""
    m_v = 4101842887655102017
    m_w = 1
    m_u = 1
    
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    def int64(self):
        self.m_u = np.uint64(self.m_u * 2862933555777941757) + np.uint64(7046029254386353087)
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

if __name__ == "__main__":
    if '-h' in sys.argv or '--help' in sys.argv:
        print("Usage: {} [-seed number -file filename]".format(sys.argv[0]))
        print()
        sys.exit(1)

   
    seed = 5555
    
    fname = 'random_numbers'

    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
        
    if '-file' in sys.argv:
        p = sys.argv.index('-file')
        fname = sys.argv[p+1]
        
    if '-f' in sys.argv:
        p = sys.argv.index('-f')
        fname = sys.argv[p+1]
        
        
    np.random.seed(seed)
    random = Random(seed)

    # data
    N = 10000
    x = np.random.rand(N)
    myx = []
    for i in range(0,N):
        myx.append(random.rand())
    
    # using numpy to save to text
    np.savetxt(fname, myx)
    


