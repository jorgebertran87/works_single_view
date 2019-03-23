import unittest


class TestLoadWorksCommand(unittest.TestCase):

    COMMAND_CLASSNAME = 'LoadWorksCommand'
    WORK_REPOSITORY_CLASSNAME = 'WorkRepository'

    _command = None

    def setUp(self):
        works = []
        workRepository = WorkRepository()
        _command = LoadWorksCommand(works, workRepository)

    def testItReturnsValidCommand(self):
        self.assertEqual(self._command.__class__.__name__,
                         self.COMMAND_CLASSNAME)

    def testItReturnsValidCommandWorks(self):
        self.assertEqual(0, len(self._command.works()))

    def testItReturnsValidCommandWorkRepository(self):
        self.assertEqual(self.WORK_REPOSITORY_CLASSNAME,
                         self._command.workRepository().__class__.__name__)
