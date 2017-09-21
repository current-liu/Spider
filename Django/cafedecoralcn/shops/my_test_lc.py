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


def get_all_shop_appraise():
    res = dao_lc.get_all_shop_ids()
    shop_appraise_list = []
    for r in res:
        id = r[0]
        print id
        name = r[1]
        dp = r[2]
        o_r = r[3]
        mfw = r[4]
        ta = r[5]

        star_list = []
        if o_r != 0:
            star_or = float(dao_lc.get_shop_star_from_pla("or", o_r)[0][0])
            if star_or > 0:
                star_list.append(star_or)
        if mfw != 0:
            star_mfw = float(dao_lc.get_shop_star_from_pla("mfw", mfw)[0][0])
            if star_mfw > 0:
                star_list.append(star_mfw)
        if ta != 0:
            star_ta = float(dao_lc.get_shop_star_from_pla("ta", ta)[0][0])
            if star_ta > 0:
                star_list.append(star_ta)

        taste = -1
        environment = -1
        service = -1
        if dp != 0:
            dp_star_and_more = dao_lc.get_shop_star_and_more_from_dp(dp)[0]
            star_dp = float(dp_star_and_more[0])
            taste = dp_star_and_more[1]
            environment = dp_star_and_more[2]
            service = dp_star_and_more[3]
            if star_dp > 0:
                star_list.append(star_dp)

        num = star_list.__len__()
        star_total = 0
        if num == 0:
            star_avg = 0
        else:
            for i in range(0, num):
                star_total += star_list[i]
            star_avg = star_total / num
        shop_appraise = {"id": id, "name": name, "star": star_avg, "taste": taste, "envir": environment,
                         "service": service}

        shop_appraise_list.append(shop_appraise)

    pass


if __name__ == '__main__':
    get_all_shop_appraise()
