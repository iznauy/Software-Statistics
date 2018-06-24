#-*- coding:utf-8 -*-
import math

class Solution():
    def solve(self, A):
        #call function prime
        return [x for x in A if self.prime(x)]

    #judge whether x is prime or not
    def prime(self, x):
        if x < 2:
            return False
        else:
            for i in range(2, int(math.ceil(math.sqrt(x)))):
                if x % i == 0:
                    return False
            return True
            