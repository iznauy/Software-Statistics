#-*- coding:utf-8 -*-

import pandas as pd
from pandas import DataFrame

movie_file_name = 'movies.csv'
rating_file_name = 'ratings.csv'

class Solution():
    def solve(self):
        movies = DataFrame(pd.read_csv(movie_file_name))
        movie1 = movies[movies.movieId == 1]
        
        movieNameOfMovieId1 = movie1.title[0]
        genresCounts = len(movie1.genres[0].split('|'))
        ratings = DataFrame(pd.read_csv(rating_file_name))
        
        movieIdOfTheMostRatedMovie = ratings.groupby('movieId').size().sort_values(ascending=False).index[0]
        movieNameOfTheMostRatedMovie = movies[movies.movieId == movieIdOfTheMostRatedMovie].title.values[0]
        
        return [movieNameOfMovieId1, genresCounts, movieNameOfTheMostRatedMovie]