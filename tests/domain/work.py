import unittest
from core.domain.work import Work


class TestWork (unittest.TestCase):

    TITLE = 'Title 1'
    ISWC = 'iswc'
    SOURCE = 'source'
    ID = 9999
    WORK_CLASSNAME = 'Work'

    _work = None

    def setUp(self):
        self._work = Work(self.TITLE, [], self.ISWC,  self.SOURCE, self.ID)

    def testItReturnsValidWork(self):
        self.assertEqual(self._work.__class__.__name__, self.WORK_CLASSNAME)

    def testItReturnsValidWorkTitle(self):
        self.assertEqual(self.TITLE, self._work.title())

    def testItReturnsValidWorkIswc(self):
        self.assertEqual(self.ISWC, self._work.iswc())

    def testItReturnsValidWorkSource(self):
        self.assertEqual(self.SOURCE, self._work.source())

    def testItReturnsValidWorkId(self):
        self.assertEqual(self.ID, self._work.id())
