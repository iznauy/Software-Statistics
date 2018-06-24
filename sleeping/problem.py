#-*- coding:utf-8 -*-
import math
from scipy.stats import norm

class Solution:
    def solve(self):
        avg, s2, n = 8.5, 25.0, 3600.0
        alpha = 0.05
        
        z_value = norm.isf(alpha / 2)
        
        return [avg - math.sqrt(s2 / n) * z_value, avg + math.sqrt(s2 / n) * z_value]