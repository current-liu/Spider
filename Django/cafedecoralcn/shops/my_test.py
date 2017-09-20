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


def get_shop_id_with_tel(target):
    """以target的作为样本，匹配结果对里，target的放第二个"""
    r_list = []
    for pla in ["dp", "mfw", "or", "ta"]:
        res = dao.get_shop_id_with_the_same_tel(target, pla)
        r_list.append({"pla": pla, "id_shop": res})

    return r_list


def update_shop_id_table_by_tel_fix(target):
    r_list = get_shop_id_with_tel(target)
    for i in range(0, r_list.__len__()):
        r = r_list[i]
        pla = r["pla"]
        if pla != "or":
            id_shop = r["id_shop"]
            dao.update_shop_id(target, pla, id_shop)


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



def get_shop_id_with_the_same_addr(target):
    """以openrice的作为样本，匹配结果对里地址中数字相同的，openeice的放第二个"""
    r_list = []
    for pla in ["dp", "mfw", "or", "ta"]:
        res = dao.get_shop_id_with_the_same_addr(target, pla)
        r_list.append({"pla": pla, "id_shop": res})

    return r_list


def update_shop_id_table_by_addr_fix(target):
    r_list = get_shop_id_with_the_same_addr(target)

    for i in range(0, r_list.__len__()):
        r = r_list[i]
        pla = r["pla"]
        if pla != target:
            id_shop = r["id_shop"]
            dao.update_shop_id(target, pla, id_shop)


def init_shop_id():
    target_list = ["dp", "mfw", "ta"]
    target = target_list[1]
    ids = dao.select_shop_id_unmatched(target)
    shop_ids = []
    for i in ids:
        shop_id = (i[0],)
        shop_ids.append(shop_id)
    dao.init_shop_id_by_pla(target, shop_ids)
    # dao.init_shop_id_by_pla(target, -10)


def get_shop_info(platform):
    """获取店铺的基本信息"""
    res_or = dao.selete_shops_info(platform)
    shop_info = []
    for res in res_or:
        shop_id = res[0]
        addr = res[1]
        name = res[2]
        tel = res[3]
        if platform == "dp":
            addr = addr.split(" ")[0]

        addr_fix = 0
        try:
            addr_str = re.sub(r"\D", "", addr)
            addr_fix = addr_str
        except BaseException, e:
            print e

        tel_fix = 0
        try:
            tel_str = re.sub(r"\D", "", tel)[-8:]
            if tel_str.__len__() != 8:
                tel_str = "0"
            tel_fix = int(tel_str)
        except BaseException, e:
            print e

        shop_info.append((name, addr, addr_fix, tel, tel_fix, shop_id, platform))
    return shop_info


def update_shop_relation_info():
    """更新表shop_relation"""
    shop_info_list = []
    for pla in ["dp", "mfw", "or", "ta"]:
        shop_info = get_shop_info(pla)
        shop_info_list.append({"pla": pla, "shop_info": shop_info})

    for i in range(0, shop_info_list.__len__()):
        l_ = shop_info_list[i]
        pla_ = l_["pla"]
        shop_info_ = l_["shop_info"]
        dao.insert_shop_relation(shop_info_)


def remove_repeat_by_tel():
    """先将repeat_mark改为0都"""
    dao.update_repeat_mark_to_0()
    """从shop_relation表中按tel去重,repeat打标记1"""
    id_tel = dao.get_shopid_tel_from_shop_relation()
    length = id_tel.__len__()
    for i in range(0, length):
        # 从屁股上取一个，跟前面的比较
        index = length-1-i
        shop_id = id_tel[index][0]
        shop_tel = id_tel[index][1]
        shop_pla = id_tel[index][2]

        for n in range(0, index):
            if shop_tel == id_tel[n][1]:
                dao.update_shop_relation_repeat(shop_id, 1)
                distinct_shop_id = id_tel[n][0]
                dao.update_shop_relation_relative_pla(distinct_shop_id, shop_pla, shop_id)
                continue
                
                
def remove_repeat_by_name():
    """先将名字为'大家乐’ ‘大家乐快餐的repeat_mark改为10’"""
    dao.up_repeat_mark_to_10()
    """从shop_relation表中按name去重,repeat打标记2"""
    """按shopName group by 之后 ，人工看，名字一样的也不一定一样"""
    
    
def remove_repeat_by_addr():
    """从shop_relation表中按addr去重, repeat打标记3;匹配成功后，人工审查"""

    id_addr_10 = dao.get_shopid_addr_from_shop_relation(10)
    id_addr_0 = dao.get_shopid_addr_from_shop_relation(0)
    length_addr_10 = id_addr_10.__len__()
    length_addr_0 = id_addr_0.__len__()

    for i in range(0, length_addr_10):

        index = i
        shop_id = id_addr_10[index][0]
        shop_addr = id_addr_10[index][1]
        shop_pla = id_addr_10[index][2]

        shop_addr_fix = shop_addr[-5:].replace("\n", "")
        shop_addr_fix_1 = shop_addr[-8:-3].replace("\n", "")
        for n in range(0, length_addr_0):
            to_match_addr = id_addr_0[n][1]

            if (shop_addr_fix in to_match_addr ) or (shop_addr_fix_1 in to_match_addr):
                # dao.update_shop_relation_repeat(shop_id, 3)
                distinct_shop_id = id_addr_0[n][0]
                distinct_shop_pla = id_addr_0[n][2]
                pass
                # dao.update_shop_relation_relative_pla(distinct_shop_id, shop_pla, shop_id)
                continue






if __name__ == '__main__':
    # update_shops_tel()
    # get_shop_id_with_tel()

    # update_shop_id_table()
    # update_shops_tel_addr_fix()
    # dao.selete_shop_all()
    # dao.get_or_location()
    get_or_reviewNum()
    # update_shops_tel_addr_fix()

    # init_shop_id()

    target_list = ["dp", "mfw", "or", "ta"]

    # target = target_list[1]
    # update_shop_id_table_by_tel_fix(target)
    # update_shop_id_table_by_addr_fix(target)
    # update_shop_relation_info()
    # remove_repeat_by_tel()
    # remove_repeat_by_name()
    remove_repeat_by_addr()

