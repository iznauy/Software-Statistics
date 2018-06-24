#-*- coding:utf-8 -*-
import math
from scipy.stats import t 

class Solution():
    def solve(self):
        n1, n2 = 22.0, 22.0
        avg1, avg2 = 52.1, 27.1
        std1, std2 = 45.1, 26.4
        alpha = 0.05
        
        sw = math.sqrt(((n1 - 1) * (std1 ** 2) + (n2 - 1) * (std2 ** 2))/(n1 + n2 - 2))
        t_val = (avg1 - avg2) / (math.sqrt(1.0 / n1 + 1.0 / n2) * sw)
        threshold = t.isf(alpha / 2, n1 + n2 - 2)
        return [n1 - 1, round(t_val, 2), False if abs(t_val) >= threshold else True]