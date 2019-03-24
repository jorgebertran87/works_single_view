import unittest
from tests.stubs.work_repository_stub import WorkRepositoryStub
from core.infrastructure.cli.load_works_from_csv import LoadWorksFromCSV
import os


class TestLoadWorksFromCSV(unittest.TestCase):

    def testItLoadsWorks(self):
        workRepository = WorkRepositoryStub()
        cli = LoadWorksFromCSV(
            'tests/infrastructure/cli/works_metadata.csv', workRepository)
        cli.execute()

        self.assertEqual(8, len(workRepository.all()))
