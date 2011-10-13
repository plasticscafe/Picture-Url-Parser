# -*- coding: utf-8 -*-
########################################
import re
# yfrog
pattern = re.compile("http://yfrog.com/(\w+)/")
def search(text):
    result = []
    items = pattern.findall(text)
    for item in items:
        result.append('http://yfrog.com/' + str(item) + '.th.jpg')
    return result
