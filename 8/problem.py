#-*- coding:utf-8 -*-
from sklearn.cluster import KMeans

class Solution():
    def solve(self, X):
        algorithm = KMeans(n_clusters=12).fit(X)
        return algorithm.labels_
        