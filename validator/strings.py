from enum import Enum, auto
from typing import Any

from validator.abc import TypeSchema

class StringValidateMethods(Enum):
    lambda_ = auto()
    contains  = auto()
    min_len = auto()


class StringSchema(TypeSchema):

    name = "string"

    def __init__(self):
        super().__init__()
        self.cont = None
        self.min_len_count = None

    def _no_required_condition(self) -> bool:
        return self._required is False and (self._entity is None or self._entity == "")

    def _main_condition_for_entity(self) -> bool:
        return self._entity != "" and isinstance(self._entity, str)

    def _contains_validate(self) -> bool:
        return self.cont in self._entity

    def _len_validate(self):
        return self.min_len_count <= len(self._entity)

    def contains(self, cont: str):
        self.cont = cont
        self.active_validator = self._contains_validate.__name__
        return self

    def min_len(self, num: int):
        self.min_len_count = num
        self.active_validator = self._len_validate.__name__
        return self
