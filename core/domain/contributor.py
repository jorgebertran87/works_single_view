class Contributor:
    _name: str

    def __init__(self, name: str):
        self._name = name

    def name(self):
        return self._name
