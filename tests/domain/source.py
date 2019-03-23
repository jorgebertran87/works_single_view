import unittest
from core.domain.source import Source


class TestSource(unittest.TestCase):

    VALUE = 'Source'
    SOURCE_CLASSNAME = 'Source'

    _source = None

    def setUp(self):
        self._source = Source(self.VALUE)

    def testItReturnsValidSource(self):
        self.assertEqual(self._source.__class__.__name__,
                         self.SOURCE_CLASSNAME)

    def testItReturnsValidSourceValue(self):
        self.assertEqual(self.VALUE, self._source.value())
