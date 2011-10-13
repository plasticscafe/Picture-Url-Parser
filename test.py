# -*- coding: utf-8 -*-
########################################
# http://blog.irons.jp/2009/12/23/twitter_thumb_url/
#
#########################################

#########################################
# unit test data
#########################################
test_datas = [
    # フォト蔵
    {
        'url':'http://photozou.jp/photo/show/784/17561757',
        'result':[
            'http://photozou.jp/p/img/17561757',
            'http://photozou.jp/p/thumb/17561757',
        ]
    },
    # twitpic
    {
        'url':'http://twitpic.com/6rqkel',
        'result':[
            'http://twitpic.com/show/thumb/6rqkel',
            'http://twitpic.com/show/mini/6rqkel',
        ]
    },
    # Mobypicture
    {
        'url':'http://moby.to/6rqkel/',
        'result':[
            'http://moby.to/6rqkel:medium',
            'http://moby.to/6rqkel:square',
            'http://moby.to/6rqkel:small',
            'http://moby.to/6rqkel:thumbnail',
        ]
    },
    # yFrog
    {
        'url':'http://yfrog.com/6rqkel/',
        'result':[
            'http://yfrog.com/6rqkel.th.jpg',
        ]
    },
    # 携帯百景
    {
        'url':'http://movapic.com/pic/6rqkel/',
        'result':[
            'http://movapic.com/pic/s_6rqkel.jpeg',
            'http://movapic.com/pic/t_6rqkel.jpeg',
        ]
    },
    # はてなフォトライフ
    {
        'url':'http://f.hatena.ne.jp/kakifurai/20110624001001',
        'result':[
            'http://img.f.hatena.ne.jp/images/fotolife/k/kakifurai/20110624/20110624001001.jpg',
            'http://img.f.hatena.ne.jp/images/fotolife/k/kakifurai/20110624/20110624001001_120.jpg',
            'http://img.f.hatena.ne.jp/images/fotolife/k/kakifurai/20110624/20110624001001_m.jpg',
        ]
    },
    # PhotoSHare
    # TODO: 短縮URL
    {
        'url':'http://www.bcphotoshare.com/photos/564683/3200644',
        'result':[
            'http://images.bcphotoshare.com/storages/3200644/large.jpg',
            'http://images.bcphotoshare.com/storages/3200644/thumb180.jpg',
            'http://images.bcphotoshare.com/storages/3200644/thumbnail.jpg',
            'http://images.bcphotoshare.com/storages/3200644/thumb68.jpg',
        ]
    },
    # img.ly
    {
        'url':'http://img.ly/8VbD',
        'result':[
            'http://img.ly/show/thumb/8VbD',
            'http://img.ly/show/mini/8VbD',
        ]
    },
    # Twitgoo
    {
        'url':'http://twitgoo.com/4kv9j7',
        'result':[
            'http://twitgoo.com/show/img/4kv9j7',
            'http://twitgoo.com/show/mini/4kv9j7',
            'http://twitgoo.com/show/thumb/4kv9j7',
        ]
    },
    # imgur
    {
        'url':'http://imgur.com/4nwRA',
        'result':[
            'http://i.imgur.com/4nwRAl.jpg',
            'http://i.imgur.com/4nwRAs.jpg',
        ]
    },
    # Lockers
    {
        'url':'http://lockerz.com/s/143934392',
        'result':[
            'http://api.plixi.com/api/TPAPI.svc/imagefromurl?size=big&url=http://lockerz.com/s/143934392',
            'http://api.plixi.com/api/TPAPI.svc/imagefromurl?size=medium&url=http://lockerz.com/s/143934392',
            'http://api.plixi.com/api/TPAPI.svc/imagefromurl?size=mobile&url=http://lockerz.com/s/143934392',
            'http://api.plixi.com/api/TPAPI.svc/imagefromurl?size=samll&url=http://lockerz.com/s/143934392',
            'http://api.plixi.com/api/TPAPI.svc/imagefromurl?size=thumbnail&url=http://lockerz.com/s/143934392',
        ]
    },
    # Instgram
    {
            'url':'http://instagr.am/p/EiMN/',
        'result':[
            'http://instagr.am/p/EiMN/media/?size=l',
            'http://instagr.am/p/EiMN/media/?size=m',
            'http://instagr.am/p/EiMN/media/?size=t',
        ]
    },
]

import imageurl
for data in test_datas:
    res = imageurl.get_all(data['url'])
    num = len(res)
    for i in range(num):
        if res[0][i] != data['result'][i]:
            print "error: " + res[0][i] + " : " + data['result'][i]




