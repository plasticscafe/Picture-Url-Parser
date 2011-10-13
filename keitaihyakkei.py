# -*- coding: utf-8 -*-
########################################
import re
# 携帯百景
pattern = re.compile("http://movapic.com/pic/(\w+)/")
def search(text):
    result = []
    items = pattern.findall(text)
    sizes = [
        's_',
        't_',
    ]
    for item in items:
        for size in sizes:
            result.append('http://movapic.com/pic/' + size + str(item) + '.jpeg')
    return result
