from core.application.repositories.work_repository import WorkRepository
from core.infrastructure.api.drf.works_single_view.works_single_view.models import Works, Contributors
from core.domain.work import Work
from core.domain.id import Id
from core.domain.title import Title
from core.domain.contributor import Contributor
from core.domain.iswc import Iswc
from core.domain.source import Source


class DjangoWorkRepository(WorkRepository):

    def add(self, work: Work):
        contributors = []

        for contributor in work.contributors():
            contributorsModel = Contributors()
            contributorsModel.name = contributor.name()
            contributorsModel.save()
            contributors.append(contributorsModel)


        worksModel = self.reconcile(work, contributors)

        if worksModel is None:
            return

        worksModel.contributors.clear()
        worksModel.save()

        self.addContributorsToWork(worksModel, contributors)


    def reconcile(self, work: Work, contributors: list):
        worksModel = self.findByIswc(work.iswc())

        if worksModel is None:
            worksModel = self.findByTitleAndContributors(work.title(), contributors)



        if worksModel is None:
            
            if not work.hasIswc():
                return None 

            worksModel = Works()         

        worksModel.id = work.id().value()
        worksModel.title = work.title().value()
        
        if work.hasIswc():
            worksModel.iswc = work.iswc().value()

        worksModel.source = work.source().value()    

        return worksModel



    def addContributorsToWork(self, worksModel, contributors: list):
        for contributor in contributors:
            worksModel.contributors.add(contributor)

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

    def findByIswc(self, iswc: Iswc):
        return Works.objects.filter(pk=iswc.value()).first()

    def findByTitleAndContributors(self, title: Title, contributors: list):
        return Works.objects.filter(title=title.value(), contributors__in=contributors) .first()   
