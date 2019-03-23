import unittest
from core.domain.work import Work
from core.domain.title import Title
from core.domain.iswc import Iswc
from core.domain.source import Source
from core.domain.id import Id
from core.domain.contributor import Contributor


class TestWork (unittest.TestCase):

    TITLE = 'Title 1'
    ISWC = 'iswc'
    SOURCE = 'source'
    ID = 9999
    CONTRIBUTOR = 'Contributor'

    WORK_CLASSNAME = 'Work'

    _work = None

    def setUp(self):
        title = Title(self.TITLE)
        iswc = Iswc(self.ISWC)
        source = Source(self.SOURCE)
        id = Id(self.ID)
        contributor = Contributor(self.CONTRIBUTOR)

        self._work = Work(title, [contributor], iswc,  source, id)

    def testItReturnsValidWork(self):
        self.assertEqual(self._work.__class__.__name__, self.WORK_CLASSNAME)

    def testItReturnsValidWorkTitle(self):
        self.assertEqual(self.TITLE, self._work.title().value())

    def testItReturnsValidWorkIswc(self):
        self.assertEqual(self.ISWC, self._work.iswc().value())

    def testItReturnsValidWorkSource(self):
        self.assertEqual(self.SOURCE, self._work.source().value())

    def testItReturnsValidWorkId(self):
        self.assertEqual(self.ID, self._work.id().value())

    def testItReturnsValidWorkContributor(self):
        contributors = self._work.contributors()
        self.assertEqual(self.CONTRIBUTOR, contributors[0].name())
