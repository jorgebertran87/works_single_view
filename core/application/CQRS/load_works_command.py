from core.application.repositories.work_repository import WorkRepository


class LoadWorksCommand:

    _works: list

    def __init__(self, works: list):
        self._works = works

    def works(self):
        return self._works
