#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/11 0011 上午 11:23

base Info
"""

import sys
from maxims import DBManager

reload(sys)
sys.setdefaultencoding("utf8")


__author__ = 'Administrator'
__version__ = '1.0'


def get_all_shop_ids():
    sql = """SELECT id,shopName,(CASE WHEN dp IS NOT NULL THEN dp ELSE 0 END) dp, (CASE WHEN o_r IS NOT NULL THEN o_r ELSE 0 END) o_r ,(CASE WHEN mfw IS NOT NULL THEN mfw ELSE 0 END) mfw,(CASE WHEN ta IS NOT NULL THEN ta ELSE 0 END) ta
              FROM view_shop_relation"""

    results = DBManager.queryAll(sql)
    return results


def get_shop_star_from_pla(pla, shop_id):
    sql = "SELECT star FROM shops_"+pla+"shop WHERE shopId = %s"

    results = DBManager.queryAll(sql, shop_id)
    return results


def get_shop_star_and_more_from_dp(shop_id):
    sql = """SELECT star,taste,environment,service FROM shops_dpshop WHERE shopId = %s"""

    results = DBManager.queryAll(sql, shop_id)
    return results
