#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/11 0011 上午 11:23

base Info
"""

import sys
import traceback
from maxims import DBManager

reload(sys)
sys.setdefaultencoding("utf8")

__author__ = 'Administrator'
__version__ = '1.0'


def get_or_reviewNum(shop_id):
    sql = """SELECT COUNT(shopId) from reviews_orreview where shopId = %s"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_dp_reviewNum(shop_id):
    sql = """SELECT COUNT(shopId) from reviews_dpreview where shopId = %s"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_ta_reviewNum(shop_id):
    sql = """SELECT COUNT(shopId) from reviews_tareview where shopId = %s"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_mfw_reviewNum(shop_id):
    sql = """SELECT COUNT(shopId) from reviews_mfwreview where shopId = %s"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_all_id(shop_id):
    """没有的平台，id返回0"""
    sql = """SELECT id,(CASE WHEN o_r IS NOT NULL THEN o_r ELSE 0 END) o_r ,(CASE WHEN mfw IS NOT NULL THEN mfw ELSE 0 END) mfw,(CASE WHEN ta IS NOT NULL THEN ta ELSE 0 END) ta, (CASE WHEN dp IS NOT NULL THEN dp ELSE 0 END) dp
                      FROM view_shop_relation WHERE id = %s"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_or_review(shop_id):
    sql = """select content from reviews_orreview where memberId IN  (SELECT DISTINCT memberId from reviews_orreview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_mfw_review(shop_id):
    sql = """select content from reviews_mfwreview where memberId IN  (SELECT DISTINCT memberId from reviews_mfwreview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_dp_review(shop_id):
    sql = """select content from reviews_dpreview where memberId IN  (SELECT DISTINCT memberId from reviews_dpreview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_ta_review(shop_id):
    sql = """select content from reviews_tareview where memberId IN  (SELECT DISTINCT memberId from reviews_tareview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_or_month_review(shop_id):
    sql = """select LEFT(time,7) from reviews_orreview where memberId IN  (SELECT DISTINCT memberId from reviews_orreview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_mfw_month_review(shop_id):
    sql = """select LEFT(time,7) from reviews_mfwreview where memberId IN  (SELECT DISTINCT memberId from reviews_mfwreview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_dp_month_review(shop_id):
    sql = """select LEFT(time,7) from reviews_dpreview where memberId IN  (SELECT DISTINCT memberId from reviews_dpreview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_ta_month_review(shop_id):
    sql = """select LEFT(time,7) from reviews_tareview where memberId IN  (SELECT DISTINCT memberId from reviews_tareview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_or_review_info(shop_id):
    sql = """select memberName,memberId,title,content,time,taste,environment,services,health,pic from view_orreview where memberId IN  (SELECT DISTINCT memberId from reviews_orreview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_dp_review_info(shop_id):
    sql = """select memberId,name,content,time,taste,environment,likes,reply,pic from view_dpreview where memberId IN (SELECT DISTINCT memberId from reviews_dpreview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_ta_review_info(shop_id):
    sql = """select memberId,memberName,title,content,time,star,pic from view_tareview where memberId IN (SELECT DISTINCT memberId from reviews_tareview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_mfw_review_info(shop_id):
    sql = """select memberId,name,content,time,star,likes,pic from view_mfwreview where memberId IN (SELECT DISTINCT memberId from reviews_mfwreview where shopId = %s)"""
    results = DBManager.queryAll(sql, shop_id)
    return results

