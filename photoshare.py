# -*- coding: utf-8 -*-
########################################
import re
# PhotoShare
pattern = re.compile("http://www.bcphotoshare.com/photos/\w+/(\w+)/")
def search(text):
    result = []
    items = pattern.findall(text)
    sizes = [
        'large',
        'thumb180',
        'thumbnail',
        'thumb68',
    ]
    for item in items:
        for size in sizes:
            result.append('http://images.bcphotoshare.com/storages/' + str(item) + '/' + size + '.jpg')
    return result
