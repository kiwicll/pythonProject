import unittest
import requests
def output_check(self,expect,actual):
    """

    :param self:
    :param expect: 描述断言的期望值，以object结构描述出期望值，支持动态值的校验和精准值的校验
    :param actual: 描述断言的实际结果 字典接口的json字符串，一般来说指的是response.json()
    :return:
    """
    self.assertEqual(len(expect.key()),len(actual.key()),msg='keys len error')
    for k,v in expect.items():
        self.assertIn(k,actual.key(),msg=f'expect key【{k}】 not in response!')
        if isinstance(v,type):
            self.assertEqual(v,type(actual[k]),msg=f'key:【{k}】 type error!')
        elif isinstance(v,dict):
            #递归
            self.output_check(v,actual[k])
        elif isinstance(v, list):
            self.assertEqual(len(v),len(actual[k]), msg=f'key:【{k}】 len error!')
            for i in  range(len(v)):
                if isinstance(v[i],type):
                    self.assertEqual(v[i],type(actual[k][i]),msg=f'list value:【{v[i]}】 type error!')
                elif isinstance(v[i],dict):
                    self.output_check(v[i],actual[k][i])
                else:
                    self.assertEqual(v[i],actual[k][i],msg=f'list value:【{v[i]}】 value error!')