# -*- coding: utf-8 -*-
########################################
import re
# img.ly
pattern = re.compile("http://img.ly/(\w+)")
def search(text):
    result = []
    items = pattern.findall(text)
    urls = [
        'http://img.ly/show/thumb/',
        'http://img.ly/show/mini/',
    ]
    for item in items:
        for url in urls:
            result.append(url + str(item))
    return result
