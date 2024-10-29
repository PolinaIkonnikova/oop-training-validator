from typing import Any

from validator.abc import TypeSchema

class ListsSchema(TypeSchema):

    def __init__(self):
        super().__init__()
        self._size = None

    def _main_condition_for_entity(self) -> bool:
        return isinstance(self._entity, list)

    def _sizeof_validate(self):
        if self._main_condition_for_entity:
            return len(self._entity) == self._size
        return False

    def is_valid(self, entity: Any) -> bool:
        self._set_entity(entity)
        if self._no_required_condition():
            return True
        if self._size:
            return self._sizeof_validate()
        return self._main_condition_for_entity()

    def sizeof(self, num: int):
        self._size = num
