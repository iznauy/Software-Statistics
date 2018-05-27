#-*- coding:utf-8 -*-
import numpy as np
from random import randint

class Solution():
    def solve(self, R, Y, ratings, k):
        R = np.array(R).astype(np.float) # may useless
        Y = np.array(Y).astype(np.float)
        n_m, n_u = Y.shape

        ratings = np.array(ratings).astype(np.float)

        # calc adjusted cosine
        Y[Y == 0] = np.nan
        user_means = np.nanmean(Y, axis=0)
        
        normed_Y = Y - user_means
        var = np.sqrt(np.nansum(normed_Y * normed_Y, axis=0))

        ratings[ratings == 0] = np.nan
        current_user_mean = np.nanmean(ratings)
        normed_current_user = ratings - current_user_mean
        current_var = np.sqrt(np.nansum(normed_current_user * normed_current_user))

        similarities = np.nansum(normed_Y * normed_current_user, axis=0) / (var * current_var)
        
        similarities_orders = np.argsort(similarities)[::-1]
        recommendations = []

        for i in range(n_u):
            user = similarities_orders[i]
            for j in range(n_m):
                if Y[j][user] >= 4 and np.isnan(ratings[j]): # you can choose 4 or 5 according to your preference
                    recommendations.append(j)
                    ratings[j] = 0
                    if len(recommendations) == k:
                        return set(recommendations)
                        
        # don't get enough movies, so we need to generate some movies randomly
        while len(recommendations) < k:
            rand = randint(0, n_m - 1)
            if np.isnan(ratings[rand]):
                recommendations.append(rand)
                ratings[rand] = 0
                
        return set(recommendations)
                  
