# coding=utf-8

results = []

a = 1


def get_new_result():
    new_res = results.pop()
    return new_res


def has_new_result():
    return len(results) != 0


def add_new_result(res):

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
        results.append(l)



