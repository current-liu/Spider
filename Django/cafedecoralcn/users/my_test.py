#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/9/18 0018 上午 11:13

base Info
"""
import dao
# from users import service
__author__ = 'liuchao'
__version__ = '1.0'


def get_or_favorite():
    # id = request.GET.get("id")
    id = 6
    res = dao.get_all_id(id)
    o_r = res[0][1]
    if o_r is None:
        f = 0
        d = {"f": f}
        j = JsonResponse(d, safe=False)
        return j
    else:
        res_list = dao.get_or_favorite(o_r)
        length = res_list.__len__()
        fav_stat = {}
        for i in range(0, length):
            res = res_list[i]
            f = res[0]
            f_1 = f.replace("\n", "")
            f_2 = f_1.split("/")
            for i in range(0, f_2.__len__()):
                x = f_2[i]
                try:
                    n = fav_stat[x]
                    fav_stat[x] = n+1
                except Exception, e:
                    fav_stat[x] = 1

        j = JsonResponse(shop_list, safe=False)
        return j





if __name__ == '__main__':
    # service.get_dp_members()
    get_or_favorite()
