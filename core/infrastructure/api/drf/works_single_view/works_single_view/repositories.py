from core.application.repositories.work_repository import WorkRepository
from core.infrastructure.api.drf.works_single_view.works_single_view.models import Works
from core.domain.work import Work
from core.domain.id import Id
from core.domain.title import Title
from core.domain.contributor import Contributor
from core.domain.iswc import Iswc
from core.domain.source import Source


class DjangoWorkRepository(WorkRepository):

    def add(self, work: Work):
        worksModel = Works()
        worksModel.id = work.id().value()
        worksModel.title = work.title().value()
        worksModel.iswc = work.iswc().value()
        worksModel.source = work.source().value()
        worksModel.save()

    def update(self, updatedWork: Work):
        pass

    def all(self):
        worksModels = Works.objects.all()
        works = []

        for worksModel in worksModels:
            title = Title(worksModel.title)
            contributors = []
            iswc = Iswc(worksModel.iswc)
            source = Source(worksModel.source)
            id = Id(worksModel.id)

            work = Work(title, contributors, iswc, source, id)
            works.append(work)
        return works

    def findById(self, id: Id):
        pass
