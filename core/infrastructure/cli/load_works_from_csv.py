from core.application.repositories.work_repository import WorkRepository
from core.application.CQRS.load_works_command import LoadWorksCommand
from core.application.CQRS.load_works_command_handler import LoadWorksCommandHandler
import csv

class LoadWorksFromCSV:

    _works: list
    _workRepository: WorkRepository

    def __init__(self, csvPath: str, workRepository: WorkRepository):
        self._works = []
        
        csvFile = open(csvPath)

        inputFile = csv.DictReader(csvFile)

        for work in inputFile:
            self._works.append(work)

        csvFile.close()    

        self._workRepository = workRepository



    def execute(self):
        loadWorksCommand = LoadWorksCommand(self._works)
        loadWorksCommandHandler = LoadWorksCommandHandler(self._workRepository)

        loadWorksCommandHandler.handle(loadWorksCommand)
