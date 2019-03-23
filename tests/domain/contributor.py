import unittest
from core.domain.contributor import Contributor


class TestContributor(unittest.TestCase):

    NAME = 'Contributor'
    CONTRIBUTOR_CLASSNAME = 'Contributor'

    _contributor = None

    def setUp(self):
        self._contributor = Contributor(self.NAME)

    def testItReturnsValidContributor(self):
        self.assertEqual(self._contributor.__class__.__name__,
                         self.CONTRIBUTOR_CLASSNAME)

    def testItReturnsValidContributorName(self):
        self.assertEqual(self.NAME, self._contributor.name())
