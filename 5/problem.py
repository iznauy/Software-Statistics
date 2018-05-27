#-*- coding:utf-8 -*-
import os

def bin_digits(n, bits):
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)


class Solution():

    def solve(self):
    
        os.system('pip install fp-growth')
        import fp_growth as fg
    
        data_set = []
        with open('A.csv', 'r') as f:
            lines = f.readlines()
            for line in lines:
                data_set.append(line.strip().split(","))
        
        freq_items = fg.find_frequent_itemsets(data_set, len(data_set) * 0.45, include_support=True)  
        
        L = []
        for (items, count) in freq_items:
            s_items = set(items)
            if ('republican0' in s_items or 'democrat0' in s_items) and len(s_items) > 1:
                L.append((items, count))
        
        rules = []

        for (items, count) in L:
            items.sort()
            rule_lens = len(items) - 1

            for i in range(1, 2 ** rule_lens):
                left = {items[0]}
                right = set()
                bin_form = bin_digits(i, rule_lens)
                for j in range(rule_lens):
                    if bin_form[j] == '1':
                        right.add(items[j + 1])
                    else:
                        left.add(items[j + 1])

                left_count = 0
                for entry in data_set:
                    if left.issubset(entry):
                        left_count += 1
                if count * 1.0 / left_count >= 0.9:
                    rules.append([list(left), list(right)])
                    
        return rules