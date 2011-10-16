# -*- coding: utf-8 -*-
########################################
import re
# フォト蔵
pattern = re.compile("http://photozou\.jp/photo/show/\d+/(\d+)")
def search(text):
    result = []
    items = pattern.findall(text)
    urls = [
        'http://photozou.jp/p/img/',
        'http://photozou.jp/p/thumb/'
    ]
    for item in items:
        for url in urls:
            result.append(url + str(item))
    return result
