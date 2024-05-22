import time
import unittest
import requests


class DC(unittest.TestCase):
    userid1='439541276'
    sid1='V02SYHsPw9uZS6Uk7Ft6-mvHPUDbl-Q00a5b7afa001a32de1c'
    host='http://note-api.wps.cn'

    #获取分组后清除分组
    def group_clear(self,sid,user_id):
        """ 获取当前用户有效分组"""
        #新建便签分组
        url=self.host+'/v3/notesvr/get/notegroup'

        headers={
            'Cookie':f'wps_sid={self.sid1}',
            'X-user-key':f'{self.userid1}'
        }
        data={"excludeInvalid":False}
        get_res=requests.post(url,headers=headers,json=data)
        print(len(get_res.json()['noteGroup']))
        for group in get_res.json()['noteGroup']:
            group_id=group['groupId']
            #删除分组
            del_url='https://note-api.wps.cn/notesvr/delete/notegroup'
            data={
                'groupId':group_id
            }
            del_res=requests.post(url=del_url,headers=headers,json=data)
            print(del_res.status_code)
            if del_res.status_code!=200:
                return False
        return True