from core.application.repositories.work_repository import WorkRepository
from core.domain.work import Work
from core.domain.id import Id


class WorkRepositoryStub(WorkRepository):

    def add(self, work: Work):
        pass

    def update(self, work: Work):
        pass

    def all(self):
        pass

    def findById(self, id: Id):
        pass
