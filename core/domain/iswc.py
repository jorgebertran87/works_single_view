class Iswc:
    _value: int

    def __init__(self, value: int):
        self._value = value

    def value(self):
        return self._value

    def equals(self, iswc):
        return self._value == iswc.value()
