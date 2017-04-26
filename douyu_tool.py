# coding: utf-8

import requests
import json
from fcookie import fcookie

cookie = 'acf_devid=fb8e615b5b265f6df5e95da88807107b; PHPSESSID=vcbkdakk2lu6d3maose61qmkn0; acf_auth=21e981DmQ39ZqRg1FYAg%2FuybxS%2BPlzsEU7yXe%2F7%2FaCDxkt3d1SLf%2F06zXeUfCAeh0vwUm0WODfwqrMAK8ZIMi2JNpVEffS7BpEcWGu%2BTMU%2Bpt8QPiQQBe2Y; wan_auth37wan=6a67c937a525JWNAysgjvWzwNyifFrkzsL6BX3NqCHC5fqHbhF%2Fi9mp6yFreXqYGe%2BOVmC4Q4GDxdUKWK3WxbpMgjY6j1xJY6r%2Begy1mVITeJ1W2; acf_uid=1609995; acf_username=qq_BdRXuxgi; acf_nickname=cccccelery; acf_own_room=1; acf_groupid=1; acf_phonestatus=1; acf_avatar=https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar%2F001%2F60%2F99%2F95_avatar_; acf_ct=0; acf_ltkid=16740576; acf_biz=1; acf_stk=791ba929ea66967c; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1492820912,1492994544,1493084247,1493167701; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1493167703; _dys_lastPageCode=page_home,page_home; _dys_refer_action_code=show_page_staydur'

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