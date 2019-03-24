from core.application.repositories.work_repository import WorkRepository
from core.application.CQRS.get_works_query import GetWorksQuery


class GetWorksQueryHandler:

    __workRepository: WorkRepository

    def __init__(self, workRepository: WorkRepository):
        self._workRepository = workRepository

    def handle(self, query: GetWorksQuery):
        return self._workRepository.all()
