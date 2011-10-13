# -*- coding: utf-8 -*-
########################################
import re
# imgur
pattern = re.compile("http://imgur.com/(\w+)")
def search(text):
    result = []
    items = pattern.findall(text)
    sizes = [
        'l',
        's',
    ]
    for item in items:
        for size in sizes:
            result.append('http://i.imgur.com/' + str(item) + size + '.jpg')
    return result
