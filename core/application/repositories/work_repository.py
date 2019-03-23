import abc
from core.domain.work import Work
from core.domain.id import Id


class WorkRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, work: Work):
        pass

    @abc.abstractmethod
    def update(self, work: Work):
        pass

    @abc.abstractmethod
    def all(self):
        pass

    @abc.abstractmethod
    def findById(self, id: Id):
        pass
