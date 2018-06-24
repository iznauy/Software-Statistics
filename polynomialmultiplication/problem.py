#-*- coding:utf-8 -*-
import numpy as np

class Solution():
    def solve(self, A):
        f = np.array([2.0, 0.0, -1.0, 1.0])
        g = np.array(A)
        return np.poly1d(f) * np.poly1d(g)