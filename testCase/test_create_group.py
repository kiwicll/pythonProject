import time
import unittest
import requests
import business.dataClear
from common.logsMethod import class_case_log


@class_case_log
class NoteGroupAPITest(unittest.TestCase):
    userid1='439541276'
    sid1='V02SYHsPw9uZS6Uk7Ft6-mvHPUDbl-Q00a5b7afa001a32de1c'
    host='http://note-api.wps.cn'

    def setUp(self):
        #前置步骤：数据清除无效分组
        self.DC.group_clear(sid=self.userid1,user_id=self.userid1)

    def test_set_note_groups(self):
        """ 新建分组列表的主流程"""
        #新建便签分组
        set_group_url=self.host+'/v3/notesvr/set/notegroup'

        headers={
            'Cookie':f'wps_sid={self.sid1}',
            'X-user-key':f'{self.userid1}'
        }
        group_id=str(int(time.time()*1000))+'_groupId'
        body={
            'groupId':group_id,
            'groupName':'test分组1',
            'order':0
        }
        res=requests.post(url=set_group_url,headers=headers,json=body)
        self.assertEqual(200,res.status_code)

