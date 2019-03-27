from core.application.repositories.work_repository import WorkRepository
from core.domain.work import Work
from core.domain.iswc import Iswc
from core.domain.title import Title


class WorkRepositoryStub(WorkRepository):
    _works: list

    def __init__(self):
        self._works = []

    def add(self, work: Work):
        self._works.append(work)

    def update(self, updatedWork: Work):
        for i in range(len(self._works)):
            work = self._works[i]
            if work.equals(updatedWork):
                works[i] = updatedWork

    def all(self):
        return self._works

    def findByIswc(self, iswc: Iswc):
        for i in range(len(self._works)):
            work = self._works[i]
            if work.iswc().equals(iswc):
                return work

        return None

    def findByTitleAndContributors(self, title: Title, contributors: list):
        for i in range(len(self._works)):
            work = self._works[i]
            if work.title().equals(title):
                return work

        return None
