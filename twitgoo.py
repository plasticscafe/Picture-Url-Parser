# -*- coding: utf-8 -*-
########################################
import re
# Twitgoo
pattern = re.compile("http://twitgoo.com/(\w+)")
def search(text):
    result = []
    items = pattern.findall(text)
    urls = [
        'http://twitgoo.com/show/img/',
        'http://twitgoo.com/show/mini/',
        'http://twitgoo.com/show/thumb/',
    ]
    for item in items:
        for url in urls:
            result.append(url + str(item))
    return result
