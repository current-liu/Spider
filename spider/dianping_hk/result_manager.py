# coding=utf-8

hotel_review_results = []
attraction_review_results = []




def get_new_hotel_review_result():
    new_res = hotel_review_results.pop()
    return new_res


def has_new_hotel_review_result():
    return len(hotel_review_results) != 0


def add_new_hotel_review_result(res):

    # results = results + res
    # 为啥错了 新声明的局部变量覆盖了全局变量，而还没有初始化的时候无法引用
    pass

    shopIds = res[0]
    review_ids = res[1]
    user_ids = res[2]
    reviewStars = res[3]
    rooms = res[4]
    locs = res[5]
    services = res[6]
    healths = res[7]
    facs = res[8]
    comment_txts = res[9]
    create_times = res[10]
    likes = res[11]
    reply_nums = res[12]
    for (q,w,e,r,t,y,u,i,o,p,a,s,d) in zip(shopIds, review_ids, user_ids, reviewStars, rooms, locs,
                                                            services, healths, facs, comment_txts,
                                                            create_times, likes, reply_nums):
        l = [q,w,e,r,t,y,u,i,o,p,a,s,d]
        hotel_review_results.append(l)
# ------------------------------------------------------------------------------------------------------


def get_new_attraction_review_result():
    new_res = attraction_review_results.pop()
    return new_res


def has_new_attraction_review_result():
    return len(attraction_review_results) != 0


def add_new_attraction_review_result(res):

    # results = results + res
    # 为啥错了 新声明的局部变量覆盖了全局变量，而还没有初始化的时候无法引用
    pass

    shopIds = res[0]
    review_ids = res[1]
    user_ids = res[2]
    reviewStars = res[3]

    items = res[4]
    foods = res[5]
    huasuans = res[6]
    prices = res[7]

    comment_txts = res[8]
    create_times = res[9]
    likes = res[10]
    reply_nums = res[11]
    for (q,w,e,r,t,y,u,i,o,p,a,s) in zip(shopIds, review_ids, user_ids, reviewStars, items, foods,
                                                            huasuans, prices,  comment_txts,
                                                            create_times, likes, reply_nums):
        l = [q,w,e,r,t,y,u,i,o,p,a,s]
        attraction_review_results.append(l)



