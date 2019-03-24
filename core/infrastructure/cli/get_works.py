from core.application.repositories.work_repository import WorkRepository
from core.application.CQRS.get_works_query import GetWorksQuery
from core.application.CQRS.get_works_query_handler import GetWorksQueryHandler


class GetWorks:

    _workRepository: WorkRepository

    def __init__(self, csvPath: str, workRepository: WorkRepository):
        self._workRepository = workRepository

    def execute(self):
        getWorksQuery = GetWorksQuery()
        getWorksQueryHandler = GetWorksQueryHandler(self._workRepository)

        return getWorksQueryHandler.handle(getWorksQuery)
