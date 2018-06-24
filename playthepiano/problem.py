#-*- coding:utf-8 -*-
import math
from scipy.stats import t

class Solution():
    def solve(self):
        n, avg, std = 20.0, 4.6, 2.2
        claim = 5.0
        alpha = 0.05
        
        t_value = (avg - claim) / (std / math.sqrt(n))
        threshold = t.ppf(alpha , n - 1)
        
        return [n - 1, round(t_value, 2), True if t_value >= threshold else False]