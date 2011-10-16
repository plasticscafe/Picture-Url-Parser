# -*- coding: utf-8 -*-
########################################
import re
# Lockers
pattern = re.compile("http://lockerz.com/s/(\d+)")
def search(text):
    result = []
    items = pattern.findall(text)
    sizes = [
        'big',
        'medium',
        'mobile',
        'small',
        'thumbnail',
    ]
    for item in items:
        for size in sizes:
            url = 'http://api.plixi.com/api/TPAPI.svc/imagefromurl?size='
            url += size + '&url=http://lockerz.com/s/' +  str(item)
            result.append(url)
    return result
