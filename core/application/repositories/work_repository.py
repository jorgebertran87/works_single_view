import abc
from core.domain.work import Work
from core.domain.iswc import Iswc
from core.domain.title import Title


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
    def findByIswc(self, iswc: Iswc):
        pass

    @abc.abstractmethod
    def findByTitleAndContributors(self, title: Title, contributors: list):
        pass
