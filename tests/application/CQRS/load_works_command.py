import unittest
from core.application.CQRS.load_works_command import LoadWorksCommand


class TestLoadWorksCommand(unittest.TestCase):

    COMMAND_CLASSNAME = 'LoadWorksCommand'

    _command = None

    def setUp(self):
        works = []
        self._command = LoadWorksCommand(works)

    def testItReturnsValidCommand(self):
        self.assertEqual(self._command.__class__.__name__,
                         self.COMMAND_CLASSNAME)

    def testItReturnsValidCommandWorks(self):
        self.assertEqual(0, len(self._command.works()))
