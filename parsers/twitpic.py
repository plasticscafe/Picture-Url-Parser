# -*- coding: utf-8 -*-
########################################
import re
# twitpic
pattern = re.compile("http://twitpic.com/(\w+)")
def search(text):
    result = []
    items = pattern.findall(text)
    urls = [
        'http://twitpic.com/show/thumb/',
        'http://twitpic.com/show/mini/',
    ]
    for item in items:
        for url in urls:
            result.append(url + str(item))
    return result
