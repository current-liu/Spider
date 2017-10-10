#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/9/16 0016 上午 10:55

base Info
"""
from shops import dao
import re

__author__ = 'liuchao'
__version__ = '1.0'


def get_shop_tel_fix(platform):
    res_or = dao.selete_shops_id_tel(platform)
    shop_id_tel = []
    for res in res_or:
        shop_id = res[0]
        tel = res[1]
        # tel = "123456789"
        tel_fix = 0
        try:
            tel_str = re.sub(r"\D", "", tel)[-8:]
            if tel_str.__len__() != 8:
                tel_str = "0"
            tel_fix = int(tel_str)
        except BaseException, e:
            print e

        shop_id_tel.append((shop_id, tel_fix))
    return shop_id_tel


def update_shops_tel():
    shop_id_tel_list = []
    for pla in ["dp", "mfw", "or", "ta"]:
        shop_id_tel = get_shop_tel_fix(pla)
        shop_id_tel_list.append({"pla": pla, "shop_id_tel": shop_id_tel})

    for i in range(0, shop_id_tel_list.__len__()):
        l_ = shop_id_tel_list[i]
        pla_ = l_["pla"]
        shop_id_tel_ = l_["shop_id_tel"]
        dao.insert_x_shops_tel(pla_, shop_id_tel_)


def get_shop_id_with_tel():
    """以openrice的作为样本，匹配结果对里，openeice的放第一个"""
    r_list = []
    for pla in ["dp", "mfw", "or", "ta"]:
        res = dao.get_shop_id_with_the_same_tel(pla)
        r_list.append({"pla": pla, "id_shop": res})

    return r_list


def update_shop_id_table():
    r_list = get_shop_id_with_tel()
    for i in range(0, r_list.__len__()):
        r = r_list[i]
        pla = r["pla"]
        if pla != "or":
            id_shop = r["id_shop"]
            dao.update_shop_id(pla, id_shop)
            
            
def get_shop_addr_fix(platform):
    res_or = dao.selete_shops_id_addr(platform)
    shop_id_addr = []
    for res in res_or:
        shop_id = res[0]
        addr = res[1]

        if platform == "dp":
            addr = addr.split(" ")[0]

        addr_fix = 0

        try:
            addr_str = re.sub(r"\D", "", addr)
            addr_fix = addr_str
        except BaseException, e:
            print e

        shop_id_addr.append((addr_fix, shop_id))
    return shop_id_addr
            
            
def update_shops_tel_addr_fix():
    shop_id_addr_list = []
    for pla in ["dp", "mfw", "or", "ta"]:
        shop_id_addr = get_shop_addr_fix(pla)
        shop_id_addr_list.append({"pla": pla, "shop_id_addr": shop_id_addr})

    for i in range(0, shop_id_addr_list.__len__()):
        l_ = shop_id_addr_list[i]
        pla_ = l_["pla"]
        shop_id_addr_ = l_["shop_id_addr"]
        dao.insert_x_shops_addr(pla_, shop_id_addr_)
            
def get_or_reviewNum():
    res = dao.get_or_reviewNum()
    num = res[0][0]
    d = {"num":num}

    pass


if __name__ == '__main__':
    # update_shops_tel()
    # get_shop_id_with_tel()
    # update_shop_id_table()
    # update_shops_tel_addr_fix()
    # dao.selete_shop_all()
    # dao.get_or_location()
    get_or_reviewNum()
