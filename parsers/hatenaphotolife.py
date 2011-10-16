# -*- coding: utf-8 -*-
########################################
import re
# はてなフォトライフ
pattern = re.compile("http://f.hatena.ne.jp/((\w{1})\w+)/((\d{8})\d{6})")
def search(text):
    result = []
    items = pattern.findall(text)
    sizes = [
        '',
        '_120',
        '_m',
    ]
    for item in items:
        for size in sizes:
            url = 'http://img.f.hatena.ne.jp/images/fotolife/'
            url += str(item[1]) + '/'
            url += str(item[0]) + '/'
            url += str(item[3]) + '/'
            url += str(item[2]) + size + '.jpg'
            result.append(url)
    return result
