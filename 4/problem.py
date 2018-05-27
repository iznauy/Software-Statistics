#-*- coding:utf-8 -*-
import re

class Solution():

    def solve(self):
        with open('A.txt') as f:
            text = f.readline()
        text = re.split(r"[\s\,\.\|\;\?\!\"]+", text)
        dct = dict()
        for i in text:
            dct[i] = dct.get(i, 0) + 1
        dic = sorted(dct.items(), key=lambda x: x[1], reverse=True)
        result = [5059]
        for i in range(10):
            result.append(dic[i][0])
        return result