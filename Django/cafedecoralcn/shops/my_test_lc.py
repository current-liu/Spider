#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/9/16 0016 上午 10:55

base Info
"""
from shops import dao_lc
import re

__author__ = 'liuchao'
__version__ = '1.0'


def get_all_shop_info():
    res = dao_lc.get_all_shop_ids()
    id_list = []
    name_list = []
    dp_list = []
    o_r_list = []
    mfw_list = []
    ta_list = []
    
    for r in res:
        id = r[0]
        name = r[1]
        dp = r[2]
        o_r = r[3]
        mfw = r[4]
        ta = r[5]

        id_list.append(id)
        name_list.append(name)
        dp_list.append((dp,))
        o_r_list.append(o_r)
        mfw_list.append(mfw)
        ta_list.append(ta)

    star_list = dao_lc.get_shop_info_from_pla("dp", dp_list)
    pass



if __name__ == '__main__':
    get_all_shop_info()


