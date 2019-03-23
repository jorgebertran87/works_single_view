import unittest
from tests.stubs.work_repository_stub import WorkRepositoryStub
from core.application.CQRS.load_works_command_handler import LoadWorksCommandHandler
from core.application.CQRS.load_works_command import LoadWorksCommand


class TestLoadWorksCommandHandler(unittest.TestCase):

    COMMAND_HANDLER_CLASSNAME = 'LoadWorksCommandHandler'

    _commandHandler = None
    _workRepository = None

    def setUp(self):
        self._workRepository = WorkRepositoryStub()
        self._commandHandler = LoadWorksCommandHandler(self._workRepository)

    def testItReturnsValidCommandHandler(self):
        self.assertEqual(self._commandHandler.__class__.__name__,
                         self.COMMAND_HANDLER_CLASSNAME)

    def testItHandlesSuccesfully(self):
        works = [
            {
                'title': 'Title 1',
                'contributors': 'Jeje',
                'iswc': 'Iswc',
                'source': 'Source',
                'id': 1
            },
            {
                'title': 'Title 2',
                'contributors': 'Jeje 2',
                'iswc': 'Iswc 2',
                'source': 'Source 2',
                'id': 2
            }
        ]

        command = LoadWorksCommand(works)

        self._commandHandler.handle(command)

        self.assertEqual(2, len(self._workRepository.all()))
