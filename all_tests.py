# -*- coding:utf-8 -*-
import time, unittest, HTMLTestRunner
listaa = 'C:\\Users\\lanlan\\Desktop\\12-30\\desk\\test_case\\'
def creatsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa, pattern = 'start*', top_level_dir=None)
    print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit
alltestnames = creatsuite()

now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
filename = 'C:\Users\lanlan\Desktop\\12-30\desk\\' + now + '-report.html'
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = u'综合测试', description = u'用例执行情况')
runner.run(alltestnames)

