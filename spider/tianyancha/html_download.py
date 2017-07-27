# coding=utf-8

import requests

import pip


# print(pip.pep425tags.get_supported())


def downloadPage(url):
    headers = {

        "Host": "www.tianyancha.com",
        "Connection": "keep - alive",
        "Upgrade - Insecure - Requests": "1",
        "User - Agent": "Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 59.0.3064.0 Safari / 537.36",
        "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8.",
        "Referer": "https: // www.tianyancha.com /",
        "Accept - Encoding": "gzip, deflate, br",
        "Accept - Language": "zh - CN, zh; q = 0.8",
        "Cookie": "ssuid=9316319424; jsid=SEM-SOUGOU-PP-SY-000099; _pk_ref.6835.e431=%5B%22%22%2C%22%22%2C1498800876%2C%22https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_qbhB5TwFUHrSv1MbFsrL0IBuo9pqAzDXqP8HWkNU_zKtm8N1pmsKgK%26query%3D%E5%87%AF%E7%9F%B3%E9%80%9A%22%5D; _pk_ref.1.e431=%5B%22%22%2C%22%22%2C1498800876%2C%22https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_qbhB5TwFUHrSv1MbFsrL0IBuo9pqAzDXqP8HWkNU_zKtm8N1pmsKgK%26query%3D%E5%87%AF%E7%9F%B3%E9%80%9A%22%5D; _pk_id.6835.e431=4506091f68130793.1497342237.10.1498800896.1498800876.; _pk_id.1.e431=66a8c05821cb6b5a.1497342237.10.1498800897.1498800876.; aliyungf_tc=AQAAABtL5x8slgYASLWPccdhvZ7ucdar; csrfToken=i0I-RfJAJAy8zqCM75VBslgO; TYCID=5957f6b072ba11e78a0105670635d82b; uccid=0adec762c1cc7ffe51c566d571c8694f; tyc-user-info=%257B%2522new%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTcwMDczMzE5NyIsImlhdCI6MTUwMTE1OTEzNiwiZXhwIjoxNTE2NzExMTM2fQ.0giWG2H6LGP_7xKwIaiLvFRezL5TM74hY1zjuUimNIvgg2dnDot8V-dLprd_oCRVVmABBdYrL1z6kusr6Z-K4Q%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215700733197%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTcwMDczMzE5NyIsImlhdCI6MTUwMTE1OTEzNiwiZXhwIjoxNTE2NzExMTM2fQ.0giWG2H6LGP_7xKwIaiLvFRezL5TM74hY1zjuUimNIvgg2dnDot8V-dLprd_oCRVVmABBdYrL1z6kusr6Z-K4Q; _csrf=gdG0D24jOPeOpmIYwXnI8g==; OA=MehB8UJnQba9MKzQq9kEaonMBa6mhI3BLYtnGiR9PelCw891fLMl4eP5cxP3lfUwdeBuWvVie1706nJqBFPtWKYohCUs/vd4HTDHnCatnsoFA2MRwM8k0SDv9mxBMkri; _csrf_bk=c94b7006415251e185344ea5bf420282; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1498800875,1501153035; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1501171190"

        }

    headers1 = {

        "Host": "www.tianyancha.com",
        "Connection": "keep - alive",
        "Upgrade - Insecure - Requests": "1",
        "User - Agent": "Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 59.0.3064.0 Safari / 537.36",
        "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8.",
        "Referer": "https: // www.tianyancha.com / search / t100?key = % E6 % 96 % B9 % E5 % BE % 97",
        "Accept - Encoding": "gzip, deflate, br",
        "Accept - Language": "zh - CN, zh; q = 0.8",
        "Cookie": "ssuid=9316319424; jsid=SEM-SOUGOU-PP-SY-000099; _pk_ref.6835.e431=%5B%22%22%2C%22%22%2C1498800876%2C%22https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_qbhB5TwFUHrSv1MbFsrL0IBuo9pqAzDXqP8HWkNU_zKtm8N1pmsKgK%26query%3D%E5%87%AF%E7%9F%B3%E9%80%9A%22%5D; _pk_ref.1.e431=%5B%22%22%2C%22%22%2C1498800876%2C%22https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_qbhB5TwFUHrSv1MbFsrL0IBuo9pqAzDXqP8HWkNU_zKtm8N1pmsKgK%26query%3D%E5%87%AF%E7%9F%B3%E9%80%9A%22%5D; _pk_id.6835.e431=4506091f68130793.1497342237.10.1498800896.1498800876.; _pk_id.1.e431=66a8c05821cb6b5a.1497342237.10.1498800897.1498800876.; aliyungf_tc=AQAAABtL5x8slgYASLWPccdhvZ7ucdar; csrfToken=i0I-RfJAJAy8zqCM75VBslgO; TYCID=5957f6b072ba11e78a0105670635d82b; uccid=0adec762c1cc7ffe51c566d571c8694f; tyc-user-info=%257B%2522new%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTcwMDczMzE5NyIsImlhdCI6MTUwMTE1OTEzNiwiZXhwIjoxNTE2NzExMTM2fQ.0giWG2H6LGP_7xKwIaiLvFRezL5TM74hY1zjuUimNIvgg2dnDot8V-dLprd_oCRVVmABBdYrL1z6kusr6Z-K4Q%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215700733197%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTcwMDczMzE5NyIsImlhdCI6MTUwMTE1OTEzNiwiZXhwIjoxNTE2NzExMTM2fQ.0giWG2H6LGP_7xKwIaiLvFRezL5TM74hY1zjuUimNIvgg2dnDot8V-dLprd_oCRVVmABBdYrL1z6kusr6Z-K4Q; _csrf=gdG0D24jOPeOpmIYwXnI8g==; OA=MehB8UJnQba9MKzQq9kEaonMBa6mhI3BLYtnGiR9PelCw891fLMl4eP5cxP3lfUwdeBuWvVie1706nJqBFPtWKYohCUs/vd4HTDHnCatnsoFA2MRwM8k0SDv9mxBMkri; _csrf_bk=c94b7006415251e185344ea5bf420282; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1498800875,1501153035; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1501171190"

    }




    # data = requests.get(url, headers=headers).content

    doc = """<!DOCTYPE html>
    <html>
    <head>
      <meta charset=utf-8>
      <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
      <title>天眼查-人人都在用企业信息调查工具_企业信息查询_公司查询_工商查询_信用查询平台</title>
      <meta http-equiv="pragma" content="no-cache">
      <meta http-equiv="cache-control" content="no-cache">
      <meta http-equiv="expires" content="0">

      <meta http-equiv="cache-control" content="no-transform"/>
      <meta http-equiv="cache-control" content="no-siteapp"/>
      <meta name="applicable-device" content="pc,mobile">
      <meta name="MobileOptimized" content="width"/>
      <meta name="HandheldFriendly" content="true"/>

      <meta name="description" itemprop="description" content="天眼查专注服务于个人与企业信息查询工具,为您提供企业查询,信息查询,工商查询,信用查询,公司查询等相关信息,帮您快速了解企业信息,企业工商信息,企业信用信息等企业经营和人员投资状况,查询更多企业信息就到天眼查官网！">
      <meta name="keywords" content="天眼查,企业查询,公司查询,工商查询,信用查询,企业信息查询,企业工商信息查询,企业信用查询,启信宝,企查查,红盾网">
      <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
            charset="UTF-8">

      <!--qq config-->
      <meta itemprop="name" content="天眼查-人人都在用企业信息调查工具_企业信息查询_公司查询_工商查询_信用查询平台">
      <meta itemprop="image" content="https://static.tianyancha.com/wap/images/weixinlogo.png">

      <meta name="fragment" content="!"/>

      <meta name="tyc-wx-type" content=""/>
      <meta name="tyc-wx-name" content=""/>
      <meta name="tyc-device" content="pc"/>

      <base href="/">
      <script>
        String.prototype.trim = function () {
          return this.replace(/(^\s*)|(\s*$)/g, "");
        }
        window.serverDomain = 'https://www.tianyancha.com'
        window.antirobotServer = 'https://antirobot.tianyancha.com'
        window.serverSuffix = '.tianyancha.com'
        window.cookieServerSuffix = '.tianyancha.com'
      </script>
      <script type="text/javascript" src="https://static.tianyancha.com/wap-require-js/public/js/require-6dc3b40987.config.js"></script>
      <script data-main="route/search"
              src="https://static.tianyancha.com/wap-require-js/public/js/lib/require.js"></script>

      <link rel="stylesheet" href="https://static.tianyancha.com/wap/css/font-awesome.min.css">
      <link rel="stylesheet" href="https://static.tianyancha.com/wap/css/bootstrap.css">

      <!-- build:css(./) resources/styles/app.css -->
      <!-- inject:css -->
      <link rel="stylesheet" href="https://static.tianyancha.com/wap-require-js/public/styles/main-19c79d2d66.css">
      <!-- endinject -->
      <!-- endbuild -->


      <style type="text/css">
        [ng\:cloak], [ng-cloak], [data-ng-cloak], [x-ng-cloak], .ng-cloak, .x-ng-cloak, .ng-hide {
          display: none !important;
        }

        ng\:form {
          display: block;
        }

        .ng-animate-start {
          clip: rect(0, auto, auto, 0);
          -ms-zoom: 1.0001;
        }

        .ng-animate-active {
          clip: rect(-1px, auto, auto, 0);
          -ms-zoom: 1;
        }
      </style>


      <!--[if lt IE 9]>
      <link rel="stylesheet" href="https://static.tianyancha.com/wap-require-js/resources/css/ie8-style.scss">
      <script src="https://static.tianyancha.com/wap/js/respond.js"></script>
      <![endif]-->

      <script>
        (function () {
          var method;
          var noop = function () {
          };
          var methods = [
            'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
            'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
            'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
            'timeline', 'timelineEnd', 'timeStamp', 'trace', 'warn'
          ];
          var length = methods.length;
          var console = (window.console = window.console || {});

          while (length--) {
            method = methods[length];

            // Only stub undefined methods.
            if (!console[method]) {
              console[method] = noop;
            }
          }
          CacheStoarge = function CacheStoarge() {
            var _bb = [];
            return {
              _tt: function (bbV, bbE, bbX) {
                bbX ? _bb.push(bbX) : _bb[bbV].push(bbE);
              },
              _ff: function (ii) {
                //console.log(_bb);
                return _bb[ii];
              }
            };
          };
          DOMImplementaiton = CacheStoarge();
        }());

      </script>

    </head>
    <body>








    <div class="company_input_v2" style="width: 100%; height: 74px;background:#14326e ;position: fixed; z-index: 1040;">
      <!--style="width: 100%; height: 74px;background:#29376B url('https://static.tianyancha.com/wap/images/bg-left-v1.jpg') repeat-x;position: fixed; z-index: 1040;"-->
      <!--id="company_input_web"-->
      <div class="container company_container">
        <div class="row" style="padding-left: 0;padding-right: 0; padding-top:0; padding-bottom: 0;">
          <div style="padding-left: 0;padding-right: 0;height: 74px; position: relative; " class="head-left">
            <a href="https://www.tianyancha.com" class="header_back_to_home " style="margin-top: 19px"></a>

            <div class="head-tab-outer" ng-hide="hideInput">
              <div class="head-tab-head c-white">
                <div class="in-block head-tab mr2 head-tab-c text-center point active"
                     onclick="header.changeSearchTab(event,'company')">
                  <div class="head-tab-top">查公司</div>
                </div>
                <div class="in-block head-tab mr2 head-tab-h text-center point "
                     tyc-event-click tyc-event-ch="DaoHang.HumanSearch.Tab"
                     onclick="header.changeSearchTab(event,'human')">
                  <div class="head-tab-top">查老板</div>
                </div>
                <div class="in-block head-tab head-tab-r text-center point "
                     tyc-event-click tyc-event-ch="DaoHang.RelationSearch.Tab"
                     onclick="header.jumpToPath(event)">
                  <div class="head-tab-top">查关系</div>
                </div>
              </div>
              <div class="head-tab-body head-tab-company">
                <div class="input-group search_group head-search-group-company"
                     style="display:">
                  <form onsubmit="return header.stopSubmit();" autocomplete="off">
                    <input id="live-search" type="search"
                           maxlength="50"
                           class="search_input form-control search_form input search-input-v1 f14 js-live-search"
                           placeholder='请输入企业名称、人名、产品名称或其它关键词'
                           value="方得"
                           style="border:none;"
                           click-selected="header.suggestToCompany"
                    >
                    <img alt="搜索" onclick="header.clearKey(event,'#live-search');" ng-show="key"
                         src="https://static.tianyancha.com/wap/images/close.png" class="clearNew"
                         width="20px"/>
                  </form>
                  <div class="input-group-addon input-search-v1"
                       tyc-event-click tyc-event-ch="DaoHang.CompanySearch.Search"
                       onclick="header.search(event)">
                  </div>
                </div>
                <div class="input-group search_group head-search-group-human"
                     style="display:none">
                  <form onsubmit="return header.stopHumanSubmit();" autocomplete="off">
                    <input type="search" class="search_input form-control search_form input search-input-v1 f14"
                           maxlength="50"
                           value=""
                           ng-model="humankey" ng-focus="pEvent('behaviour','searchFocus','');"
                           id="searchInputHuman"
                           placeholder='请输入人名、人名加地域/公司/产品关键词、用空格隔开'
                           style="border:none;"
                    >
                  </form>
                  <img onclick="header.clearKey(event,'#searchInputHuman');" ng-show="humankey"
                       src="https://static.tianyancha.com/wap/images/close.png" class="clearNew"
                       width="20px" alt="搜索"/>
                  <div class="input-group-addon input-search-v1" onclick="header.searchHuman(event)">
                  </div>
                </div>
              </div>
            </div>


          </div>
          <div
            style="padding-left: 0;padding-right: 0;position: relative; height: 74px;cursor:pointer;"
            class="head-right">
            <div class="right" style="padding-top: 22px">


              <div class="hover_title user_title" style="" ng-if="islogged" ng-init="userShow=false"
                   ng-mouseenter="userShow=true" ng-mouseleave="userShow=false"
                   onmouseleave="header.mouseHideById('#userShow')" onmouseenter="header.mouseShowById('#userShow')">
                <div class="in-block title1">
                  <div>
                    <a href="/usercenter/concern/1" href="/usercenter/concern/1" href-new-event event-name="导航-用户中心"
                       class="c-white">
                      <i class="fa fa-user"></i>
                      <span class="pr2">15700733197</span><i class="fa fa-caret-down" aria-hidden="true"></i>
                    </a>
                    <div class="list-group no-radius abs text-center collapse" id="userShow" ng-mouseenter="userShow=true"
                         ng-mouseleave="userShow=false">
                      <a class="list-group-item" href="/usercenter/concern/1">
                        关注企业
                      </a> <a class="list-group-item  " href="/usercenter/myorder">
                        我的订单
                      </a> <a class="list-group-item  " href="/usercenter/setpwd">
                        设置密码
                      </a>
                      <a class="list-group-item  " href="/usercenter/modifyInfo">
                        个人信息
                      </a>
                      <a class="list-group-item  " onclick="header.loginout(event)">
                        退出登录
                      </a>
                    </div>
                  </div>
                </div>
              </div>


              <div class="hover_title" style="">
                <span class="line1">|</span>
                <a class="title1" href="/vipintro" target="_blank"
                   tyc-event-click tyc-event-ch="DaoHang.VIP"
                > &nbsp;<i
                    class="fa fa-diamond"></i> 会员服务 </a>
                &nbsp;&nbsp;<span class="line1">|</span>
              </div>

              <div class="hover_title media_title"
                   ng-init="mediaHover=false" ng-mouseenter="mediaHover=true"
                   onmouseenter="header.mouseMediaShowById('#mediaHover')" ng-mouseleave="mediaHover=false"
                   onmouseleave="header.mouseMediaHideById('#mediaHover')" ng-class="{'media_title_h':mediaHover}">
                <div class="title1 in-block">
                  <div class="media_port pl6 pr6">
                    <img class="media_icon" src='https://static.tianyancha.com/wap/images/media_icon.png'
                         ng-src="{{!mediaHover?'https://static.tianyancha.com/wap/images/media_icon.png':'https://static.tianyancha.com/wap/images/media_icon_b.png'}}"
                         alt="合作通道"/>
                    <span class="pr7 no-mr">合作通道</span><i class="fa fa-caret-down" aria-hidden="true"></i>
                    <div class="list-group no-radius abs text-center collapse" id="mediaHover" ng-if="mediaHover"
                         ng-mouseenter="mediaHover=true" ng-mouseleave="mediaHover=false"
                         onmouseenter="header.mouseMediaShowById('#mediaHover')"
                         onmouseleave="header.mouseMediaHideById('#mediaHover')">
                      <a class="list-group-item" target="_blank" href="/appfortrial">
                        媒体通道
                      </a>
                      <a class="list-group-item" target="_blank" href="/business">
                        商务通道
                      </a>
                    </div>
                  </div>
                </div>
              </div>


              <div class="hover_title" style="">
                <span class="line1">|</span>
                <a class="title1" href="/invite" tyc-event-click tyc-event-ch="daohang.xdl" target="_blank" href-event event-name="导航-邀请有奖"> &nbsp;
                  <span class="yqyjIcon vertival-middle"></span>
                  <span class="in-block vertival-middle">邀请赢奖</span>
                </a>
              </div>


            </div>
          </div>

        </div>
      </div>
    </div>

    <div>



    <div ng-if="!errorMessagePage" style="width: 100%;" class="top_container_new b-c-gray">
      <div class="container company_container">
        <div class="row">
          <!-- main -->
          <div style="min-height: 840px;" class="col-9 search-2017-2 pr10 pl0">
            <!--搜索结果--人员-->





            <!--筛选项-->


    <div class="search-multi-filter b-c-white">

      <div class="search-multi-filter-head">
        <div class="position-abs">

          <a
            class="subTitle active"
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">企业</a>

          <a
            class="subTitle "
            href="https://www.tianyancha.com/search/t100?key=%E6%96%B9%E5%BE%97">司法风险</a>

          <a
            class="subTitle "
            href="https://www.tianyancha.com/search/t200?key=%E6%96%B9%E5%BE%97">经营风险</a>

          <a
            class="subTitle "
            href="https://www.tianyancha.com/search/t300?key=%E6%96%B9%E5%BE%97">经营状况</a>

          <a
            class="subTitle "
            href="https://www.tianyancha.com/search/t400?key=%E6%96%B9%E5%BE%97">知识产权</a>

        </div>
      </div>

      <!--其他搜索范围-->


      <!--企业搜索范围-->

      <div class="search-multi-filter-body search-scope">

        <div class="over-hide ml30 mr30 f14 pb15 new-c3" style="border-bottom: 1px dashed #E2E7E8;">
          <span class="search_filter_type_title f14 new-c2">搜索范围</span>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 filter-in-selected"
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
            全部
          </a>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 "
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97&searchType=company">
            企业
          </a>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 "
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97&searchType=human">
            法人/股东/高管
          </a>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 "
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97&searchType=brand">
            产品/商标
          </a>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 "
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97&searchType=similarAddr">
            联系方式
          </a>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 "
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97&searchType=scope">
            经营范围
          </a>

        </div>

        <div class="search_filter_box filter2017 b-c-white f14">
          <!--省份筛选new-->
          <div id="abbrCode" class="hidden"></div>
    <div id="checkProv" class="hidden"></div>

    <div class="ml30 mr30 pt15"
         tyc-event-click tyc-event-ch="CompanySearch.Filter.Shengfen"
    >
      <div>
        <span class="f14 new-c2 mr30 in-block vertical-top">省份地区</span>
        <div id="prov_box" class="in-block break-word over-hide baseContentBox" style="width: 670px;height:25px;">
          <div class="in-block mb10" style="width: 75px;">
            <a class="in-block pl10 pr10 c2 break-word new-list filter-in-selected filter-in-selected-border"
              href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
            >全部</a>
          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('ah')"
                  id="prov_ah"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">A</span>安徽</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <a class="in-block new-c3 pl8 pr8 break-word new-list point  "
                  href="https://bj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
            > <span class="">B</span> 北京</a>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <a class="in-block new-c3 pl8 pr8 break-word new-list point  "
                  href="https://cq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
            > <span class="">C</span> 重庆</a>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('fj')"
                  id="prov_fj"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">F</span>福建</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('gd')"
                  id="prov_gd"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">G</span>广东</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('gs')"
                  id="prov_gs"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">G</span>甘肃</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('gx')"
                  id="prov_gx"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">G</span>广西</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('gz')"
                  id="prov_gz"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">G</span>贵州</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('han')"
                  id="prov_han"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>海南</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('heb')"
                  id="prov_heb"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>河北</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('hen')"
                  id="prov_hen"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>河南</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('hlj')"
                  id="prov_hlj"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>黑龙江</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('hub')"
                  id="prov_hub"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>湖北</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('hun')"
                  id="prov_hun"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>湖南</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('jl')"
                  id="prov_jl"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">J</span>吉林</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('js')"
                  id="prov_js"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">J</span>江苏</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('jx')"
                  id="prov_jx"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">J</span>江西</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('ln')"
                  id="prov_ln"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">L</span>辽宁</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('nmg')"
                  id="prov_nmg"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">N</span>内蒙古</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('nx')"
                  id="prov_nx"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">N</span>宁夏</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('qh')"
                  id="prov_qh"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">Q</span>青海</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('sc')"
                  id="prov_sc"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">S</span>四川</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('sd')"
                  id="prov_sd"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">S</span>山东</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <a class="in-block new-c3 pl8 pr8 break-word new-list point  "
                  href="https://sh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
            > <span class="">S</span> 上海</a>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('snx')"
                  id="prov_snx"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">S</span>陕西</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('sx')"
                  id="prov_sx"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">S</span>山西</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <a class="in-block new-c3 pl8 pr8 break-word new-list point  "
                  href="https://tj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
            > <span class="">T</span> 天津</a>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('xj')"
                  id="prov_xj"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">X</span>新疆</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('xz')"
                  id="prov_xz"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">X</span>西藏</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('yn')"
                  id="prov_yn"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">Y</span>云南</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('zj')"
                  id="prov_zj"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">Z</span>浙江</span>

          </div>

        </div>
        <div id="baseShowMore" class="in-block vertical-top new-c3 point float-right">
          更多<i class="new-c9 ml5 fa fa-caret-down js-more-btn" ng-class="!hoverShow?'fa fa-caret-down':'fa fa-caret-up'"></i>
        </div>
      </div>

      <div id="filterBox">


          <div id="ah_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://ah.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hefei.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                合肥
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuhu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                芜湖
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://bangbu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                蚌埠
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huainan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                淮南
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://mas.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                马鞍山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huaibei.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                淮北
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tongling.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                铜陵
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://anqing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                安庆
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huangshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黄山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                滁州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fuyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阜阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://suzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宿州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://liuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                六安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://bozhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                亳州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chizhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                池州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xuancheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宣城
              </a>
            </div>

          </div>







          <div id="fj_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://fj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fzh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                福州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shamen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                厦门
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://putian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                莆田
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://sanming.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                三明
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://quanzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                泉州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhangzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                漳州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanping.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南平
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://longyan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                龙岩
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ningde.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宁德
              </a>
            </div>

          </div>



          <div id="gd_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://gd.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dongguan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                东莞
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhongshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                中山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guangzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                广州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shaoguan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                韶关
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shenzhen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                深圳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhuhai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                珠海
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shantou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                汕头
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://foshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                佛山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jiangmen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                江门
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhanjiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                湛江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://maoming.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                茂名
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhaoqing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                肇庆
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huizhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                惠州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://meizhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                梅州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shanwei.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                汕尾
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://heyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                河源
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yangjiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阳江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qingyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                清远
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chaozhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                潮州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jieyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                揭阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yunfu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                云浮
              </a>
            </div>

          </div>



          <div id="gs_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://gs.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jyg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                嘉峪关
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lanzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                兰州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jinchang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                金昌
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baiyin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                白银
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tianshui.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                天水
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuwei.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                武威
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhangye.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                张掖
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://pingliang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                平凉
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jiuquan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                酒泉
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qingyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                庆阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dingxi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                定西
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://longnan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                陇南
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lxhz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                临夏回族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://gnzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                甘南藏族自治州
              </a>
            </div>

          </div>



          <div id="gx_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://gx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanning.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南宁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://liuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                柳州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guilin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                桂林
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                梧州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://beihai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                北海
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fcg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                防城港
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qinzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                钦州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guigang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                贵港
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yul.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                玉林
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baise.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                百色
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hezhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                贺州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hechi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                河池
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://laibin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                来宾
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chongzuo.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                崇左
              </a>
            </div>

          </div>



          <div id="gz_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://gz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guiyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                贵阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lps.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                六盘水
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zunyi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                遵义
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://anshun.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                安顺
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://bijie.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                毕节
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tongren.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                铜仁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qxnbyz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黔西南布依族苗族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qdnz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黔东南州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qnbyz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黔南布依族苗族自治州
              </a>
            </div>

          </div>



          <div id="han_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://han.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://haikou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                海口
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://sanya.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                三亚
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hanzx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                省直辖县级行政区划
              </a>
            </div>

          </div>



          <div id="heb_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://heb.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://sjz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                石家庄
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tangshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                唐山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qhd.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                秦皇岛
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://handan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                邯郸
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xingtai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                邢台
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baoding.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                保定
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zjk.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                张家口
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chengde.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                承德
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://cangzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                沧州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://langfang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                廊坊
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hengshui.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                衡水
              </a>
            </div>

          </div>



          <div id="hen_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://hen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhengzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                郑州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://kaifeng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                开封
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://luoyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                洛阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://pds.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                平顶山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://anyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                安阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hebi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鹤壁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xinxiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                新乡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jiaozuo.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                焦作
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://puyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                濮阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xuchang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                许昌
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://luohe.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                漯河
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://smx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                三门峡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shangqiu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                商丘
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xinyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                信阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhoukou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                周口
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zmd.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                驻马店
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://henzx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                省直辖县级行政区划
              </a>
            </div>

          </div>



          <div id="hlj_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://hlj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://herb.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                哈尔滨
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qqhe.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                齐齐哈尔
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jixi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鸡西
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hegang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鹤岗
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://sys.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                双鸭山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://daqing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                大庆
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yich.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                伊春
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jms.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                佳木斯
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qth.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                七台河
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://mdj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                牡丹江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://heihe.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黑河
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://suihua.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                绥化
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dxaldq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                大兴安岭地区
              </a>
            </div>

          </div>



          <div id="hub_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://hub.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuhan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                武汉
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huangshi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黄石
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shiyan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                十堰
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yichang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宜昌
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xiangyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                襄阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ezhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鄂州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jingmen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                荆门
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xiaogan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                孝感
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jingzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                荆州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huanggang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黄冈
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xianning.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                咸宁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://suizhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                随州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://estjz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                恩施土家族苗族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hubzx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                省直辖县级行政区划
              </a>
            </div>

          </div>



          <div id="hun_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://hun.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhangsha.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                长沙
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                株洲
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xiangtan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                湘潭
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hengyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                衡阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shaoyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                邵阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yueyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                岳阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://changde.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                常德
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zjj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                张家界
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yiyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                益阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chenzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                郴州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yongzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                永州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huaihua.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                怀化
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://loudi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                娄底
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xxtjz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                湘西土家族苗族自治州
              </a>
            </div>

          </div>



          <div id="jl_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://jl.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhangchun.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                长春
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jilin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                吉林
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://siping.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                四平
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://liaoyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                辽源
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tonghua.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                通化
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baishan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                白山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://songyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                松原
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baicheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                白城
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ybcxz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                延边朝鲜族自治州
              </a>
            </div>

          </div>



          <div id="js_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://js.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanjing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南京
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuxi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                无锡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                徐州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://changzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                常州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://szh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                苏州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nantong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南通
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lyg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                连云港
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huaian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                淮安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yancheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                盐城
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yangzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                扬州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhenjiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                镇江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tzh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                泰州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://suqian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宿迁
              </a>
            </div>

          </div>



          <div id="jx_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://jx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanchang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南昌
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jdz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                景德镇
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://pingxiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                萍乡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jiujiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                九江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xinyu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                新余
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yingtan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鹰潭
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ganzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                赣州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                吉安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ych.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宜春
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                抚州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shangrao.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                上饶
              </a>
            </div>

          </div>



          <div id="ln_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://ln.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shenyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                沈阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dalian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                大连
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://anshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鞍山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fushun.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                抚顺
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://benxi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                本溪
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dandong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                丹东
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jinzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                锦州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yingkou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                营口
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fuxin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阜新
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://liaoyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                辽阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://panjin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                盘锦
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tieling.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                铁岭
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chaoyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                朝阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hld.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                葫芦岛
              </a>
            </div>

          </div>



          <div id="nmg_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://nmg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hhht.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                呼和浩特
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baotou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                包头
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuhai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                乌海
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chifeng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                赤峰
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tongliao.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                通辽
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://eeds.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鄂尔多斯
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hlbe.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                呼伦贝尔
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://byne.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                巴彦淖尔
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wlcb.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                乌兰察布
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xam.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                兴安盟
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xlglm.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                锡林郭勒盟
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://alsm.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阿拉善盟
              </a>
            </div>

          </div>



          <div id="nx_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://nx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yinchuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                银川
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://szs.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                石嘴山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuzhong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                吴忠
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                固原
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhongwei.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                中卫
              </a>
            </div>

          </div>



          <div id="qh_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://qh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xining.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                西宁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://haidong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                海东
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hbzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                海北藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hunzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黄南藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hnzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                海南藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://glzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                果洛藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yszz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                玉树藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hxmgz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                海西蒙古族藏族自治州
              </a>
            </div>

          </div>



          <div id="sc_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://sc.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chengdu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                成都
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zigong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                自贡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://pzh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                攀枝花
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://luzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                泸州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://deyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                德阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://mianyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                绵阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guangyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                广元
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://suining.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                遂宁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://neijiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                内江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://leshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                乐山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanchong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南充
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://meishan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                眉山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yibin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宜宾
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guangan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                广安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dazhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                达州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yaan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                雅安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://bazhong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                巴中
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ziyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                资阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://abzzqz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阿坝藏族羌族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://gzzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                甘孜藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lsyz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                凉山彝族自治州
              </a>
            </div>

          </div>



          <div id="sd_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://sd.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jinan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                济南
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qingdao.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                青岛
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zibo.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                淄博
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zaozhuang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                枣庄
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dongying.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                东营
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yantai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                烟台
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://weifang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                潍坊
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jining.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                济宁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://taian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                泰安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://weihai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                威海
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://rizhao.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                日照
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://laiwu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                莱芜
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://linyi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                临沂
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dezhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                德州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://liaocheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                聊城
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://binzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                滨州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://heze.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                菏泽
              </a>
            </div>

          </div>





          <div id="snx_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://snx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                西安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tongchuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                铜川
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baoji.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宝鸡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xianyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                咸阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://weinan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                渭南
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yanan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                延安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hanzhong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                汉中
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yulin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                榆林
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ankang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                安康
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shangluo.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                商洛
              </a>
            </div>

          </div>



          <div id="sx_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://sx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://taiyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                太原
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://datong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                大同
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yangquan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阳泉
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhangzhi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                长治
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jincheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                晋城
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shuozhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                朔州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jinzhong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                晋中
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yuncheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                运城
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xinzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                忻州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://linfen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                临汾
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lvliang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                吕梁
              </a>
            </div>

          </div>





          <div id="xj_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://xj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wlmq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                乌鲁木齐
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://klmy.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                克拉玛依
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tlfdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                吐鲁番地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hmdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                哈密地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://cjhz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                昌吉回族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://betlmg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                博尔塔拉蒙古自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://byglmg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                巴音郭楞蒙古自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://aksdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阿克苏地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://kzlskek.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                克孜勒苏柯尔克孜自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ksdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                喀什地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://htdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                和田地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ylhsk.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                伊犁哈萨克自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tcdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                塔城地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://altdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阿勒泰地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xjzx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                自治区直辖县级行政区划
              </a>
            </div>

          </div>



          <div id="xz_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://xz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lasa.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                拉萨
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://rkz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                日喀则
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://cddq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                昌都地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://sndq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                山南地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nqdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                那曲地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://aldq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阿里地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lzdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                林芝地区
              </a>
            </div>

          </div>



          <div id="yn_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://yn.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://kunming.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                昆明
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qujing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                曲靖
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yuxi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                玉溪
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baoshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                保山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhaotong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                昭通
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lijiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                丽江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://puer.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                普洱
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lincang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                临沧
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://cxyz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                楚雄彝族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hhhnzyz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                红河哈尼族彝族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wszzmz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                文山壮族苗族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xsbndz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                西双版纳傣族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dlbz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                大理白族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dhdzjpz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                德宏傣族景颇族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://njlsz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                怒江傈僳族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dqzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                迪庆藏族自治州
              </a>
            </div>

          </div>



          <div id="zj_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://zj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hangzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                杭州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ningbo.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宁波
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wenzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                温州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jiaxing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                嘉兴
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                湖州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shaoxing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                绍兴
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jinhua.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                金华
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://quzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                衢州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhoushan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                舟山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://taizhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                台州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lishui.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                丽水
              </a>
            </div>

          </div>


      </div>
    </div>
          <!--企业描述-->
          <div class="line_bottom ml30 mr30 pt15 pb15">
            <span class="f14 new-c2 mr30">企业描述</span>
            <div class="in-block">
              <!--行业分类-->
              <div class="cateNowBox btn-group mr50"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Hangye"
              >
                <div class="filter_btn point">
                  <span class="in-block overflow-width vertival-middle c2"
                        style="width: 57px;">行业分类</span>
                  <span class="caret new-c1 in-block vertival-middle"></span>
                </div>
                <div class="cateSubItem position-abs b-c-white new-border border-right-none border-shadow"
                     style="z-index: 100;width: 260px;">

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">全部</a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocD?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">电力、热力、燃气及水生产和供应业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocD?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc45?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        燃气生产和供应业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc44?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        电力、热力生产和供应业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc46?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        水的生产和供应业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocE?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">建筑业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocE?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc49?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        建筑安装业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc48?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        土木工程建筑业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc47?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        房屋建筑业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc50?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        建筑装饰和其他建筑业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocF?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">批发和零售业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocF?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc51?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        批发业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc52?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        零售业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocG?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">交通运输、仓储和邮政业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocG?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc59?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        仓储业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc58?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        装卸搬运和运输代理业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc57?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        管道运输业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc56?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        航空运输业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc55?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        水上运输业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc60?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        邮政业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc53?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        铁路运输业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc54?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        道路运输业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocA?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">农、林、牧、渔业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocA?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc04?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        渔业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc05?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        农、林、牧、渔服务业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc01?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        农业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc02?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        林业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc03?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        畜牧业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocB?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">采矿业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocB?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc11?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        开采辅助活动
                      </a>

                      <a href="https://www.tianyancha.com/search/oc12?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        其他采矿业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc08?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        黑色金属矿采选业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc09?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        有色金属矿采选业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc06?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        煤炭开采和洗选业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc07?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        石油和天然气开采业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc10?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        非金属矿采选业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocC?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">制造业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocC?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc35?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        专用设备制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc36?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        汽车制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc33?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        金属制品业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc34?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        通用设备制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc39?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        计算机、通信和其他电子设备制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc37?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        铁路、船舶、航空航天和其他运输设备制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc38?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        电气机械和器材制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc43?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        金属制品、机械和设备修理业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc42?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        废弃资源综合利用业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc41?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        其他制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc40?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        仪器仪表制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc22?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        造纸和纸制品业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc23?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        印刷和记录媒介复制业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc24?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        文教、工美、体育和娱乐用品制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc25?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        石油加工、炼焦和核燃料加工业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc26?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        化学原料和化学制品制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc27?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        医药制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc28?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        化学纤维制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc29?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        橡胶和塑料制品业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc30?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        非金属矿物制品业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc32?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        有色金属冶炼和压延加工业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc31?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        黑色金属冶炼和压延加工业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc19?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        皮革、毛皮、羽毛及其制品和制鞋业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc17?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        纺织业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc18?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        纺织服装、服饰业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc15?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        酒、饮料和精制茶制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc16?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        烟草制品业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc13?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        农副食品加工业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc14?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        食品制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc21?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        家具制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc20?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        木材加工和木、竹、藤、棕、草制品业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocL?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">租赁和商务服务业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocL?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc71?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        租赁业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc72?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        商务服务业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocM?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">科学研究和技术服务业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocM?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc73?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        研究和试验发展
                      </a>

                      <a href="https://www.tianyancha.com/search/oc74?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        专业技术服务业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc75?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        科技推广和应用服务业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocN?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">水利、环境和公共设施管理业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocN?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc78?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        公共设施管理业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc77?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        生态保护和环境治理业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc76?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        水利管理业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocO?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">居民服务、修理和其他服务业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocO?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc79?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        居民服务业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc80?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        机动车、电子产品和日用产品修理业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc81?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        其他服务业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocH?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">住宿和餐饮业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocH?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc62?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        餐饮业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc61?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        住宿业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocI?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">信息传输、软件和信息技术服务业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocI?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc64?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        互联网和相关服务
                      </a>

                      <a href="https://www.tianyancha.com/search/oc65?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        软件和信息技术服务业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc63?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        电信、广播电视和卫星传输服务
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocJ?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">金融业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocJ?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc67?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        资本市场服务
                      </a>

                      <a href="https://www.tianyancha.com/search/oc66?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        货币金融服务
                      </a>

                      <a href="https://www.tianyancha.com/search/oc69?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        其他金融业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc68?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        保险业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocK?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">房地产业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocK?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc70?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        房地产业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocT?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">国际组织</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocT?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc96?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        国际组织
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocQ?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">卫生和社会工作</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocQ?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc83?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        卫生
                      </a>

                      <a href="https://www.tianyancha.com/search/oc84?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        社会工作
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocP?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">教育</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocP?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc82?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        教育
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocS?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">公共管理、社会保障和社会组织</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocS?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc95?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        基层群众自治组织
                      </a>

                      <a href="https://www.tianyancha.com/search/oc94?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        群众团体、社会团体和其他成员组织
                      </a>

                      <a href="https://www.tianyancha.com/search/oc93?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        社会保障
                      </a>

                      <a href="https://www.tianyancha.com/search/oc92?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        人民政协、民主党派
                      </a>

                      <a href="https://www.tianyancha.com/search/oc91?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        国家机构
                      </a>

                      <a href="https://www.tianyancha.com/search/oc90?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        中国共产党机关
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocR?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">文化、体育和娱乐业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocR?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc88?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        体育
                      </a>

                      <a href="https://www.tianyancha.com/search/oc89?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        娱乐业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc86?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        广播、电视、电影和影视录音制作业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc87?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        文化艺术业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc85?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        新闻和出版业
                      </a>

                    </div>

                  </div>

                </div>
              </div>
              <!--注册资本-->
              <div class="btn-group mr50 regNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Zhuceziben"
              >
                <div class="point filter_btn">
                  <span class="c2">注册资本</span>
                  <span class="caret new-c1"></span>
                </div>
                <div class="regSubItem position-abs b-c-white new-border border-shadow" style="z-index: 100;width: 125px;">

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 filter-select"
                    >
                      全部
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/or0100?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      0万－100万
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/or100200?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      100万－200万
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/or200500?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      200万－500万
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/or5001000?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      500万－1000万
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/or1000?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      1000万以上
                    </a>
                  </div>

                </div>
              </div>
              <!--注册时间-->
              <div class="btn-group mr50 regTimeNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Zhuceshijian"
              >
                <div class="point filter_btn">
                  <span class="c2">注册时间 </span>
                  <span class="caret new-c1"></span>
                </div>
                <div class="timeSubItem position-abs b-c-white new-border border-shadow" style="z-index: 100;width: 125px;">

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 filter-select"
                    >
                      全部
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/oe01?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      成立1年内
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/oe015?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      成立1－5年
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/oe510?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      成立5－10年
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/oe1015?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      成立10－15年
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/oe15?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      成立15年以上
                    </a>
                  </div>

                </div>
              </div>
              <!--企业状态-->
              <div class="btn-group mr50 statusNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Qiyezhuantai"
              >
                <div class="point filter_btn">
                  <span class="c2">企业状态</span>
                  <span class="caret new-c1"></span>
                </div>
                <div class="statusSubItem position-abs b-c-white new-border border-shadow"
                     style="z-index: 100;width: 80px;">

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 filter-select"
                    >全部</a>
                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/os1?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >在业</a>
                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/os2?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >存续</a>
                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/os3?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >吊销</a>
                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/os4?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >注销</a>
                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/os5?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >迁出</a>
                  </div>

                </div>
              </div>
            </div>
          </div>
          <!--高级筛选-->

          <div class="line_bottom ml30 mr30 pt15 pb15">
            <span class="f14 new-alert mr30">高级筛选</span>
            <div class="in-block">
              <!--联系电话-->
              <div class="btn-group mr50 phoneNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Lianxidianhua"
              >
                <div class="point filter_btn new-alert" is-need-state='true'>
                  联系电话
                  <span class="caret new-c1"></span>
                </div>
                <div class="phoneSubItem position-abs b-c-white new-border border-shadow"
                     style="z-index: 100;width: 105px;">

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512  point c2 filter-select"
                          onclick="searchNeedVip()">全部</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512  point c2 "
                          onclick="searchNeedVip()">有联系电话</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512  point c2 "
                          onclick="searchNeedVip()">无联系电话</span>

                  </div>

                </div>
              </div>
              <!--商标-->
              <div class="btn-group mr50 brandNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Shangbiao"
              >
                <div class="point filter_btn" is-need-state='true'>
                  商标
                  <span class="caret new-c1"></span>
                </div>
                <div class="brandSubItem position-abs b-c-white new-border border-shadow"
                     style="z-index: 100;width: 105px;">

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2 filter-select"
                          onclick="searchNeedVip()">全部</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2 "
                          onclick="searchNeedVip()">有商标</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2 "
                          onclick="searchNeedVip()">无商标</span>

                  </div>

                </div>
              </div>
              <!--专利-->
              <div class="btn-group mr50 patentNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Zhuanli"
              >
                <div class="point filter_btn" is-need-state='true'>
                  专利
                  <span class="caret new-c1"></span>
                </div>
                <div class="patentSubItem position-abs b-c-white new-border border-shadow"
                     style="z-index: 100;width: 105px;">

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2 filter-select "
                          onclick="searchNeedVip()">全部</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2  "
                          onclick="searchNeedVip()">有专利</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2  "
                          onclick="searchNeedVip()">无专利</span>

                  </div>

                </div>
              </div>
              <!--失信信息-->
              <div class="btn-group mr50 dishonestNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Shixin"
              >
                <div class="point filter_btn" is-need-state='true'>
                  失信信息
                  <span class="caret new-c1"></span>
                </div>

                <div class="dishonestSubItem position-abs b-c-white new-border border-shadow"
                     style="z-index: 100;width: 105px;">

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2 filter-select "
                          onclick="searchNeedVip()">全部</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2  "
                          onclick="searchNeedVip()">有失信信息</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2  "
                          onclick="searchNeedVip()">无失信信息</span>

                  </div>

                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mb15 text-center">
        <div class="in-block point pl15 pr15 pt2 pb2 b-c-subgray new-c2 new-border" id="searchTogal">
          <i class="fa fa-angle-up mr2 f14"></i>收起
        </div>
      </div>
    </div>





            <!--数据导出-->

            <div ng-if="!isTypeSearch&&(nodes | filter:{type:'1'}).length>0;">
              <div class="pl30 new-c1 b-c-subgray filter2017"
                   style="border-left: 1px solid #eee; border-right: 1px solid #eee;">
                <span
                  class="new-err f14 in-block vertival-middle pt15 pb15">2231</span>
                <span class="f14 in-block mr17 vertival-middle pt15 pb15">家相关公司</span>


                <span class="f12 in-block vertival-middle pt15 pb15">
                  普通用户可查看100家公司，
                  <a tyc-event-click tyc-event-ch="CompanySearch.Shuliang.VIP"
                     class="new-alert point" onclick="showVip()" target="_blank">升级成为VIP会员，可查看5000+家公司</a>
                </span>

                <span tyc-event-click tyc-event-ch="CompanySearch.DaoShuju"
                      is-need-state='true'
                      class="c-white f13 in-block float-right pl15 pr15 pt6 pb6 mt10 mb10 point vertival-middle mr30 "
                      style="background-color: #ff730c;"
                      onclick="searchOrder()">
                    导出联系方式
                </span>
                <div class="btn-group in-block phoneNowBox vertival-middle float-right pt10 mr15">
                  <div class="f13 pl10 pr5 pt6 pb6 b-c-white point new-border new-c3 "
                       is-need-state='true'>
                    <span class="overflow-width in-block vertival-middle"
                          style="width: 89px;">默认排序</span>
                    <span class="caret new-c1 vertival-middle"></span>
                  </div>
                  <div class="phoneSubItem position-abs b-c-white new-border border-shadow"
                       style="z-index: 100;width: 120px;">


                    <div class="pt8 pb8 pl15 pr10 block border-shadow-hover"
                         tyc-event-click tyc-event-ch="CompanySearch.Paixu.*"
                    >
                      <a class="cateName512  point new-c3 filter-select"
                         href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
                         href-new-event event-name="筛选-排序">默认排序</a>
                    </div>

                    <div class="pt8 pb8 pl15 pr10 block border-shadow-hover"
                         tyc-event-click tyc-event-ch="CompanySearch.Paixu.1"
                    >
                      <a class="cateName512  point new-c3 "
                         href="https://www.tianyancha.com/search/ola1?key=%E6%96%B9%E5%BE%97"
                         href-new-event event-name="筛选-排序">注册资本降序</a>
                    </div>

                    <div class="pt8 pb8 pl15 pr10 block border-shadow-hover"
                         tyc-event-click tyc-event-ch="CompanySearch.Paixu.2"
                    >
                      <a class="cateName512  point new-c3 "
                         href="https://www.tianyancha.com/search/ola2?key=%E6%96%B9%E5%BE%97"
                         href-new-event event-name="筛选-排序">注册资本升序</a>
                    </div>

                    <div class="pt8 pb8 pl15 pr10 block border-shadow-hover"
                         tyc-event-click tyc-event-ch="CompanySearch.Paixu.3"
                    >
                      <a class="cateName512  point new-c3 "
                         href="https://www.tianyancha.com/search/ola3?key=%E6%96%B9%E5%BE%97"
                         href-new-event event-name="筛选-排序">注册时间降序</a>
                    </div>

                    <div class="pt8 pb8 pl15 pr10 block border-shadow-hover"
                         tyc-event-click tyc-event-ch="CompanySearch.Paixu.4"
                    >
                      <a class="cateName512  point new-c3 "
                         href="https://www.tianyancha.com/search/ola4?key=%E6%96%B9%E5%BE%97"
                         href-new-event event-name="筛选-排序">注册时间升序</a>
                    </div>

                  </div>
                </div>
              </div>
              <div class="row_hr">
                <hr>
              </div>
            </div>





    <div class="b-c-white search_result_container">

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="上海雷骊机电有限公司"
               src="https://img.tianyancha.com/logo/lll/836486d8560a810d8ec41dd772a21ad5.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/258898965" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">上海雷骊机电有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>上海
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="105.24335389525808 51.83627878423158"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">67</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">67</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="邹斌宏">邹斌宏</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="200万人民币">200万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2011-08-24 00:00:00.0">2011-08-24</span>
              </div>


              <div>
                <div class="add">
                  <span>商标信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="广州方得物流有限公司"
               src="https://img.tianyancha.com/logo/lll/bfef349c3e381270be6d863eb3cfedaa.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2333407233" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">广州<em>方得</em>物流有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>广东
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="94.2477796076938 62.83185307179587"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">60</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">60</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="涂松林">涂松林</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="500万人民币">500万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2014-07-25 00:00:00.0">2014-07-25</span>
              </div>


              <div>
                <div class="add">
                  <span>商标信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="慈溪市非非贸易有限公司"
               src="https://img.tianyancha.com/logo/lll/f6d7210d28487db159998834e6a8cd8e.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/56959741" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">慈溪市非非贸易有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>浙江
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="92.6769832808989 64.40264939859077"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">59</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">59</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="黄志平">黄志平</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="50.000000万人民币">50.000000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2014-04-17 00:00:00.0">2014-04-17</span>
              </div>


              <div>
                <div class="add">
                  <span>商标信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="北京一点得咨询有限公司"
               src="https://img.tianyancha.com/logo/lll/316fb8b1ffaa65d45dfb298710de1c37.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/10016633" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">北京一点得咨询有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>北京
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="86.39379797371932 70.68583470577035"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">55</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">55</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                开业
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="姚蔚">姚蔚</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="100 万元 人民币">100 万元 人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2009-04-14 00:00:00.0">2009-04-14</span>
              </div>


              <div>
                <div class="add">
                  <span>公司简称</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>网
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="北京方得机电有限公司"
               src="https://img.tianyancha.com/logo/lll/2a1e7d87f44acca2eb416de7ea18b753.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/6834173" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">北京<em>方得</em>机电有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>北京
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="83.25220532012952 73.82742735936014"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">53</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">53</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                开业
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="李国田">李国田</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="200 万人民币">200 万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2009-07-01 00:00:00.0">2009-07-01</span>
              </div>


              <div>
                <div class="add">
                  <span>商标信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="杭州方得投资管理有限公司"
               src="https://img.tianyancha.com/logo/lll/382a1ba77d41f2614c6ba2acc3aec244.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/1624424898" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">杭州<em>方得</em>投资管理有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>浙江
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="125.66370614359174 31.415926535897924"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">80</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">80</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="吴勃">吴勃</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="500.000000万人民币">500.000000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-06-23 00:00:00.0">2015-06-23</span>
              </div>


              <div>
                <div class="add">
                  <span>产品信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="辽宁方得技术有限公司"
               src="https://img.tianyancha.com/logo/lll/cd1f7491a2f7c3966d48c8dc942c3115.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/1185508244" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">辽宁<em>方得</em>技术有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>辽宁
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="150.79644737231007 6.2831853071795924"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">96</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">96</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="金雷">金雷</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="2000 万人民币">2000 万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-05-19 00:00:00.0">2015-05-19</span>
              </div>


              <div>
                <div class="add">
                  <span>网站名称</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    辽宁<em>方得</em>技术有限公司
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="河南省方得置业有限公司"
               src="https://img.tianyancha.com/logo/lll/b7441bfdf57a93854c268beb09f52c69.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/276313057" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">河南省<em>方得</em>置业有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>河南
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="135.0884841043611 21.991148575128555"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">86</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">86</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="白金增">白金增</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="1001万人民币">1001万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2010-01-12 00:00:00.0">2010-01-12</span>
              </div>


              <div>
                <div class="add">
                  <span>网站名称</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    河南省<em>方得</em>置业有限公司
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="上海阗鑫方得金融信息服务有限公司"
               src="https://img.tianyancha.com/logo/lll/665d612e01cdae49f5b92d0ced60388c.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/1220880034" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">上海阗鑫<em>方得</em>金融信息服务有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>上海
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="139.8008730847458 17.27875959474386"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">89</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">89</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="陈光熠">陈光熠</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="1000万人民币">1000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-06-30 00:00:00.0">2015-06-30</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="杭州方得智能科技有限公司"
               src="https://img.tianyancha.com/logo/lll/8826a977dbfb6e25bcc5da0e66eddba4.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2339758255" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">杭州<em>方得</em>智能科技有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>浙江
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="135.0884841043611 21.991148575128555"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">86</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">86</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="彭长书">彭长书</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="135.135000万人民币">135.135000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-05-18 00:00:00.0">2015-05-18</span>
              </div>


              <div>
                <div class="add">
                  <span>公司简称</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>智能
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="上海惟旭方得股权投资管理合伙企业（有限合伙）"
               src="https://img.tianyancha.com/logo/lll/62bbeb99a7f7dd4fb1d8bad383cbf0f4.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/531648796" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">上海惟旭<em>方得</em>股权投资管理合伙企业（有限合伙）</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>上海
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="142.94246573833559 14.137166941154065"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">91</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">91</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="祝毅">祝毅</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="-">-</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2011-08-19 00:00:00.0">2011-08-19</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="武汉方得教育咨询有限公司"
               src="https://img.tianyancha.com/logo/lll/a530056c5604bad68c73799dfc71e452.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2989636637" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">武汉<em>方得</em>教育咨询有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>湖北
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="131.94689145077132 25.132741228718352"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">84</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">84</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="王婷">王婷</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="1000万人民币">1000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2016-11-24 00:00:00.0">2016-11-24</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="辽宁方得物流有限公司"
               src="https://img.tianyancha.com/logo/lll/6e681faef0b4cfd4945570cd592c7dd7.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/1240862310" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">辽宁<em>方得</em>物流有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>辽宁
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="125.66370614359174 31.415926535897924"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">80</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">80</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="金雷">金雷</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="500 万人民币">500 万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-07-06 00:00:00.0">2015-07-06</span>
              </div>


              <div>
                <div class="add">
                  <span>股东信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    辽宁<em>方得</em>技术有限公司
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="福建盈方得投资管理有限公司"
               src="https://img.tianyancha.com/logo/lll/91d75e4f050e764839dbc5fb7edbacef.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2344038470" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">福建盈<em>方得</em>投资管理有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>福建
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="127.23450247038663 29.84513020910303"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">81</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">81</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="林大春">林大春</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="1000.000000万人民币">1000.000000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-06-05 00:00:00.0">2015-06-05</span>
              </div>


              <div>
                <div class="add">
                  <span>网站名称</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    盈<em>方得</em>投资
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="廊坊方得环保科技有限公司"
               src="https://img.tianyancha.com/logo/lll/828bb57a302c24b554732a3b1def68b5.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/1256047049" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">廊坊<em>方得</em>环保科技有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>河北
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="124.09290981679683 32.98672286269282"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">79</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">79</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="高海丛">高海丛</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="800万人民币">800万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-05-14 00:00:00.0">2015-05-14</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="西咸新区方得信息技术有限公司"
               src="https://img.tianyancha.com/logo/lll/770829ef270b01bc9643a3fc4b11b624.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2976247958" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">西咸新区<em>方得</em>信息技术有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>陕西
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="127.23450247038663 29.84513020910303"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">81</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">81</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="杨杰">杨杰</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="2000万人民币">2000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2016-12-06 00:00:00.0">2016-12-06</span>
              </div>


              <div>
                <div class="add">
                  <span>股东信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    辽宁<em>方得</em>技术有限公司
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="山西乐活方得科技有限公司"
               src="https://img.tianyancha.com/logo/lll/b762c94e27aeaa12fda26e3b9650be91.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/3023766528" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">山西乐活<em>方得</em>科技有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>山西
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="120.95131716320704 36.12831551628262"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">77</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">77</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="王岩刚">王岩刚</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="1000万人民币">1000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2017-02-22 00:00:00.0">2017-02-22</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="广西方得科技有限公司"
               src="https://img.tianyancha.com/logo/lll/ae92b0c592b87d3b2799d1b816cc49d3.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2312476608" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">广西<em>方得</em>科技有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>广西
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="116.23892818282235 40.840704496667314"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">74</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">74</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="廖志屹">廖志屹</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="210万人民币">210万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2013-05-20 00:00:00.0">2013-05-20</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="东莞方得电子商务有限公司"
               src="https://img.tianyancha.com/logo/lll/39dbb742cac010dc8e1ee91f20d17995.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2961039820" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">东莞<em>方得</em>电子商务有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>广东
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="117.80972450961724 39.269908169872416"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">75</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">75</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="杨杰">杨杰</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="500万人民币">500万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2016-11-08 00:00:00.0">2016-11-08</span>
              </div>


              <div>
                <div class="add">
                  <span>股东信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    辽宁<em>方得</em>技术有限公司
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="济南方得商贸有限公司"
               src="https://img.tianyancha.com/logo/lll/827bc1f8fc520d0a77e5ead5c5e28599.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2363043839" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">济南<em>方得</em>商贸有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>山东
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="114.66813185602746 42.41150082346221"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">73</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">73</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                在营
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="野源">野源</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="200万人民币">200万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2016-03-16 00:00:00.0">2016-03-16</span>
              </div>


            </div>
          </div>
        </div>
      </div>

    </div>






            <!--其他tab搜索结果-->


            <!--翻页-->








    <div class="company_pager ng-scope in-block">
      <ul class="pagination-sm pagination ng-isolate-scope ng-valid ng-dirty ng-valid-parse" boundary-links="false"
          rotate="false" style="float: left;">






        <li class="pagination-prev ng-scope disabled">
          <a

            class="ng-binding">
            &lt;
          </a>
        </li>







        <li class="pagination-page ng-scope active ">
          <a

            class="ng-binding">
            1
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p2?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            2
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p3?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            3
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p4?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            4
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p5?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            5
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p6?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            6
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p7?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            7
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p8?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            8
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p9?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            9
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p10?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            10
          </a>
        </li>



        <li class="pagination-page ng-scope" style=""><a

            href="https://www.tianyancha.com/search/p11?key=%E6%96%B9%E5%BE%97"

            class="ng-binding ng-click-active">...</a></li>


        <li class="pagination-next ng-scope "><a

            href="https://www.tianyancha.com/search/p2?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">&gt;</a></li>
      </ul>
      <div class="total ng-binding">
        <span>共</span>
        112
        <span>页</span>
      </div>
    </div>




            <div onclick="xiaolingFind();" class="xiaolingfind">
              <div style="height: 30px;" class="float-right">
                <div style="line-height: 1.6;" class="c8 in-block vertival-middle f13">没有想要的查询结果？</div>
                <div class="f14 deepsearch in-block vertival-middle">
                  <i class="fa fa-search"></i><span>深度搜索</span>
                </div>
              </div>
            </div>

            <div class="f12 team-left mb20">
              <span class="point new-alert" onclick="showVip()">升级成为VIP会员,可查看多达5000条相关结果</span>
            </div>


          </div>
          <!-- end main -->
          <!-- right -->
          <div class="col-3 text-center pt10"
               style="padding-left: 0; padding-right: 0;">
            <div class="banner position-relative">
      <a href="/vipintro" href-event event-name="VIP广告"
         tyc-event-click tyc-event-ch="CompangyDetail.Right.VIP"
         style="display: block;" target="_blank"  >
        <img src="https://static.tianyancha.com/wap/images/guanggaoVIP.png" style="width: 100%;" alt="vip">
      </a>
      <a href="https://www.tianyancha.com/invite"
         tyc-event-click tyc-event-ch="CompangyDetail.Right.XDL"
         target="_blank"  style="display: block;" class="mt10">
        <img src="https://static.tianyancha.com/wap/images/guanggaoApp726.jpg" style="width: 100%" alt="app下载"/>
      </a>
    </div>
          </div>
          <!-- end right -->
        </div>
      </div>
    </div>

      <div class="backToTop backTopPc backTopPcNew point" >
    	<div class="backtop_zd" onclick="backToTop.backToTop()"></div>
    	<div class="backtop_fk" onclick="backToTop.feedback();"></div>
      <div class="backtop_app" onclick="backToTop.toApp();"></div>
    	<div class="backtop_wx"  onmouseover="common.mouseShowBySelElem('.wxcontent')" onmouseleave="common.mouseHideBySelElem('.wxcontent')">
    	</div>
    	<div  class="wxcontent collapse"></div>
    </div>
      <div class="new-foot-v1 position-rel ng-isolate-scope c-white"
         style="bottom: 0px;background-color:#13326d;
         height: 345px;width:100%;"
         new-foot="">
      <div class="mainv2_tab_new"
           style="width:100%;background:transparent;padding-top:50px;opacity:0.8;filter:alpha(opacity=80)">
        <div class="container company_container" style="padding:0 0 0 0px">
          <div style="padding-left:0;padding-right:0;padding-bottom:0px">
            <div class="col-9" style="padding-left:0;padding-right:0">
              <div class="foot1" style="border-right: 1px solid rgba(255,255,255,0.4)">
                <div class="footer_images footer_images_logo"></div>
                <div class="text" style="padding-bottom:0px;padding-top: 14px">
                  <div style="padding-bottom:6px"><a href="https://www.tianyancha.com/property/1" style="padding-right:26px"
                                                     class="c-white" target="_blank">关于我们</a> <a
                      href="https://www.tianyancha.com/property/3" class="c-white" target="_blank">版权政策</a></div>
                  <div style="padding-bottom:6px"><a href="https://www.tianyancha.com/property/2" style="padding-right:26px"
                                                     class="c-white" target="_blank">服务协议</a> <a
                      href="https://www.tianyancha.com/property/4" class="c-white" target="_blank">免责声明</a></div>
                  <div>
                    <a href="https://www.tianyancha.com/property/5" style="padding-right:26px" class="c-white" target="_blank">权利通知</a>
                    <a href="http://open.tianyancha.com" style="padding-right:26px" class="c-white" target="_blank">数据服务</a>
                  </div>
                  <div class="pt5">
                    <a href="https://www.tianyancha.com/business" style="padding-right:26px" class="c-white" target="_blank">商务通道</a>
                  </div>
                </div>
              </div>
              <div class="foot2">
                <div class="text"><span class="c-white" style="margin-top: 12px">联系我们</span> <span class="c-white"><i
                      class="fa fa-phone"></i>电话 : 400-871-6266 [工作日: 9:00-18:30 ]</span> <span class="c-white"><i
                      class="fa fa-user"></i>在线客服 : <a href="http://q.url.cn/s/tWKXe2m?_type=wpa" class="c-white"
                                                       nofollow
                                                       target="_blank">2852375336</a></span> <span class="c-white"><i
                      class="fa fa-envelope"></i>商务合作 : bd@tianyancha.com</span>
                </div>
              </div>
              <div class="foot3" style="border-right:none"><a class="c-white footer_images footer_images_complaint"
                                                              onclick="footer.openComplaint()"
                                                              style="cursor:pointer;margin-bottom:15px;margin-top:0px">
                  <div></div>
                  投诉</a> <a class="c-white footer_images footer_images_wapqq" href="http://q.url.cn/s/tWKXe2m?_type=wpa"
                            nofollow
                            target="_blank" style="margin-bottom:15px;margin-top:0px">
                  <div></div>
                  在线咨询</a> <a class="c-white footer_images footer_images_weibo" href="http://weibo.com/tianyancha"
                              nofollow
                              target="_blank" style="margin-bottom:5px">
                  <div></div>
                  新浪微博</a>
              </div>
              <div class="foot4" style="border-left: 1px solid rgba(255,255,255,0.4)">
                <div class="c-white">数据来源</div>
                <div class="c-white"><span></span>全国企业信用信息公示系统</div>
                <div class="c-white"><span></span>中国裁判文书网</div>
                <div class="c-white"><span></span>中国执行信息公开网</div>
              </div>
              <div class="foot5">
                <div class="c-white"><span></span>国家知识产权局</div>
                <div class="c-white"><span></span>商标局</div>
                <div class="c-white"><span></span>版权局</div>
              </div>
            </div>
            <div class="col-3">
              <div class="text-right">
                <div class="right_item text-center" style="margin-right:34px">
                  <div style="color:#fff">微信公众号</div>
                  <img src="https://static.tianyancha.com/wap/images/wechat_foot.png" alt="微信公众号"></div>
                <div class="right_item text-center">
                  <div style="color:#fff">天眼查APP</div>
                  <img src="https://static.tianyancha.com/wap/images/footer_download.png" style="width: 84px"
                       alt="天眼查APP"
                  ></div>
              </div>
            </div>
          </div>
        </div>
        <div class="company_container friend_link f12 mt60 pt15" style="border-top:1px solid rgba(255,255,255,0.4)"><span>友情链接：</span>
          <a href="http://www.baike.com/" nofollow target="_blank" class="c-white">互动百科</a></div>
      </div>
      <div class="position-abs over-hide f12 pb10 pt10"
           style="left: 0;right: 0;bottom: 0;color: #405e97;background-color: #0d234d;">
        <div class="company_container margin-auto">
          <span>版权所有：北京金堤科技有限公司</span>
          <span>©2015 JINDIDATA 京ICP备14061319</span>
          <span class="pl10">固定电话：400-871-6266</span>
          <div class="float-right">
            <div
              class="footer_images footer_images_beian">
              <img alt="." src="https://img2.tianyancha.com/beianicon.gif?_t=1501160364448">
            </div>
            <span>京公网安备 11010802021795号</span>
          </div>
          <div>地址：北京市海淀区知春路63号中国卫星通信大厦B座23层</div>

        </div>
      </div>

    </div>
    </div>
    <div id="banner_web"></div>
    <script>
      var gdt_tracker = gdt_tracker || [];
      gdt_tracker.push(["set_source_id", "33937"]);
      (function () {
        var userAgent = navigator.userAgent;
        if (userAgent.indexOf('ignore') < 0) {
          var doc = document, h = doc.getElementsByTagName("head")[0], s = doc.createElement("script");
          s.async = true;
          s.src = "https://qzs.qq.com/qzone/biz/res/gt.js";
          h && h.insertBefore(s, h.firstChild)
        }
      })();
    </script>
    <script>

      var _hmt = _hmt || [];
      (function () {
        var userAgent = navigator.userAgent;
        if (userAgent.indexOf('ignore') < 0) {
          var hm = document.createElement("script");
          hm.src = "//hm.baidu.com/hm.js?e92c8d65d92d534b0fc290df538b4758";
          var s = document.getElementsByTagName("script")[0];
          s.parentNode.insertBefore(hm, s);
        }
      })();

    </script>
    <script>

      (function(){
        var bp = document.createElement('script');
        var curProtocol = window.location.protocol.split(':')[0];
        if (curProtocol === 'https') {
          bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
        }
        else {
          bp.src = 'http://push.zhanzhang.baidu.com/push.js';
        }
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(bp, s);
      })();

    </script>
    </body>
    </html>"""
    return doc




