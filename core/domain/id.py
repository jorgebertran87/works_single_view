class Id:
    _value: int

    def __init__(self, value: int):
        self._value = value

    def value(self):
        return self._value

    def equals(self, id):
        return self._value == id.value()
