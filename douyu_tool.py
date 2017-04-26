# coding: utf-8

import requests
import json
from fcookie import fcookie

def get_douyu_watch_history(cookie):
    url = 'https://www.douyu.com/member/cp/get_user_history'
    r = requests.get(url, cookies=fcookie(cookie), verify=False)
    info_list = json.loads(r.content)['history_list']
    nowtime = json.loads(r.content)['nowtime']
    for i in info_list:
        print i['on']
        print i['n']
        print str((nowtime - int(i['lt'])) / 60) + '分钟前'
        print '------------'

get_douyu_watch_history(cookie)
