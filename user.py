class User:
    def __init__(self, id: int=0, first_name: str='DELETED', last_name: str=''):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name

    def __repr__(self):
        return f'{self._first_name} {self._last_name}'
