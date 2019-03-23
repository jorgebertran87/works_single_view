import unittest


class TestTitle (unittest.TestCase):

    VALUE = 'Title 1'
    TITLE_CLASSNAME = 'Title'

    _title = None

    def setUp(self):
        self._title = Title(self.VALUE)

    def testItReturnsValidTitle(self):
        self.assertEqual(self._title.__class__.__name__, self.TITLE_CLASSNAME)

    def testItReturnsValidTitleValue(self):
        self.assertEqual(self.VALUE, self._title.value())
