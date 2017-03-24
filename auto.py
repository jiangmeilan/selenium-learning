import unittest
from widget import Widget

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def test_widget_size(self):
        self.assertEqual(self.widget.getSize(), (40, 40))

    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))

    def tearDown(self):
        self.widget = None

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_widget_size'))
    suite.addTest(WidgetTestCase('testResize'))
    return suite

'''
def suite():
    return unittest.makeSuite(WidgetTestCase,'test')


if __name__ == '__main__':
    unittest.main(defaultTest = 'suite')

'''


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_widget_size'))
    suite.addTest(WidgetTestCase('testResize'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
