import unittest
from core.domain.iswc import Iswc


class TestIswc (unittest.TestCase):

    VALUE = 'Iswc'
    ISWC_CLASSNAME = 'Iswc'

    _iswc = None

    def setUp(self):
        self._iswc = Iswc(self.VALUE)

    def testItReturnsValidIswc(self):
        self.assertEqual(self._iswc.__class__.__name__, self.ISWC_CLASSNAME)

    def testItReturnsValidIswcValue(self):
        self.assertEqual(self.VALUE, self._iswc.value())
