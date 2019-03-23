import unittest
from core.domain.id import Id


class TestId(unittest.TestCase):

    VALUE = 'Id'
    ID_CLASSNAME = 'Id'

    _id = None

    def setUp(self):
        self._id = Id(self.VALUE)

    def testItReturnsValidId(self):
        self.assertEqual(self._id.__class__.__name__, self.ID_CLASSNAME)

    def testItReturnsValidIdValue(self):
        self.assertEqual(self.VALUE, self._id.value())
