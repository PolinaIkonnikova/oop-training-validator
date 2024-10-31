from validator.schemas.base import BaseSchema


class ListsSchema(BaseSchema):

    name = "list"

    def __init__(self):
        super().__init__()
        self._size = None

    def _main_condition_for_entity(self) -> bool:
        return isinstance(self._entity, list)

    def _sizeof_validate(self):
        if self._main_condition_for_entity:
            return len(self._entity) == self._size
        return False

    def sizeof(self, num: int):
        self._size = num
        self.active_validator = self._sizeof_validate.__name__
        return self
