# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2017-11-01 11:43:36
@Last Modified by:   lamborghini1993
@Last Modified time: 2017-11-01 11:43:36
"""

from budejie import text
from haowuya import wuduanzi
from meizitu import meizitu
from xiaoshuo import zww35
from movie import imdb250

def start():
    # obj = text.CText()
    # obj = wuduanzi.WuDuanZi()
    obj = imdb250.CIMDB250()
    obj.start()
    # obj.resource()


if __name__ == "__main__":
    start()