def downloadPage1(url):
    headers = {

        "Host": "www.tianyancha.com",
        "Connection": "keep - alive",
        "Upgrade - Insecure - Requests": "1",
        "User - Agent": "Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 59.0.3064.0 Safari / 537.36",
        "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8.",
        "Referer": "https: // www.tianyancha.com /",
        "Accept - Encoding": "gzip, deflate, br",
        "Accept - Language": "zh - CN, zh; q = 0.8",
        "Cookie": "ssuid=9316319424; jsid=SEM-SOUGOU-PP-SY-000099; _pk_ref.6835.e431=%5B%22%22%2C%22%22%2C1498800876%2C%22https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_qbhB5TwFUHrSv1MbFsrL0IBuo9pqAzDXqP8HWkNU_zKtm8N1pmsKgK%26query%3D%E5%87%AF%E7%9F%B3%E9%80%9A%22%5D; _pk_ref.1.e431=%5B%22%22%2C%22%22%2C1498800876%2C%22https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_qbhB5TwFUHrSv1MbFsrL0IBuo9pqAzDXqP8HWkNU_zKtm8N1pmsKgK%26query%3D%E5%87%AF%E7%9F%B3%E9%80%9A%22%5D; _pk_id.6835.e431=4506091f68130793.1497342237.10.1498800896.1498800876.; _pk_id.1.e431=66a8c05821cb6b5a.1497342237.10.1498800897.1498800876.; aliyungf_tc=AQAAABtL5x8slgYASLWPccdhvZ7ucdar; csrfToken=i0I-RfJAJAy8zqCM75VBslgO; TYCID=5957f6b072ba11e78a0105670635d82b; uccid=0adec762c1cc7ffe51c566d571c8694f; tyc-user-info=%257B%2522new%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTcwMDczMzE5NyIsImlhdCI6MTUwMTE1OTEzNiwiZXhwIjoxNTE2NzExMTM2fQ.0giWG2H6LGP_7xKwIaiLvFRezL5TM74hY1zjuUimNIvgg2dnDot8V-dLprd_oCRVVmABBdYrL1z6kusr6Z-K4Q%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215700733197%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTcwMDczMzE5NyIsImlhdCI6MTUwMTE1OTEzNiwiZXhwIjoxNTE2NzExMTM2fQ.0giWG2H6LGP_7xKwIaiLvFRezL5TM74hY1zjuUimNIvgg2dnDot8V-dLprd_oCRVVmABBdYrL1z6kusr6Z-K4Q; _csrf=gdG0D24jOPeOpmIYwXnI8g==; OA=MehB8UJnQba9MKzQq9kEaonMBa6mhI3BLYtnGiR9PelCw891fLMl4eP5cxP3lfUwdeBuWvVie1706nJqBFPtWKYohCUs/vd4HTDHnCatnsoFA2MRwM8k0SDv9mxBMkri; _csrf_bk=c94b7006415251e185344ea5bf420282; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1498800875,1501153035; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1501171190"

    }

    headers1 = {

        "Host": "www.tianyancha.com",
        "Connection": "keep - alive",
        "Upgrade - Insecure - Requests": "1",
        "User - Agent": "Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 59.0.3064.0 Safari / 537.36",
        "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8.",
        "Referer": "https: // www.tianyancha.com / search / t100?key = % E6 % 96 % B9 % E5 % BE % 97",
        "Accept - Encoding": "gzip, deflate, br",
        "Accept - Language": "zh - CN, zh; q = 0.8",
        "Cookie": "ssuid=9316319424; jsid=SEM-SOUGOU-PP-SY-000099; _pk_ref.6835.e431=%5B%22%22%2C%22%22%2C1498800876%2C%22https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_qbhB5TwFUHrSv1MbFsrL0IBuo9pqAzDXqP8HWkNU_zKtm8N1pmsKgK%26query%3D%E5%87%AF%E7%9F%B3%E9%80%9A%22%5D; _pk_ref.1.e431=%5B%22%22%2C%22%22%2C1498800876%2C%22https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_qbhB5TwFUHrSv1MbFsrL0IBuo9pqAzDXqP8HWkNU_zKtm8N1pmsKgK%26query%3D%E5%87%AF%E7%9F%B3%E9%80%9A%22%5D; _pk_id.6835.e431=4506091f68130793.1497342237.10.1498800896.1498800876.; _pk_id.1.e431=66a8c05821cb6b5a.1497342237.10.1498800897.1498800876.; aliyungf_tc=AQAAABtL5x8slgYASLWPccdhvZ7ucdar; csrfToken=i0I-RfJAJAy8zqCM75VBslgO; TYCID=5957f6b072ba11e78a0105670635d82b; uccid=0adec762c1cc7ffe51c566d571c8694f; tyc-user-info=%257B%2522new%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTcwMDczMzE5NyIsImlhdCI6MTUwMTE1OTEzNiwiZXhwIjoxNTE2NzExMTM2fQ.0giWG2H6LGP_7xKwIaiLvFRezL5TM74hY1zjuUimNIvgg2dnDot8V-dLprd_oCRVVmABBdYrL1z6kusr6Z-K4Q%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215700733197%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTcwMDczMzE5NyIsImlhdCI6MTUwMTE1OTEzNiwiZXhwIjoxNTE2NzExMTM2fQ.0giWG2H6LGP_7xKwIaiLvFRezL5TM74hY1zjuUimNIvgg2dnDot8V-dLprd_oCRVVmABBdYrL1z6kusr6Z-K4Q; _csrf=gdG0D24jOPeOpmIYwXnI8g==; OA=MehB8UJnQba9MKzQq9kEaonMBa6mhI3BLYtnGiR9PelCw891fLMl4eP5cxP3lfUwdeBuWvVie1706nJqBFPtWKYohCUs/vd4HTDHnCatnsoFA2MRwM8k0SDv9mxBMkri; _csrf_bk=c94b7006415251e185344ea5bf420282; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1498800875,1501153035; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1501171190"

    }

    data = requests.get(url, headers=headers1).content

    doc = """<!DOCTYPE html>
    <html>
    <head>
      <meta charset=utf-8>
      <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
      <title>天眼查-人人都在用企业信息调查工具_企业信息查询_公司查询_工商查询_信用查询平台</title>
      <meta http-equiv="pragma" content="no-cache">
      <meta http-equiv="cache-control" content="no-cache">
      <meta http-equiv="expires" content="0">

      <meta http-equiv="cache-control" content="no-transform"/>
      <meta http-equiv="cache-control" content="no-siteapp"/>
      <meta name="applicable-device" content="pc,mobile">
      <meta name="MobileOptimized" content="width"/>
      <meta name="HandheldFriendly" content="true"/>

      <meta name="description" itemprop="description" content="天眼查专注服务于个人与企业信息查询工具,为您提供企业查询,信息查询,工商查询,信用查询,公司查询等相关信息,帮您快速了解企业信息,企业工商信息,企业信用信息等企业经营和人员投资状况,查询更多企业信息就到天眼查官网！">
      <meta name="keywords" content="天眼查,企业查询,公司查询,工商查询,信用查询,企业信息查询,企业工商信息查询,企业信用查询,启信宝,企查查,红盾网">
      <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
            charset="UTF-8">

      <!--qq config-->
      <meta itemprop="name" content="天眼查-人人都在用企业信息调查工具_企业信息查询_公司查询_工商查询_信用查询平台">
      <meta itemprop="image" content="https://static.tianyancha.com/wap/images/weixinlogo.png">

      <meta name="fragment" content="!"/>

      <meta name="tyc-wx-type" content=""/>
      <meta name="tyc-wx-name" content=""/>
      <meta name="tyc-device" content="pc"/>

      <base href="/">
      <script>
        String.prototype.trim = function () {
          return this.replace(/(^\s*)|(\s*$)/g, "");
        }
        window.serverDomain = 'https://www.tianyancha.com'
        window.antirobotServer = 'https://antirobot.tianyancha.com'
        window.serverSuffix = '.tianyancha.com'
        window.cookieServerSuffix = '.tianyancha.com'
      </script>
      <script type="text/javascript" src="https://static.tianyancha.com/wap-require-js/public/js/require-6dc3b40987.config.js"></script>
      <script data-main="route/search"
              src="https://static.tianyancha.com/wap-require-js/public/js/lib/require.js"></script>

      <link rel="stylesheet" href="https://static.tianyancha.com/wap/css/font-awesome.min.css">
      <link rel="stylesheet" href="https://static.tianyancha.com/wap/css/bootstrap.css">

      <!-- build:css(./) resources/styles/app.css -->
      <!-- inject:css -->
      <link rel="stylesheet" href="https://static.tianyancha.com/wap-require-js/public/styles/main-19c79d2d66.css">
      <!-- endinject -->
      <!-- endbuild -->


      <style type="text/css">
        [ng\:cloak], [ng-cloak], [data-ng-cloak], [x-ng-cloak], .ng-cloak, .x-ng-cloak, .ng-hide {
          display: none !important;
        }

        ng\:form {
          display: block;
        }

        .ng-animate-start {
          clip: rect(0, auto, auto, 0);
          -ms-zoom: 1.0001;
        }

        .ng-animate-active {
          clip: rect(-1px, auto, auto, 0);
          -ms-zoom: 1;
        }
      </style>


      <!--[if lt IE 9]>
      <link rel="stylesheet" href="https://static.tianyancha.com/wap-require-js/resources/css/ie8-style.scss">
      <script src="https://static.tianyancha.com/wap/js/respond.js"></script>
      <![endif]-->

      <script>
        (function () {
          var method;
          var noop = function () {
          };
          var methods = [
            'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
            'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
            'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
            'timeline', 'timelineEnd', 'timeStamp', 'trace', 'warn'
          ];
          var length = methods.length;
          var console = (window.console = window.console || {});

          while (length--) {
            method = methods[length];

            // Only stub undefined methods.
            if (!console[method]) {
              console[method] = noop;
            }
          }
          CacheStoarge = function CacheStoarge() {
            var _bb = [];
            return {
              _tt: function (bbV, bbE, bbX) {
                bbX ? _bb.push(bbX) : _bb[bbV].push(bbE);
              },
              _ff: function (ii) {
                //console.log(_bb);
                return _bb[ii];
              }
            };
          };
          DOMImplementaiton = CacheStoarge();
        }());

      </script>

    </head>
    <body>








    <div class="company_input_v2" style="width: 100%; height: 74px;background:#14326e ;position: fixed; z-index: 1040;">
      <!--style="width: 100%; height: 74px;background:#29376B url('https://static.tianyancha.com/wap/images/bg-left-v1.jpg') repeat-x;position: fixed; z-index: 1040;"-->
      <!--id="company_input_web"-->
      <div class="container company_container">
        <div class="row" style="padding-left: 0;padding-right: 0; padding-top:0; padding-bottom: 0;">
          <div style="padding-left: 0;padding-right: 0;height: 74px; position: relative; " class="head-left">
            <a href="https://www.tianyancha.com" class="header_back_to_home " style="margin-top: 19px"></a>

            <div class="head-tab-outer" ng-hide="hideInput">
              <div class="head-tab-head c-white">
                <div class="in-block head-tab mr2 head-tab-c text-center point active"
                     onclick="header.changeSearchTab(event,'company')">
                  <div class="head-tab-top">查公司</div>
                </div>
                <div class="in-block head-tab mr2 head-tab-h text-center point "
                     tyc-event-click tyc-event-ch="DaoHang.HumanSearch.Tab"
                     onclick="header.changeSearchTab(event,'human')">
                  <div class="head-tab-top">查老板</div>
                </div>
                <div class="in-block head-tab head-tab-r text-center point "
                     tyc-event-click tyc-event-ch="DaoHang.RelationSearch.Tab"
                     onclick="header.jumpToPath(event)">
                  <div class="head-tab-top">查关系</div>
                </div>
              </div>
              <div class="head-tab-body head-tab-company">
                <div class="input-group search_group head-search-group-company"
                     style="display:">
                  <form onsubmit="return header.stopSubmit();" autocomplete="off">
                    <input id="live-search" type="search"
                           maxlength="50"
                           class="search_input form-control search_form input search-input-v1 f14 js-live-search"
                           placeholder='请输入企业名称、人名、产品名称或其它关键词'
                           value="方得"
                           style="border:none;"
                           click-selected="header.suggestToCompany"
                    >
                    <img alt="搜索" onclick="header.clearKey(event,'#live-search');" ng-show="key"
                         src="https://static.tianyancha.com/wap/images/close.png" class="clearNew"
                         width="20px"/>
                  </form>
                  <div class="input-group-addon input-search-v1"
                       tyc-event-click tyc-event-ch="DaoHang.CompanySearch.Search"
                       onclick="header.search(event)">
                  </div>
                </div>
                <div class="input-group search_group head-search-group-human"
                     style="display:none">
                  <form onsubmit="return header.stopHumanSubmit();" autocomplete="off">
                    <input type="search" class="search_input form-control search_form input search-input-v1 f14"
                           maxlength="50"
                           value=""
                           ng-model="humankey" ng-focus="pEvent('behaviour','searchFocus','');"
                           id="searchInputHuman"
                           placeholder='请输入人名、人名加地域/公司/产品关键词、用空格隔开'
                           style="border:none;"
                    >
                  </form>
                  <img onclick="header.clearKey(event,'#searchInputHuman');" ng-show="humankey"
                       src="https://static.tianyancha.com/wap/images/close.png" class="clearNew"
                       width="20px" alt="搜索"/>
                  <div class="input-group-addon input-search-v1" onclick="header.searchHuman(event)">
                  </div>
                </div>
              </div>
            </div>


          </div>
          <div
            style="padding-left: 0;padding-right: 0;position: relative; height: 74px;cursor:pointer;"
            class="head-right">
            <div class="right" style="padding-top: 22px">


              <div class="hover_title user_title" style="" ng-if="islogged" ng-init="userShow=false"
                   ng-mouseenter="userShow=true" ng-mouseleave="userShow=false"
                   onmouseleave="header.mouseHideById('#userShow')" onmouseenter="header.mouseShowById('#userShow')">
                <div class="in-block title1">
                  <div>
                    <a href="/usercenter/concern/1" href="/usercenter/concern/1" href-new-event event-name="导航-用户中心"
                       class="c-white">
                      <i class="fa fa-user"></i>
                      <span class="pr2">15700733197</span><i class="fa fa-caret-down" aria-hidden="true"></i>
                    </a>
                    <div class="list-group no-radius abs text-center collapse" id="userShow" ng-mouseenter="userShow=true"
                         ng-mouseleave="userShow=false">
                      <a class="list-group-item" href="/usercenter/concern/1">
                        关注企业
                      </a> <a class="list-group-item  " href="/usercenter/myorder">
                        我的订单
                      </a> <a class="list-group-item  " href="/usercenter/setpwd">
                        设置密码
                      </a>
                      <a class="list-group-item  " href="/usercenter/modifyInfo">
                        个人信息
                      </a>
                      <a class="list-group-item  " onclick="header.loginout(event)">
                        退出登录
                      </a>
                    </div>
                  </div>
                </div>
              </div>


              <div class="hover_title" style="">
                <span class="line1">|</span>
                <a class="title1" href="/vipintro" target="_blank"
                   tyc-event-click tyc-event-ch="DaoHang.VIP"
                > &nbsp;<i
                    class="fa fa-diamond"></i> 会员服务 </a>
                &nbsp;&nbsp;<span class="line1">|</span>
              </div>

              <div class="hover_title media_title"
                   ng-init="mediaHover=false" ng-mouseenter="mediaHover=true"
                   onmouseenter="header.mouseMediaShowById('#mediaHover')" ng-mouseleave="mediaHover=false"
                   onmouseleave="header.mouseMediaHideById('#mediaHover')" ng-class="{'media_title_h':mediaHover}">
                <div class="title1 in-block">
                  <div class="media_port pl6 pr6">
                    <img class="media_icon" src='https://static.tianyancha.com/wap/images/media_icon.png'
                         ng-src="{{!mediaHover?'https://static.tianyancha.com/wap/images/media_icon.png':'https://static.tianyancha.com/wap/images/media_icon_b.png'}}"
                         alt="合作通道"/>
                    <span class="pr7 no-mr">合作通道</span><i class="fa fa-caret-down" aria-hidden="true"></i>
                    <div class="list-group no-radius abs text-center collapse" id="mediaHover" ng-if="mediaHover"
                         ng-mouseenter="mediaHover=true" ng-mouseleave="mediaHover=false"
                         onmouseenter="header.mouseMediaShowById('#mediaHover')"
                         onmouseleave="header.mouseMediaHideById('#mediaHover')">
                      <a class="list-group-item" target="_blank" href="/appfortrial">
                        媒体通道
                      </a>
                      <a class="list-group-item" target="_blank" href="/business">
                        商务通道
                      </a>
                    </div>
                  </div>
                </div>
              </div>


              <div class="hover_title" style="">
                <span class="line1">|</span>
                <a class="title1" href="/invite" tyc-event-click tyc-event-ch="daohang.xdl" target="_blank" href-event event-name="导航-邀请有奖"> &nbsp;
                  <span class="yqyjIcon vertival-middle"></span>
                  <span class="in-block vertival-middle">邀请赢奖</span>
                </a>
              </div>


            </div>
          </div>

        </div>
      </div>
    </div>

    <div>



    <div ng-if="!errorMessagePage" style="width: 100%;" class="top_container_new b-c-gray">
      <div class="container company_container">
        <div class="row">
          <!-- main -->
          <div style="min-height: 840px;" class="col-9 search-2017-2 pr10 pl0">
            <!--搜索结果--人员-->





            <!--筛选项-->


    <div class="search-multi-filter b-c-white">

      <div class="search-multi-filter-head">
        <div class="position-abs">

          <a
            class="subTitle active"
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">企业</a>

          <a
            class="subTitle "
            href="https://www.tianyancha.com/search/t100?key=%E6%96%B9%E5%BE%97">司法风险</a>

          <a
            class="subTitle "
            href="https://www.tianyancha.com/search/t200?key=%E6%96%B9%E5%BE%97">经营风险</a>

          <a
            class="subTitle "
            href="https://www.tianyancha.com/search/t300?key=%E6%96%B9%E5%BE%97">经营状况</a>

          <a
            class="subTitle "
            href="https://www.tianyancha.com/search/t400?key=%E6%96%B9%E5%BE%97">知识产权</a>

        </div>
      </div>

      <!--其他搜索范围-->


      <!--企业搜索范围-->

      <div class="search-multi-filter-body search-scope">

        <div class="over-hide ml30 mr30 f14 pb15 new-c3" style="border-bottom: 1px dashed #E2E7E8;">
          <span class="search_filter_type_title f14 new-c2">搜索范围</span>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 filter-in-selected"
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
            全部
          </a>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 "
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97&searchType=company">
            企业
          </a>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 "
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97&searchType=human">
            法人/股东/高管
          </a>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 "
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97&searchType=brand">
            产品/商标
          </a>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 "
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97&searchType=similarAddr">
            联系方式
          </a>

          <a
            class="float-left list mr7 in-block pt2 pb2 c1 "
            href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97&searchType=scope">
            经营范围
          </a>

        </div>

        <div class="search_filter_box filter2017 b-c-white f14">
          <!--省份筛选new-->
          <div id="abbrCode" class="hidden"></div>
    <div id="checkProv" class="hidden"></div>

    <div class="ml30 mr30 pt15"
         tyc-event-click tyc-event-ch="CompanySearch.Filter.Shengfen"
    >
      <div>
        <span class="f14 new-c2 mr30 in-block vertical-top">省份地区</span>
        <div id="prov_box" class="in-block break-word over-hide baseContentBox" style="width: 670px;height:25px;">
          <div class="in-block mb10" style="width: 75px;">
            <a class="in-block pl10 pr10 c2 break-word new-list filter-in-selected filter-in-selected-border"
              href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
            >全部</a>
          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('ah')"
                  id="prov_ah"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">A</span>安徽</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <a class="in-block new-c3 pl8 pr8 break-word new-list point  "
                  href="https://bj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
            > <span class="">B</span> 北京</a>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <a class="in-block new-c3 pl8 pr8 break-word new-list point  "
                  href="https://cq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
            > <span class="">C</span> 重庆</a>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('fj')"
                  id="prov_fj"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">F</span>福建</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('gd')"
                  id="prov_gd"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">G</span>广东</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('gs')"
                  id="prov_gs"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">G</span>甘肃</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('gx')"
                  id="prov_gx"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">G</span>广西</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('gz')"
                  id="prov_gz"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">G</span>贵州</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('han')"
                  id="prov_han"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>海南</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('heb')"
                  id="prov_heb"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>河北</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('hen')"
                  id="prov_hen"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>河南</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('hlj')"
                  id="prov_hlj"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>黑龙江</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('hub')"
                  id="prov_hub"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>湖北</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('hun')"
                  id="prov_hun"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">H</span>湖南</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('jl')"
                  id="prov_jl"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">J</span>吉林</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('js')"
                  id="prov_js"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">J</span>江苏</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('jx')"
                  id="prov_jx"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">J</span>江西</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('ln')"
                  id="prov_ln"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">L</span>辽宁</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('nmg')"
                  id="prov_nmg"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">N</span>内蒙古</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('nx')"
                  id="prov_nx"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">N</span>宁夏</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('qh')"
                  id="prov_qh"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">Q</span>青海</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('sc')"
                  id="prov_sc"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">S</span>四川</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('sd')"
                  id="prov_sd"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">S</span>山东</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <a class="in-block new-c3 pl8 pr8 break-word new-list point  "
                  href="https://sh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
            > <span class="">S</span> 上海</a>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('snx')"
                  id="prov_snx"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">S</span>陕西</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('sx')"
                  id="prov_sx"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">S</span>山西</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <a class="in-block new-c3 pl8 pr8 break-word new-list point  "
                  href="https://tj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
            > <span class="">T</span> 天津</a>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('xj')"
                  id="prov_xj"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">X</span>新疆</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('xz')"
                  id="prov_xz"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">X</span>西藏</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('yn')"
                  id="prov_yn"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">Y</span>云南</span>

          </div>

          <div class="in-block mb10" style="width: 80px;">

            <span onclick="filterProvence('zj')"
                  id="prov_zj"
              class="in-block new-c3 pl8 pr8 break-word new-list point canClick  "
            ><span class="mr2">Z</span>浙江</span>

          </div>

        </div>
        <div id="baseShowMore" class="in-block vertical-top new-c3 point float-right">
          更多<i class="new-c9 ml5 fa fa-caret-down js-more-btn" ng-class="!hoverShow?'fa fa-caret-down':'fa fa-caret-up'"></i>
        </div>
      </div>

      <div id="filterBox">


          <div id="ah_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://ah.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hefei.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                合肥
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuhu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                芜湖
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://bangbu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                蚌埠
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huainan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                淮南
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://mas.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                马鞍山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huaibei.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                淮北
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tongling.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                铜陵
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://anqing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                安庆
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huangshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黄山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                滁州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fuyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阜阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://suzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宿州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://liuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                六安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://bozhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                亳州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chizhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                池州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xuancheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宣城
              </a>
            </div>

          </div>







          <div id="fj_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://fj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fzh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                福州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shamen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                厦门
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://putian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                莆田
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://sanming.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                三明
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://quanzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                泉州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhangzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                漳州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanping.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南平
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://longyan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                龙岩
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ningde.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宁德
              </a>
            </div>

          </div>



          <div id="gd_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://gd.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dongguan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                东莞
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhongshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                中山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guangzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                广州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shaoguan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                韶关
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shenzhen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                深圳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhuhai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                珠海
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shantou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                汕头
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://foshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                佛山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jiangmen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                江门
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhanjiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                湛江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://maoming.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                茂名
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhaoqing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                肇庆
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huizhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                惠州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://meizhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                梅州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shanwei.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                汕尾
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://heyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                河源
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yangjiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阳江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qingyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                清远
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chaozhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                潮州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jieyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                揭阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yunfu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                云浮
              </a>
            </div>

          </div>



          <div id="gs_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://gs.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jyg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                嘉峪关
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lanzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                兰州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jinchang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                金昌
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baiyin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                白银
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tianshui.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                天水
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuwei.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                武威
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhangye.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                张掖
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://pingliang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                平凉
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jiuquan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                酒泉
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qingyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                庆阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dingxi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                定西
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://longnan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                陇南
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lxhz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                临夏回族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://gnzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                甘南藏族自治州
              </a>
            </div>

          </div>



          <div id="gx_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://gx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanning.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南宁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://liuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                柳州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guilin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                桂林
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                梧州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://beihai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                北海
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fcg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                防城港
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qinzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                钦州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guigang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                贵港
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yul.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                玉林
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baise.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                百色
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hezhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                贺州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hechi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                河池
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://laibin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                来宾
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chongzuo.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                崇左
              </a>
            </div>

          </div>



          <div id="gz_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://gz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guiyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                贵阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lps.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                六盘水
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zunyi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                遵义
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://anshun.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                安顺
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://bijie.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                毕节
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tongren.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                铜仁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qxnbyz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黔西南布依族苗族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qdnz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黔东南州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qnbyz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黔南布依族苗族自治州
              </a>
            </div>

          </div>



          <div id="han_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://han.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://haikou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                海口
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://sanya.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                三亚
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hanzx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                省直辖县级行政区划
              </a>
            </div>

          </div>



          <div id="heb_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://heb.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://sjz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                石家庄
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tangshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                唐山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qhd.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                秦皇岛
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://handan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                邯郸
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xingtai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                邢台
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baoding.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                保定
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zjk.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                张家口
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chengde.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                承德
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://cangzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                沧州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://langfang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                廊坊
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hengshui.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                衡水
              </a>
            </div>

          </div>



          <div id="hen_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://hen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhengzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                郑州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://kaifeng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                开封
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://luoyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                洛阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://pds.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                平顶山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://anyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                安阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hebi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鹤壁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xinxiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                新乡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jiaozuo.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                焦作
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://puyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                濮阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xuchang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                许昌
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://luohe.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                漯河
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://smx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                三门峡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shangqiu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                商丘
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xinyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                信阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhoukou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                周口
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zmd.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                驻马店
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://henzx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                省直辖县级行政区划
              </a>
            </div>

          </div>



          <div id="hlj_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://hlj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://herb.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                哈尔滨
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qqhe.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                齐齐哈尔
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jixi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鸡西
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hegang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鹤岗
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://sys.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                双鸭山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://daqing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                大庆
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yich.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                伊春
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jms.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                佳木斯
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qth.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                七台河
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://mdj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                牡丹江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://heihe.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黑河
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://suihua.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                绥化
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dxaldq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                大兴安岭地区
              </a>
            </div>

          </div>



          <div id="hub_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://hub.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuhan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                武汉
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huangshi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黄石
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shiyan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                十堰
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yichang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宜昌
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xiangyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                襄阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ezhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鄂州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jingmen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                荆门
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xiaogan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                孝感
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jingzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                荆州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huanggang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黄冈
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xianning.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                咸宁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://suizhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                随州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://estjz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                恩施土家族苗族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hubzx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                省直辖县级行政区划
              </a>
            </div>

          </div>



          <div id="hun_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://hun.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhangsha.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                长沙
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                株洲
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xiangtan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                湘潭
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hengyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                衡阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shaoyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                邵阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yueyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                岳阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://changde.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                常德
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zjj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                张家界
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yiyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                益阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chenzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                郴州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yongzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                永州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huaihua.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                怀化
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://loudi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                娄底
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xxtjz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                湘西土家族苗族自治州
              </a>
            </div>

          </div>



          <div id="jl_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://jl.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhangchun.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                长春
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jilin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                吉林
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://siping.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                四平
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://liaoyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                辽源
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tonghua.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                通化
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baishan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                白山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://songyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                松原
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baicheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                白城
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ybcxz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                延边朝鲜族自治州
              </a>
            </div>

          </div>



          <div id="js_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://js.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanjing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南京
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuxi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                无锡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                徐州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://changzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                常州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://szh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                苏州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nantong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南通
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lyg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                连云港
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huaian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                淮安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yancheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                盐城
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yangzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                扬州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhenjiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                镇江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tzh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                泰州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://suqian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宿迁
              </a>
            </div>

          </div>



          <div id="jx_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://jx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanchang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南昌
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jdz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                景德镇
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://pingxiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                萍乡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jiujiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                九江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xinyu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                新余
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yingtan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鹰潭
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ganzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                赣州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                吉安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ych.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宜春
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fuzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                抚州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shangrao.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                上饶
              </a>
            </div>

          </div>



          <div id="ln_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://ln.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shenyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                沈阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dalian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                大连
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://anshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鞍山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fushun.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                抚顺
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://benxi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                本溪
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dandong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                丹东
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jinzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                锦州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yingkou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                营口
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://fuxin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阜新
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://liaoyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                辽阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://panjin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                盘锦
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tieling.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                铁岭
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chaoyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                朝阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hld.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                葫芦岛
              </a>
            </div>

          </div>



          <div id="nmg_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://nmg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hhht.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                呼和浩特
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baotou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                包头
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuhai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                乌海
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chifeng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                赤峰
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tongliao.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                通辽
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://eeds.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                鄂尔多斯
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hlbe.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                呼伦贝尔
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://byne.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                巴彦淖尔
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wlcb.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                乌兰察布
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xam.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                兴安盟
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xlglm.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                锡林郭勒盟
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://alsm.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阿拉善盟
              </a>
            </div>

          </div>



          <div id="nx_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://nx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yinchuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                银川
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://szs.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                石嘴山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wuzhong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                吴忠
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                固原
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhongwei.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                中卫
              </a>
            </div>

          </div>



          <div id="qh_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://qh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xining.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                西宁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://haidong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                海东
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hbzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                海北藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hunzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                黄南藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hnzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                海南藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://glzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                果洛藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yszz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                玉树藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hxmgz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                海西蒙古族藏族自治州
              </a>
            </div>

          </div>



          <div id="sc_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://sc.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://chengdu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                成都
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zigong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                自贡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://pzh.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                攀枝花
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://luzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                泸州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://deyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                德阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://mianyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                绵阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guangyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                广元
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://suining.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                遂宁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://neijiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                内江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://leshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                乐山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nanchong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                南充
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://meishan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                眉山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yibin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宜宾
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://guangan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                广安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dazhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                达州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yaan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                雅安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://bazhong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                巴中
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ziyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                资阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://abzzqz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阿坝藏族羌族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://gzzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                甘孜藏族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lsyz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                凉山彝族自治州
              </a>
            </div>

          </div>



          <div id="sd_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://sd.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jinan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                济南
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qingdao.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                青岛
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zibo.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                淄博
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zaozhuang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                枣庄
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dongying.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                东营
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yantai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                烟台
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://weifang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                潍坊
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jining.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                济宁
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://taian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                泰安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://weihai.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                威海
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://rizhao.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                日照
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://laiwu.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                莱芜
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://linyi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                临沂
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dezhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                德州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://liaocheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                聊城
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://binzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                滨州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://heze.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                菏泽
              </a>
            </div>

          </div>





          <div id="snx_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://snx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xian.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                西安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tongchuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                铜川
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baoji.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宝鸡
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xianyang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                咸阳
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://weinan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                渭南
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yanan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                延安
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hanzhong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                汉中
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yulin.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                榆林
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ankang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                安康
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shangluo.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                商洛
              </a>
            </div>

          </div>



          <div id="sx_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://sx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://taiyuan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                太原
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://datong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                大同
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yangquan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阳泉
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhangzhi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                长治
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jincheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                晋城
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shuozhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                朔州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jinzhong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                晋中
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yuncheng.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                运城
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xinzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                忻州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://linfen.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                临汾
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lvliang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                吕梁
              </a>
            </div>

          </div>





          <div id="xj_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://xj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wlmq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                乌鲁木齐
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://klmy.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                克拉玛依
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tlfdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                吐鲁番地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hmdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                哈密地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://cjhz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                昌吉回族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://betlmg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                博尔塔拉蒙古自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://byglmg.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                巴音郭楞蒙古自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://aksdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阿克苏地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://kzlskek.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                克孜勒苏柯尔克孜自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ksdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                喀什地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://htdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                和田地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ylhsk.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                伊犁哈萨克自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://tcdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                塔城地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://altdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阿勒泰地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xjzx.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                自治区直辖县级行政区划
              </a>
            </div>

          </div>



          <div id="xz_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://xz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lasa.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                拉萨
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://rkz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                日喀则
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://cddq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                昌都地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://sndq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                山南地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://nqdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                那曲地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://aldq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                阿里地区
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lzdq.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                林芝地区
              </a>
            </div>

          </div>



          <div id="yn_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://yn.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://kunming.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                昆明
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://qujing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                曲靖
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://yuxi.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                玉溪
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://baoshan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                保山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhaotong.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                昭通
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lijiang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                丽江
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://puer.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                普洱
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lincang.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                临沧
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://cxyz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                楚雄彝族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hhhnzyz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                红河哈尼族彝族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wszzmz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                文山壮族苗族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://xsbndz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                西双版纳傣族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dlbz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                大理白族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dhdzjpz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                德宏傣族景颇族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://njlsz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                怒江傈僳族自治州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://dqzz.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                迪庆藏族自治州
              </a>
            </div>

          </div>



          <div id="zj_Content" class="ml70 new-border b-c-gray pt10 pl10 pr10 hidden">
            <div class="in-block mb10 mr10">
              <a class="new-list pl10 pr10 pt2 pb2 border-radio2 new-c5 "
                 href="https://zj.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
              >全部</a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://hangzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                杭州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://ningbo.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                宁波
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://wenzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                温州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jiaxing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                嘉兴
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://huzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                湖州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://shaoxing.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                绍兴
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://jinhua.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                金华
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://quzhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                衢州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://zhoushan.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                舟山
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://taizhou.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                台州
              </a>
            </div>

            <div class="in-block mb10 mr10">
              <a
                class="new-list new-c5 pl10 pr10 pt2 pb2 border-radio2 "
                href="https://lishui.tianyancha.com/search?key=%E6%96%B9%E5%BE%97">
                丽水
              </a>
            </div>

          </div>


      </div>
    </div>
          <!--企业描述-->
          <div class="line_bottom ml30 mr30 pt15 pb15">
            <span class="f14 new-c2 mr30">企业描述</span>
            <div class="in-block">
              <!--行业分类-->
              <div class="cateNowBox btn-group mr50"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Hangye"
              >
                <div class="filter_btn point">
                  <span class="in-block overflow-width vertival-middle c2"
                        style="width: 57px;">行业分类</span>
                  <span class="caret new-c1 in-block vertival-middle"></span>
                </div>
                <div class="cateSubItem position-abs b-c-white new-border border-right-none border-shadow"
                     style="z-index: 100;width: 260px;">

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">全部</a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocD?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">电力、热力、燃气及水生产和供应业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocD?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc45?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        燃气生产和供应业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc44?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        电力、热力生产和供应业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc46?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        水的生产和供应业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocE?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">建筑业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocE?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc49?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        建筑安装业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc48?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        土木工程建筑业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc47?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        房屋建筑业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc50?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        建筑装饰和其他建筑业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocF?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">批发和零售业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocF?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc51?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        批发业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc52?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        零售业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocG?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">交通运输、仓储和邮政业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocG?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc59?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        仓储业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc58?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        装卸搬运和运输代理业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc57?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        管道运输业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc56?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        航空运输业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc55?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        水上运输业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc60?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        邮政业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc53?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        铁路运输业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc54?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        道路运输业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocA?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">农、林、牧、渔业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocA?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc04?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        渔业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc05?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        农、林、牧、渔服务业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc01?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        农业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc02?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        林业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc03?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        畜牧业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocB?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">采矿业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocB?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc11?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        开采辅助活动
                      </a>

                      <a href="https://www.tianyancha.com/search/oc12?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        其他采矿业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc08?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        黑色金属矿采选业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc09?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        有色金属矿采选业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc06?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        煤炭开采和洗选业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc07?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        石油和天然气开采业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc10?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        非金属矿采选业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocC?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">制造业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocC?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc35?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        专用设备制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc36?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        汽车制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc33?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        金属制品业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc34?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        通用设备制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc39?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        计算机、通信和其他电子设备制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc37?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        铁路、船舶、航空航天和其他运输设备制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc38?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        电气机械和器材制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc43?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        金属制品、机械和设备修理业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc42?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        废弃资源综合利用业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc41?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        其他制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc40?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        仪器仪表制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc22?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        造纸和纸制品业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc23?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        印刷和记录媒介复制业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc24?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        文教、工美、体育和娱乐用品制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc25?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        石油加工、炼焦和核燃料加工业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc26?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        化学原料和化学制品制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc27?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        医药制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc28?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        化学纤维制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc29?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        橡胶和塑料制品业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc30?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        非金属矿物制品业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc32?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        有色金属冶炼和压延加工业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc31?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        黑色金属冶炼和压延加工业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc19?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        皮革、毛皮、羽毛及其制品和制鞋业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc17?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        纺织业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc18?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        纺织服装、服饰业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc15?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        酒、饮料和精制茶制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc16?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        烟草制品业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc13?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        农副食品加工业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc14?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        食品制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc21?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        家具制造业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc20?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        木材加工和木、竹、藤、棕、草制品业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocL?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">租赁和商务服务业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocL?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc71?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        租赁业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc72?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        商务服务业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocM?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">科学研究和技术服务业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocM?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc73?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        研究和试验发展
                      </a>

                      <a href="https://www.tianyancha.com/search/oc74?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        专业技术服务业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc75?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        科技推广和应用服务业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocN?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">水利、环境和公共设施管理业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocN?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc78?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        公共设施管理业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc77?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        生态保护和环境治理业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc76?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        水利管理业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocO?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">居民服务、修理和其他服务业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocO?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc79?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        居民服务业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc80?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        机动车、电子产品和日用产品修理业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc81?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        其他服务业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocH?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">住宿和餐饮业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocH?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc62?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        餐饮业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc61?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        住宿业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocI?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">信息传输、软件和信息技术服务业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocI?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc64?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        互联网和相关服务
                      </a>

                      <a href="https://www.tianyancha.com/search/oc65?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        软件和信息技术服务业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc63?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        电信、广播电视和卫星传输服务
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocJ?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">金融业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocJ?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc67?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        资本市场服务
                      </a>

                      <a href="https://www.tianyancha.com/search/oc66?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        货币金融服务
                      </a>

                      <a href="https://www.tianyancha.com/search/oc69?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        其他金融业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc68?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        保险业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocK?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">房地产业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocK?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc70?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        房地产业
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocT?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">国际组织</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocT?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc96?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        国际组织
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocQ?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">卫生和社会工作</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocQ?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc83?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        卫生
                      </a>

                      <a href="https://www.tianyancha.com/search/oc84?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        社会工作
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocP?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">教育</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocP?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc82?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        教育
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocS?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">公共管理、社会保障和社会组织</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocS?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc95?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        基层群众自治组织
                      </a>

                      <a href="https://www.tianyancha.com/search/oc94?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        群众团体、社会团体和其他成员组织
                      </a>

                      <a href="https://www.tianyancha.com/search/oc93?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        社会保障
                      </a>

                      <a href="https://www.tianyancha.com/search/oc92?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        人民政协、民主党派
                      </a>

                      <a href="https://www.tianyancha.com/search/oc91?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        国家机构
                      </a>

                      <a href="https://www.tianyancha.com/search/oc90?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        中国共产党机关
                      </a>

                    </div>

                  </div>

                  <div style="width: 260px;position: relative" class="item77 cateItemHover">
                    <div class="pt8 pb8 pl10 pr10 canClick"
                         ng-class="cate.primInduCode == showIndus&&cate.secList?'filter-select':'new-border-right'">
                      <a href="https://www.tianyancha.com/search/ocR?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="cateName512 c2 ">文化、体育和娱乐业</a>

                      <i class="fa fa-angle-right float-right pt3 c2"></i>

                    </div>

                    <div class="position-abs b-c-white new-border cate_sub_item"
                         style="left: 259px;top:0;width: 259px;max-height: 505px;overflow-y: auto;">

                      <a href="https://www.tianyancha.com/search/ocR?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        全部
                      </a>

                      <a href="https://www.tianyancha.com/search/oc88?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        体育
                      </a>

                      <a href="https://www.tianyancha.com/search/oc89?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        娱乐业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc86?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        广播、电视、电影和影视录音制作业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc87?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        文化艺术业
                      </a>

                      <a href="https://www.tianyancha.com/search/oc85?key=%E6%96%B9%E5%BE%97"
                         ng-click="filterClick($event,'click','searchFilterTotal');"
                         class="pt8 pb8 pl10 c2 codeSecName block ">
                        新闻和出版业
                      </a>

                    </div>

                  </div>

                </div>
              </div>
              <!--注册资本-->
              <div class="btn-group mr50 regNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Zhuceziben"
              >
                <div class="point filter_btn">
                  <span class="c2">注册资本</span>
                  <span class="caret new-c1"></span>
                </div>
                <div class="regSubItem position-abs b-c-white new-border border-shadow" style="z-index: 100;width: 125px;">

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 filter-select"
                    >
                      全部
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/or0100?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      0万－100万
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/or100200?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      100万－200万
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/or200500?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      200万－500万
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/or5001000?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      500万－1000万
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/or1000?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      1000万以上
                    </a>
                  </div>

                </div>
              </div>
              <!--注册时间-->
              <div class="btn-group mr50 regTimeNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Zhuceshijian"
              >
                <div class="point filter_btn">
                  <span class="c2">注册时间 </span>
                  <span class="caret new-c1"></span>
                </div>
                <div class="timeSubItem position-abs b-c-white new-border border-shadow" style="z-index: 100;width: 125px;">

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 filter-select"
                    >
                      全部
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/oe01?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      成立1年内
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/oe015?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      成立1－5年
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/oe510?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      成立5－10年
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/oe1015?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      成立10－15年
                    </a>
                  </div>

                  <div class="pt8 pb8 pl10 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/oe15?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >
                      成立15年以上
                    </a>
                  </div>

                </div>
              </div>
              <!--企业状态-->
              <div class="btn-group mr50 statusNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Qiyezhuantai"
              >
                <div class="point filter_btn">
                  <span class="c2">企业状态</span>
                  <span class="caret new-c1"></span>
                </div>
                <div class="statusSubItem position-abs b-c-white new-border border-shadow"
                     style="z-index: 100;width: 80px;">

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 filter-select"
                    >全部</a>
                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/os1?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >在业</a>
                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/os2?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >存续</a>
                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/os3?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >吊销</a>
                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/os4?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >注销</a>
                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">
                    <a href="https://www.tianyancha.com/search/os5?key=%E6%96%B9%E5%BE%97"
                       class="cateName512 c2 "
                    >迁出</a>
                  </div>

                </div>
              </div>
            </div>
          </div>
          <!--高级筛选-->

          <div class="line_bottom ml30 mr30 pt15 pb15">
            <span class="f14 new-alert mr30">高级筛选</span>
            <div class="in-block">
              <!--联系电话-->
              <div class="btn-group mr50 phoneNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Lianxidianhua"
              >
                <div class="point filter_btn new-alert" is-need-state='true'>
                  联系电话
                  <span class="caret new-c1"></span>
                </div>
                <div class="phoneSubItem position-abs b-c-white new-border border-shadow"
                     style="z-index: 100;width: 105px;">

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512  point c2 filter-select"
                          onclick="searchNeedVip()">全部</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512  point c2 "
                          onclick="searchNeedVip()">有联系电话</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512  point c2 "
                          onclick="searchNeedVip()">无联系电话</span>

                  </div>

                </div>
              </div>
              <!--商标-->
              <div class="btn-group mr50 brandNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Shangbiao"
              >
                <div class="point filter_btn" is-need-state='true'>
                  商标
                  <span class="caret new-c1"></span>
                </div>
                <div class="brandSubItem position-abs b-c-white new-border border-shadow"
                     style="z-index: 100;width: 105px;">

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2 filter-select"
                          onclick="searchNeedVip()">全部</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2 "
                          onclick="searchNeedVip()">有商标</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2 "
                          onclick="searchNeedVip()">无商标</span>

                  </div>

                </div>
              </div>
              <!--专利-->
              <div class="btn-group mr50 patentNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Zhuanli"
              >
                <div class="point filter_btn" is-need-state='true'>
                  专利
                  <span class="caret new-c1"></span>
                </div>
                <div class="patentSubItem position-abs b-c-white new-border border-shadow"
                     style="z-index: 100;width: 105px;">

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2 filter-select "
                          onclick="searchNeedVip()">全部</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2  "
                          onclick="searchNeedVip()">有专利</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2  "
                          onclick="searchNeedVip()">无专利</span>

                  </div>

                </div>
              </div>
              <!--失信信息-->
              <div class="btn-group mr50 dishonestNowBox"
                   tyc-event-click tyc-event-ch="CompanySearch.Filter.Shixin"
              >
                <div class="point filter_btn" is-need-state='true'>
                  失信信息
                  <span class="caret new-c1"></span>
                </div>

                <div class="dishonestSubItem position-abs b-c-white new-border border-shadow"
                     style="z-index: 100;width: 105px;">

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2 filter-select "
                          onclick="searchNeedVip()">全部</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2  "
                          onclick="searchNeedVip()">有失信信息</span>

                  </div>

                  <div class="pt8 pb8 pl15 pr10 block border-shadow-hover">

                    <span class="cateName512 point c2  "
                          onclick="searchNeedVip()">无失信信息</span>

                  </div>

                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="mb15 text-center">
        <div class="in-block point pl15 pr15 pt2 pb2 b-c-subgray new-c2 new-border" id="searchTogal">
          <i class="fa fa-angle-up mr2 f14"></i>收起
        </div>
      </div>
    </div>





            <!--数据导出-->

            <div ng-if="!isTypeSearch&&(nodes | filter:{type:'1'}).length>0;">
              <div class="pl30 new-c1 b-c-subgray filter2017"
                   style="border-left: 1px solid #eee; border-right: 1px solid #eee;">
                <span
                  class="new-err f14 in-block vertival-middle pt15 pb15">2231</span>
                <span class="f14 in-block mr17 vertival-middle pt15 pb15">家相关公司</span>


                <span class="f12 in-block vertival-middle pt15 pb15">
                  普通用户可查看100家公司，
                  <a tyc-event-click tyc-event-ch="CompanySearch.Shuliang.VIP"
                     class="new-alert point" onclick="showVip()" target="_blank">升级成为VIP会员，可查看5000+家公司</a>
                </span>

                <span tyc-event-click tyc-event-ch="CompanySearch.DaoShuju"
                      is-need-state='true'
                      class="c-white f13 in-block float-right pl15 pr15 pt6 pb6 mt10 mb10 point vertival-middle mr30 "
                      style="background-color: #ff730c;"
                      onclick="searchOrder()">
                    导出联系方式
                </span>
                <div class="btn-group in-block phoneNowBox vertival-middle float-right pt10 mr15">
                  <div class="f13 pl10 pr5 pt6 pb6 b-c-white point new-border new-c3 "
                       is-need-state='true'>
                    <span class="overflow-width in-block vertival-middle"
                          style="width: 89px;">默认排序</span>
                    <span class="caret new-c1 vertival-middle"></span>
                  </div>
                  <div class="phoneSubItem position-abs b-c-white new-border border-shadow"
                       style="z-index: 100;width: 120px;">


                    <div class="pt8 pb8 pl15 pr10 block border-shadow-hover"
                         tyc-event-click tyc-event-ch="CompanySearch.Paixu.*"
                    >
                      <a class="cateName512  point new-c3 filter-select"
                         href="https://www.tianyancha.com/search?key=%E6%96%B9%E5%BE%97"
                         href-new-event event-name="筛选-排序">默认排序</a>
                    </div>

                    <div class="pt8 pb8 pl15 pr10 block border-shadow-hover"
                         tyc-event-click tyc-event-ch="CompanySearch.Paixu.1"
                    >
                      <a class="cateName512  point new-c3 "
                         href="https://www.tianyancha.com/search/ola1?key=%E6%96%B9%E5%BE%97"
                         href-new-event event-name="筛选-排序">注册资本降序</a>
                    </div>

                    <div class="pt8 pb8 pl15 pr10 block border-shadow-hover"
                         tyc-event-click tyc-event-ch="CompanySearch.Paixu.2"
                    >
                      <a class="cateName512  point new-c3 "
                         href="https://www.tianyancha.com/search/ola2?key=%E6%96%B9%E5%BE%97"
                         href-new-event event-name="筛选-排序">注册资本升序</a>
                    </div>

                    <div class="pt8 pb8 pl15 pr10 block border-shadow-hover"
                         tyc-event-click tyc-event-ch="CompanySearch.Paixu.3"
                    >
                      <a class="cateName512  point new-c3 "
                         href="https://www.tianyancha.com/search/ola3?key=%E6%96%B9%E5%BE%97"
                         href-new-event event-name="筛选-排序">注册时间降序</a>
                    </div>

                    <div class="pt8 pb8 pl15 pr10 block border-shadow-hover"
                         tyc-event-click tyc-event-ch="CompanySearch.Paixu.4"
                    >
                      <a class="cateName512  point new-c3 "
                         href="https://www.tianyancha.com/search/ola4?key=%E6%96%B9%E5%BE%97"
                         href-new-event event-name="筛选-排序">注册时间升序</a>
                    </div>

                  </div>
                </div>
              </div>
              <div class="row_hr">
                <hr>
              </div>
            </div>





    <div class="b-c-white search_result_container">

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="上海雷骊机电有限公司"
               src="https://img.tianyancha.com/logo/lll/836486d8560a810d8ec41dd772a21ad5.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/258898965" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">上海雷骊机电有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>上海
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="105.24335389525808 51.83627878423158"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">67</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">67</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="邹斌宏">邹斌宏</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="200万人民币">200万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2011-08-24 00:00:00.0">2011-08-24</span>
              </div>


              <div>
                <div class="add">
                  <span>商标信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="广州方得物流有限公司"
               src="https://img.tianyancha.com/logo/lll/bfef349c3e381270be6d863eb3cfedaa.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2333407233" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">广州<em>方得</em>物流有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>广东
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="94.2477796076938 62.83185307179587"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">60</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">60</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="涂松林">涂松林</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="500万人民币">500万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2014-07-25 00:00:00.0">2014-07-25</span>
              </div>


              <div>
                <div class="add">
                  <span>商标信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="慈溪市非非贸易有限公司"
               src="https://img.tianyancha.com/logo/lll/f6d7210d28487db159998834e6a8cd8e.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/56959741" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">慈溪市非非贸易有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>浙江
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="92.6769832808989 64.40264939859077"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">59</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">59</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="黄志平">黄志平</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="50.000000万人民币">50.000000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2014-04-17 00:00:00.0">2014-04-17</span>
              </div>


              <div>
                <div class="add">
                  <span>商标信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="北京一点得咨询有限公司"
               src="https://img.tianyancha.com/logo/lll/316fb8b1ffaa65d45dfb298710de1c37.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/10016633" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">北京一点得咨询有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>北京
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="86.39379797371932 70.68583470577035"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">55</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">55</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                开业
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="姚蔚">姚蔚</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="100 万元 人民币">100 万元 人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2009-04-14 00:00:00.0">2009-04-14</span>
              </div>


              <div>
                <div class="add">
                  <span>公司简称</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>网
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="北京方得机电有限公司"
               src="https://img.tianyancha.com/logo/lll/2a1e7d87f44acca2eb416de7ea18b753.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/6834173" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">北京<em>方得</em>机电有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>北京
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="83.25220532012952 73.82742735936014"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">53</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">53</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                开业
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="李国田">李国田</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="200 万人民币">200 万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2009-07-01 00:00:00.0">2009-07-01</span>
              </div>


              <div>
                <div class="add">
                  <span>商标信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="杭州方得投资管理有限公司"
               src="https://img.tianyancha.com/logo/lll/382a1ba77d41f2614c6ba2acc3aec244.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/1624424898" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">杭州<em>方得</em>投资管理有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>浙江
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="125.66370614359174 31.415926535897924"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">80</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">80</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="吴勃">吴勃</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="500.000000万人民币">500.000000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-06-23 00:00:00.0">2015-06-23</span>
              </div>


              <div>
                <div class="add">
                  <span>产品信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="辽宁方得技术有限公司"
               src="https://img.tianyancha.com/logo/lll/cd1f7491a2f7c3966d48c8dc942c3115.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/1185508244" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">辽宁<em>方得</em>技术有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>辽宁
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="150.79644737231007 6.2831853071795924"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">96</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">96</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="金雷">金雷</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="2000 万人民币">2000 万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-05-19 00:00:00.0">2015-05-19</span>
              </div>


              <div>
                <div class="add">
                  <span>网站名称</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    辽宁<em>方得</em>技术有限公司
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="河南省方得置业有限公司"
               src="https://img.tianyancha.com/logo/lll/b7441bfdf57a93854c268beb09f52c69.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/276313057" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">河南省<em>方得</em>置业有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>河南
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="135.0884841043611 21.991148575128555"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">86</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">86</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="白金增">白金增</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="1001万人民币">1001万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2010-01-12 00:00:00.0">2010-01-12</span>
              </div>


              <div>
                <div class="add">
                  <span>网站名称</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    河南省<em>方得</em>置业有限公司
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="上海阗鑫方得金融信息服务有限公司"
               src="https://img.tianyancha.com/logo/lll/665d612e01cdae49f5b92d0ced60388c.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/1220880034" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">上海阗鑫<em>方得</em>金融信息服务有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>上海
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="139.8008730847458 17.27875959474386"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">89</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">89</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="陈光熠">陈光熠</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="1000万人民币">1000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-06-30 00:00:00.0">2015-06-30</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="杭州方得智能科技有限公司"
               src="https://img.tianyancha.com/logo/lll/8826a977dbfb6e25bcc5da0e66eddba4.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2339758255" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">杭州<em>方得</em>智能科技有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>浙江
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="135.0884841043611 21.991148575128555"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">86</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">86</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="彭长书">彭长书</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="135.135000万人民币">135.135000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-05-18 00:00:00.0">2015-05-18</span>
              </div>


              <div>
                <div class="add">
                  <span>公司简称</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    <em>方得</em>智能
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="上海惟旭方得股权投资管理合伙企业（有限合伙）"
               src="https://img.tianyancha.com/logo/lll/62bbeb99a7f7dd4fb1d8bad383cbf0f4.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/531648796" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">上海惟旭<em>方得</em>股权投资管理合伙企业（有限合伙）</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>上海
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="142.94246573833559 14.137166941154065"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">91</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">91</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="祝毅">祝毅</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="-">-</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2011-08-19 00:00:00.0">2011-08-19</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="武汉方得教育咨询有限公司"
               src="https://img.tianyancha.com/logo/lll/a530056c5604bad68c73799dfc71e452.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2989636637" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">武汉<em>方得</em>教育咨询有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>湖北
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="131.94689145077132 25.132741228718352"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">84</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">84</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="王婷">王婷</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="1000万人民币">1000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2016-11-24 00:00:00.0">2016-11-24</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="辽宁方得物流有限公司"
               src="https://img.tianyancha.com/logo/lll/6e681faef0b4cfd4945570cd592c7dd7.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/1240862310" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">辽宁<em>方得</em>物流有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>辽宁
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="125.66370614359174 31.415926535897924"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">80</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">80</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="金雷">金雷</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="500 万人民币">500 万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-07-06 00:00:00.0">2015-07-06</span>
              </div>


              <div>
                <div class="add">
                  <span>股东信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    辽宁<em>方得</em>技术有限公司
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="福建盈方得投资管理有限公司"
               src="https://img.tianyancha.com/logo/lll/91d75e4f050e764839dbc5fb7edbacef.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2344038470" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">福建盈<em>方得</em>投资管理有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>福建
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="127.23450247038663 29.84513020910303"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">81</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">81</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="林大春">林大春</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="1000.000000万人民币">1000.000000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-06-05 00:00:00.0">2015-06-05</span>
              </div>


              <div>
                <div class="add">
                  <span>网站名称</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    盈<em>方得</em>投资
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="廊坊方得环保科技有限公司"
               src="https://img.tianyancha.com/logo/lll/828bb57a302c24b554732a3b1def68b5.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/1256047049" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">廊坊<em>方得</em>环保科技有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>河北
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="124.09290981679683 32.98672286269282"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">79</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">79</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="高海丛">高海丛</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="800万人民币">800万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2015-05-14 00:00:00.0">2015-05-14</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="西咸新区方得信息技术有限公司"
               src="https://img.tianyancha.com/logo/lll/770829ef270b01bc9643a3fc4b11b624.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2976247958" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">西咸新区<em>方得</em>信息技术有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>陕西
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="127.23450247038663 29.84513020910303"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">81</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">81</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="杨杰">杨杰</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="2000万人民币">2000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2016-12-06 00:00:00.0">2016-12-06</span>
              </div>


              <div>
                <div class="add">
                  <span>股东信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    辽宁<em>方得</em>技术有限公司
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="山西乐活方得科技有限公司"
               src="https://img.tianyancha.com/logo/lll/b762c94e27aeaa12fda26e3b9650be91.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/3023766528" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">山西乐活<em>方得</em>科技有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>山西
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="120.95131716320704 36.12831551628262"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">77</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">77</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="王岩刚">王岩刚</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="1000万人民币">1000万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2017-02-22 00:00:00.0">2017-02-22</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="广西方得科技有限公司"
               src="https://img.tianyancha.com/logo/lll/ae92b0c592b87d3b2799d1b816cc49d3.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2312476608" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">广西<em>方得</em>科技有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>广西
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="116.23892818282235 40.840704496667314"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">74</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">74</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="廖志屹">廖志屹</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="210万人民币">210万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2013-05-20 00:00:00.0">2013-05-20</span>
              </div>


            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="东莞方得电子商务有限公司"
               src="https://img.tianyancha.com/logo/lll/39dbb742cac010dc8e1ee91f20d17995.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2961039820" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">东莞<em>方得</em>电子商务有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>广东
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="117.80972450961724 39.269908169872416"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">75</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">75</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                存续
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="杨杰">杨杰</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="500万人民币">500万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2016-11-08 00:00:00.0">2016-11-08</span>
              </div>


              <div>
                <div class="add">
                  <span>股东信息</span>
                  <span>:</span>
                  <span
                    style=" max-width:500px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;display: inline-block;vertical-align: bottom">
                                                    辽宁<em>方得</em>技术有限公司
                                                </span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <div class="search_result_single search-2017 pb20 pt20 pl30 pr30">
        <div class="mr20 search_left_icon">
          <img alt="济南方得商贸有限公司"
               src="https://img.tianyancha.com/logo/lll/827bc1f8fc520d0a77e5ead5c5e28599.png@!watermark01"
               onerror="this.src='https://static.tianyancha.com/wap/images/logo327.png'">
        </div>
        <div class="search_right_item">
          <!--company name-->
          <div class="row pb10" style="margin-left: 0; margin-right: 0;">
            <div class="col-xs-10 search_repadding2 f18">
              <a href="https://www.tianyancha.com/company/2363043839" target='_blank'
                 tyc-event-click tyc-event-ch="CompanySearch.Company"
                 style="word-break: break-all;"
                 ng-click="$event.preventDefault();goToCompany(node.id,node.name,$index);inClick=true;"
                 class="query_name search-new-color sv-search-company">
                <span ng-class="inClick?'visited':''">济南<em>方得</em>商贸有限公司</span>
              </a>
            </div>
            <div class="search_base col-xs-2 search_repadding2 text-right c3 position-rel"
                 style="margin-top: 0;margin-bottom: 0;padding-right: 10px;">
              <i class="fa fa-map-marker c9" style="padding-right: 3px;"></i>山东
              <div class="notInIE8 position-abs" style="cursor: default; top: 20px;right: 0;">
                <svg class="score_line" width="54" height="54" viewbox="0 0 54 54">
        <defs>
            <!--2ec8db-->
            <linearGradient id="orange_red" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#2ec8db;"/>
                <stop offset="100%" style="stop-color:#2ec8db;"/>
            </linearGradient>
        </defs>
        <circle cx="27" cy="27" r="25" stroke-width="3" stroke="#F0F0F0" fill="none"></circle>


        <circle cx="27" cy="27" r="25" stroke-width="2" stroke="url(#orange_red)" fill="none" transform="matrix(0,-1,1,0,0,54)" stroke-dasharray="114.66813185602746 42.41150082346221"></circle>
        <text x="27" y="28" text-anchor="middle" fill="#009bae" font-size="18">73</text>
        <text x="27" y="40" text-anchor="middle" fill="#6D6D6D" font-size="11">评分</text>
    </svg>
              </div>
              <div class="scoreV4">
                <img alt="评分" src="https://static.tianyancha.com/wap/images/scoreV3.png">
                <div class="content">
                  <span class="t1">73</span> <span class="t2">评分</span>
                </div>
              </div>
              <div class="position-abs statusTypeNor statusType1" style="top:36px;right: 85px;">
                在营
              </div>
            </div>
          </div>
          <div>

          </div>
          <!--body-->
          <div class="row" style="margin-left: 0; margin-right: 0;">
            <div class="search_row_new">
              <div class="title overflow-width" style="padding-left: 0;">
                法定代表人：
                <span
                  title="野源">野源</span>
              </div>
              <div class="title overflow-width">
                注册资本：<span
                  title="200万人民币">200万人民币</span>
              </div>
              <div class="title overflow-width" style="border-right: none">
                注册时间：<span
                  title="2016-03-16 00:00:00.0">2016-03-16</span>
              </div>


            </div>
          </div>
        </div>
      </div>

    </div>






            <!--其他tab搜索结果-->


            <!--翻页-->








    <div class="company_pager ng-scope in-block">
      <ul class="pagination-sm pagination ng-isolate-scope ng-valid ng-dirty ng-valid-parse" boundary-links="false"
          rotate="false" style="float: left;">






        <li class="pagination-prev ng-scope disabled">
          <a

            class="ng-binding">
            &lt;
          </a>
        </li>







        <li class="pagination-page ng-scope active ">
          <a

            class="ng-binding">
            1
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p2?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            2
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p3?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            3
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p4?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            4
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p5?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            5
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p6?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            6
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p7?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            7
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p8?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            8
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p9?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            9
          </a>
        </li>

        <li class="pagination-page ng-scope  ">
          <a

            href="https://www.tianyancha.com/search/p10?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">
            10
          </a>
        </li>



        <li class="pagination-page ng-scope" style=""><a

            href="https://www.tianyancha.com/search/p11?key=%E6%96%B9%E5%BE%97"

            class="ng-binding ng-click-active">...</a></li>


        <li class="pagination-next ng-scope "><a

            href="https://www.tianyancha.com/search/p2?key=%E6%96%B9%E5%BE%97"

            class="ng-binding">&gt;</a></li>
      </ul>
      <div class="total ng-binding">
        <span>共</span>
        112
        <span>页</span>
      </div>
    </div>




            <div onclick="xiaolingFind();" class="xiaolingfind">
              <div style="height: 30px;" class="float-right">
                <div style="line-height: 1.6;" class="c8 in-block vertival-middle f13">没有想要的查询结果？</div>
                <div class="f14 deepsearch in-block vertival-middle">
                  <i class="fa fa-search"></i><span>深度搜索</span>
                </div>
              </div>
            </div>

            <div class="f12 team-left mb20">
              <span class="point new-alert" onclick="showVip()">升级成为VIP会员,可查看多达5000条相关结果</span>
            </div>


          </div>
          <!-- end main -->
          <!-- right -->
          <div class="col-3 text-center pt10"
               style="padding-left: 0; padding-right: 0;">
            <div class="banner position-relative">
      <a href="/vipintro" href-event event-name="VIP广告"
         tyc-event-click tyc-event-ch="CompangyDetail.Right.VIP"
         style="display: block;" target="_blank"  >
        <img src="https://static.tianyancha.com/wap/images/guanggaoVIP.png" style="width: 100%;" alt="vip">
      </a>
      <a href="https://www.tianyancha.com/invite"
         tyc-event-click tyc-event-ch="CompangyDetail.Right.XDL"
         target="_blank"  style="display: block;" class="mt10">
        <img src="https://static.tianyancha.com/wap/images/guanggaoApp726.jpg" style="width: 100%" alt="app下载"/>
      </a>
    </div>
          </div>
          <!-- end right -->
        </div>
      </div>
    </div>

      <div class="backToTop backTopPc backTopPcNew point" >
    	<div class="backtop_zd" onclick="backToTop.backToTop()"></div>
    	<div class="backtop_fk" onclick="backToTop.feedback();"></div>
      <div class="backtop_app" onclick="backToTop.toApp();"></div>
    	<div class="backtop_wx"  onmouseover="common.mouseShowBySelElem('.wxcontent')" onmouseleave="common.mouseHideBySelElem('.wxcontent')">
    	</div>
    	<div  class="wxcontent collapse"></div>
    </div>
      <div class="new-foot-v1 position-rel ng-isolate-scope c-white"
         style="bottom: 0px;background-color:#13326d;
         height: 345px;width:100%;"
         new-foot="">
      <div class="mainv2_tab_new"
           style="width:100%;background:transparent;padding-top:50px;opacity:0.8;filter:alpha(opacity=80)">
        <div class="container company_container" style="padding:0 0 0 0px">
          <div style="padding-left:0;padding-right:0;padding-bottom:0px">
            <div class="col-9" style="padding-left:0;padding-right:0">
              <div class="foot1" style="border-right: 1px solid rgba(255,255,255,0.4)">
                <div class="footer_images footer_images_logo"></div>
                <div class="text" style="padding-bottom:0px;padding-top: 14px">
                  <div style="padding-bottom:6px"><a href="https://www.tianyancha.com/property/1" style="padding-right:26px"
                                                     class="c-white" target="_blank">关于我们</a> <a
                      href="https://www.tianyancha.com/property/3" class="c-white" target="_blank">版权政策</a></div>
                  <div style="padding-bottom:6px"><a href="https://www.tianyancha.com/property/2" style="padding-right:26px"
                                                     class="c-white" target="_blank">服务协议</a> <a
                      href="https://www.tianyancha.com/property/4" class="c-white" target="_blank">免责声明</a></div>
                  <div>
                    <a href="https://www.tianyancha.com/property/5" style="padding-right:26px" class="c-white" target="_blank">权利通知</a>
                    <a href="http://open.tianyancha.com" style="padding-right:26px" class="c-white" target="_blank">数据服务</a>
                  </div>
                  <div class="pt5">
                    <a href="https://www.tianyancha.com/business" style="padding-right:26px" class="c-white" target="_blank">商务通道</a>
                  </div>
                </div>
              </div>
              <div class="foot2">
                <div class="text"><span class="c-white" style="margin-top: 12px">联系我们</span> <span class="c-white"><i
                      class="fa fa-phone"></i>电话 : 400-871-6266 [工作日: 9:00-18:30 ]</span> <span class="c-white"><i
                      class="fa fa-user"></i>在线客服 : <a href="http://q.url.cn/s/tWKXe2m?_type=wpa" class="c-white"
                                                       nofollow
                                                       target="_blank">2852375336</a></span> <span class="c-white"><i
                      class="fa fa-envelope"></i>商务合作 : bd@tianyancha.com</span>
                </div>
              </div>
              <div class="foot3" style="border-right:none"><a class="c-white footer_images footer_images_complaint"
                                                              onclick="footer.openComplaint()"
                                                              style="cursor:pointer;margin-bottom:15px;margin-top:0px">
                  <div></div>
                  投诉</a> <a class="c-white footer_images footer_images_wapqq" href="http://q.url.cn/s/tWKXe2m?_type=wpa"
                            nofollow
                            target="_blank" style="margin-bottom:15px;margin-top:0px">
                  <div></div>
                  在线咨询</a> <a class="c-white footer_images footer_images_weibo" href="http://weibo.com/tianyancha"
                              nofollow
                              target="_blank" style="margin-bottom:5px">
                  <div></div>
                  新浪微博</a>
              </div>
              <div class="foot4" style="border-left: 1px solid rgba(255,255,255,0.4)">
                <div class="c-white">数据来源</div>
                <div class="c-white"><span></span>全国企业信用信息公示系统</div>
                <div class="c-white"><span></span>中国裁判文书网</div>
                <div class="c-white"><span></span>中国执行信息公开网</div>
              </div>
              <div class="foot5">
                <div class="c-white"><span></span>国家知识产权局</div>
                <div class="c-white"><span></span>商标局</div>
                <div class="c-white"><span></span>版权局</div>
              </div>
            </div>
            <div class="col-3">
              <div class="text-right">
                <div class="right_item text-center" style="margin-right:34px">
                  <div style="color:#fff">微信公众号</div>
                  <img src="https://static.tianyancha.com/wap/images/wechat_foot.png" alt="微信公众号"></div>
                <div class="right_item text-center">
                  <div style="color:#fff">天眼查APP</div>
                  <img src="https://static.tianyancha.com/wap/images/footer_download.png" style="width: 84px"
                       alt="天眼查APP"
                  ></div>
              </div>
            </div>
          </div>
        </div>
        <div class="company_container friend_link f12 mt60 pt15" style="border-top:1px solid rgba(255,255,255,0.4)"><span>友情链接：</span>
          <a href="http://www.baike.com/" nofollow target="_blank" class="c-white">互动百科</a></div>
      </div>
      <div class="position-abs over-hide f12 pb10 pt10"
           style="left: 0;right: 0;bottom: 0;color: #405e97;background-color: #0d234d;">
        <div class="company_container margin-auto">
          <span>版权所有：北京金堤科技有限公司</span>
          <span>©2015 JINDIDATA 京ICP备14061319</span>
          <span class="pl10">固定电话：400-871-6266</span>
          <div class="float-right">
            <div
              class="footer_images footer_images_beian">
              <img alt="." src="https://img2.tianyancha.com/beianicon.gif?_t=1501160364448">
            </div>
            <span>京公网安备 11010802021795号</span>
          </div>
          <div>地址：北京市海淀区知春路63号中国卫星通信大厦B座23层</div>

        </div>
      </div>

    </div>
    </div>
    <div id="banner_web"></div>
    <script>
      var gdt_tracker = gdt_tracker || [];
      gdt_tracker.push(["set_source_id", "33937"]);
      (function () {
        var userAgent = navigator.userAgent;
        if (userAgent.indexOf('ignore') < 0) {
          var doc = document, h = doc.getElementsByTagName("head")[0], s = doc.createElement("script");
          s.async = true;
          s.src = "https://qzs.qq.com/qzone/biz/res/gt.js";
          h && h.insertBefore(s, h.firstChild)
        }
      })();
    </script>
    <script>

      var _hmt = _hmt || [];
      (function () {
        var userAgent = navigator.userAgent;
        if (userAgent.indexOf('ignore') < 0) {
          var hm = document.createElement("script");
          hm.src = "//hm.baidu.com/hm.js?e92c8d65d92d534b0fc290df538b4758";
          var s = document.getElementsByTagName("script")[0];
          s.parentNode.insertBefore(hm, s);
        }
      })();

    </script>
    <script>

      (function(){
        var bp = document.createElement('script');
        var curProtocol = window.location.protocol.split(':')[0];
        if (curProtocol === 'https') {
          bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
        }
        else {
          bp.src = 'http://push.zhanzhang.baidu.com/push.js';
        }
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(bp, s);
      })();

    </script>
    </body>
    </html>"""
    return data

