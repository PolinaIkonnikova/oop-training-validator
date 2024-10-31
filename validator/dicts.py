from typing import Any

from validator.abc import TypeSchema


class DictSchema(TypeSchema):

    name = "dict"

    def __init__(self):
        super().__init__()
        self._targets = None

    def shape(self, items: dict[Any, TypeSchema]):
        self.active_validator = self._shape_dict_validate.__name__
        self._targets = items
        return self

    def _main_condition_for_entity(self) -> bool:
        return all(list(map(lambda item:
                            self._targets.get(item[0]).is_valid(item[1]),
                            self._entity.items())))

    def _validate_key(self, key, val):
        return self._targets.get(key).is_valid(val)

    def _shape_dict_validate(self):
        return self._main_condition_for_entity()
