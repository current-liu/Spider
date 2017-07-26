# coding=utf-8

import random


class RandomUserAgentMiddleware(object):
    @classmethod
    def process_request(cls, request, spider):
        user_agent = random.choice(spider.settings['USER_AGENT_LIST'])
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
