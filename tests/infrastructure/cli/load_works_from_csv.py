import unittest
from tests.stubs.work_repository_stub import WorkRepositoryStub

class TestLoadWorksFromCSV(unittest.TestCase):

    def testItLoadsWorks(self):
        workRepository = WorkRepositoryStub()
        cli = LoadWorksFromCSV('works_metadata.csv', workRepository)
        cli.execute()

        self.assertEqual(2, len(workRepository.all()))

