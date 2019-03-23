
class Work:

    _title: str
    _contributors: list
    _iswc: str
    _source: str
    _id: int

    def __init__(self, title: str, contributors: list, iswc: str, source: str, id: int):
        self._title = title
        self._contributors = contributors
        self._iswc = iswc
        self._source = source
        self._id = id

    def title(self):
        return self._title

    def contributors(self):
        return self._contributors

    def iswc(self):
        return self._iswc

    def source(self):
        return self._source

    def id(self):
        return self._id
