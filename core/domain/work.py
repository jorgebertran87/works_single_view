from .title import Title
from .iswc import Iswc
from .source import Source
from .id import Id


class Work:

    _title: Title
    _contributors: list
    _iswc: Iswc
    _source: Source
    _id: Id

    def __init__(self, title: Title, contributors: list, iswc: Iswc, source: Source, id: Id):
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

    def equals(work):
        return self._id.equals(work.id())
