# -*- coding: utf-8 -*-
########################################
# http://blog.irons.jp/2009/12/23/twitter_thumb_url/
#
# フォト蔵
# twitpic
# Mobypicture
# yFrog
# 携帯百景
# はてなフォトライフ
# PhotoSHare  TODO: 短縮URL
# img.ly
# Twitgoo
# imgur
# Lockers
# Instgram
#########################################

funcs = []
#########################################
# Parser for Services
#########################################
"""
import photozo
funcs.append(photozo.search)
import twitpic
funcs.append(twitpic.search)
import mobypicture
funcs.append(mobypicture.search)
import yfrog
funcs.append(yfrog.search)
import keitaihyakkei
funcs.append(keitaihyakkei.search)
import hatenaphotolife
funcs.append(hatenaphotolife.search)
import photoshare
funcs.append(photoshare.search)
import imgly
funcs.append(imgly.search)
import twitgoo
funcs.append(twitgoo.search)
import imgur
funcs.append(imgur.search)
import lockers
funcs.append(lockers.search)
import instgram
funcs.append(instgram.search)
"""
import parsers
from parsers import * 
for parser in parsers.__all__:
    funcs.append(eval(parser + '.search'))

#########################################
# Interface
#########################################
def get(text):
    res = []
    for func in funcs:
        urls = func(text)
        if 0 < len(urls):
            res.append(urls[0])
    return res
 
def get_all(text):
    res = []
    for func in funcs:
        urls = func(text)
        if 0 < len(urls):
            res.append(urls)
    return res
        
