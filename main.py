import unittest
import os
from BeautifulReport import BeautifulReport

DIR = os.path.dirname(os.path.abspath(__file__))
ENVIRON ='Online'#online-线上环境，offline-测试环境

if __name__ == '__main__':
    run_pattern ='all' #all全量测试用例执行 smoking冒烟测试执行 指定执行文件
    if run_pattern=='all':
        pattern='test_*.py'
    elif run_pattern == 'smoking':
        pattern ='test_major*.py'
    else:
        run_pattern=run_pattern+'.py'
    suite =unittest.TestLoader().discover('./testCase',pattern=run_pattern)

    result= BeautifulReport(suite)
    result.report(filename="report.html",description='测试报告',report_dir='./')
