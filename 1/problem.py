#-*- coding:utf-8 -*-

import requests
import zipfile
import pandas as pd
from pandas import DataFrame
from pandas import Series

url = 'https://www.imf.org/external/pubs/ft/wp/2008/Data/wp08266.zip'
file_name = 'wp08266.zip'
dataset_name = 'Financial Reform Dataset Dec 2008.dta'
iter_size = 100

class Solution():
    def solve(self):
        response = requests.get(url) # 保存远端文件到本地
        with open(file_name, 'wb') as f:
            for clip in response.iter_content(iter_size):
                f.write(clip)

        zipper = zipfile.ZipFile(file_name) # 解压数据文件
        zipper.extractall()
        zipper.close()

        df = DataFrame(pd.read_stata(dataset_name))

        countries_series = df.groupby('country').size()

        countries = countries_series.size

        countries_series = countries_series.sort_values()

        if countries % 2 == 1:
            medianNumber = countries_series[(countries - 1) / 2]
        else:
            medianNumber = (countries_series[countries / 2 - 1] + countries_series[countries / 2]) / 2

        return [countries, medianNumber]