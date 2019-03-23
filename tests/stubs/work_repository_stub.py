from core.application.repositories.work_repository import WorkRepository
from core.domain.work import Work
from core.domain.id import Id


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

    def findById(self, id: Id):
        for i in range(len(self._works)):
            work = self._works[i]
            if work.id().equals(id):
                return work

        return None
