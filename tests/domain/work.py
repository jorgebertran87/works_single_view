import unittest


class TestWorks (unittest.TestCase):

    TITLE = 'Title 1'
    ISWC = 'iswc'
    SOURCE = 'source'
    ID = 9999

    _work = None

    def setUp(self):
        self._work = Work(TITLE, [], ISWC,  SOURCE, ID)

    def testItReturnsValidWork(self):
        
        self.assertEqual(self._work.__class__.__name__, 'Work')

    def testItReturnsValidWorkTitle(self):
        self.assertEqual(TITLE, self._work.title())

    def testItReturnsValidWorkIswc(self):
        self.assertEqual(ISWC, self._work.iswc()) 

    def testItReturnsValidWorkSource(self):
        self.assertEqual(SOURCE, self._work.source())

    def testItReturnsValidWorkId(self):
        self.assertEqual(ID, self._work.id())                 
