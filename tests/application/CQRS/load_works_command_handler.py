import unittest
from tests.stubs.work_repository_stub import WorkRepositoryStub
from core.application.CQRS.load_works_command import LoadWorksCommand


class TestLoadWorksCommandHandler(unittest.TestCase):

    COMMAND_CLASSNAME = 'LoadWorksCommandHandler'

    _commandHandler = None

    def setUp(self):
        workRepositoryStub = WorkRepositoryStub()
        self._commandHandler = LoadWorksCommandHandler(workRepositoryStub)

    def testItReturnsValidCommandHandler(self):
        self.assertEqual(self._command.__class__.__name__,
                         self.COMMAND_CLASSNAME)
