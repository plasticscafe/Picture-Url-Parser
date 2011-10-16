# -*- coding: utf-8 -*-
########################################
import re
# Instgram
pattern = re.compile("http://instagr.am/p/(\w+)/")
def search(text):
    result = []
    items = pattern.findall(text)
    sizes = [
        'l',
        'm',
        't',
    ]
    for item in items:
        for size in sizes:
            result.append('http://instagr.am/p/' + str(item) + '/media/?size=' + size)
    return result
