# coding=utf-8

import requests
from openpyxl import Workbook


def get_json(url, page, lang_name):
    data = {'first': 'true', 'pn': page, 'kd': lang_name}
    headers = {'Accept': 'application / json, text / javascript, * / *; q = 0.01',
               'Accept - Encoding': 'gzip, deflate, br',
               'Accept - Language': 'zh - CN, zh;q = 0.8',
               'Connection': 'keep - alive',
               'Content - Length': '23',
               'Content - Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
               'Cookie': ('JSESSIONID = ABAAABAAAIAACBI8D22AE9D4BA8E5A535A730F0B3C40EA0;'
                          'user_trace_token = 20170713084303 - 331afe7caecb45d3a6e0216a751cfda0;'
                          'PRE_UTM =;'
                          'PRE_HOST =;'
                          'PRE_SITE =;'
                          'PRE_LAND = https %3A%2F%2Fwww.lagou.com%2F;'
                          'LGUID = 20170713084304 - 3ae80e85 - 6764 - 11e7 - b5c7 - 525400f775ce;'
                          'index_location_city = %E5%85%A8%E5%9B%BD;'
                          '_gid = GA1.2.197789553.1499906560;'
                          '_ga = GA1.2.1018396097.1499906560;'
                          'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6 = 1499906560;'
                          'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6 = 1499906768;'
                          'LGSID = 20170713084304 - 3'
                          'ae80b96 - 6764 - 11e7 - b5c7 - 525400f775ce;'
                          'LGRID = 20170713084632 - b7686653 - 6764 - 11e7 - a80b - 5254005c3644;'
                          'TG - TRACK - CODE = index_search;'
                          'SEARCH_ID = beda8c8183d9482886ba2f8a0e7c73f7'),
               'Host': 'www.lagou.com',
               'Origin': 'https: // www.lagou.com',
               'Referer': 'https: // www.lagou.com / jobs / list_java?labelWords = & fromSearch = true & suginput =',
               'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 59.0.3071.115 Safari / 537.36',
               'X - Anit - Forge - Code': 0,
               'X - Anit - Forge - Token': None,
               'X - Requested - With': 'XMLHttpRequest'}

    json = requests.post(url, data, headers=headers).json()
    list_con = json['content']['positionResult']['result']
    info_list = []
    for i in list_con:
        info = []
        info.append(i['companyShortName'])
        # info.append(i['companyName'])
        info.append(i['salary'])
        info.append(i['city'])
        info.append(i['education'])
        info_list.append(info)
    return info_list


def main():
    lang_name = input('职位名：')
    page = 1
    url = 'http://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    info_result = []
    while page < 31:
        info = get_json(url, page, lang_name)
        info_result = info_result + info
        page += 1
    wb = Workbook()
    ws1 = wb.active
    ws1.title = lang_name
    for row in info_result:
        ws1.append(row)
    wb.save('职位信息.xlsx')


if __name__ == '__main__':
    main()
