# -*- coding: utf-8 -*-
########################################
import re
# Mobypicture
pattern = re.compile("http://moby.to/(\w+)/")
def search(text):
    result = []
    items = pattern.findall(text)
    sizes = [
        ':medium',
        ':square',
        ':small',
        ':thumbnail',
    ]
    for item in items:
        for size in sizes:
            result.append('http://moby.to/' + str(item) + size)
    return result
