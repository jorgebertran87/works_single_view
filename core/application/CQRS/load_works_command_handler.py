from core.application.repositories.work_repository import WorkRepository
from core.application.CQRS.load_works_command import LoadWorksCommand
from core.domain.title import Title
from core.domain.contributor import Contributor
from core.domain.iswc import Iswc
from core.domain.source import Source
from core.domain.id import Id
from core.domain.work import Work


class LoadWorksCommandHandler:

    __workRepository: WorkRepository

    def __init__(self, workRepository: WorkRepository):
        self._workRepository = workRepository

    def handle(self, command: LoadWorksCommand):
        works = command.works()

        for i in range(len(works)):
            rawWork = works[i]
            work = self.createWork(rawWork)

            self._workRepository.add(work)

    def createWork(self, rawWork):
        title = Title(rawWork['title'])
        
        contributorsList = rawWork['contributors'].split('|')
        contributors = []

        for contributor in contributorsList:
            contributors.append(Contributor(contributor))

        iswc = Iswc(rawWork['iswc'])
        source = Source(rawWork['source'])
        id = Id(rawWork['id'])

        work = Work(title, contributors, iswc, source, id)

        return work
