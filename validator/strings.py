from typing import Any

from validator.abc import TypeSchema


class StringSchema(TypeSchema):

    def __init__(self):
        super().__init__()
        self.entity = None
        self.cont = None
        self.min_len_count = None

    def _string_validate(self) -> bool:
        if self._required:
            return bool(self.entity)
        return True

    def _contains_validate(self) -> bool:
        return self.cont in self.entity

    def _len_validate(self):
        return self.min_len_count <= len(self.entity)

    def is_valid(self, entity: Any) -> bool:
        self.entity = entity
        if self.cont:
            return self._contains_validate()
        if self.min_len_count:
            return self._len_validate()

        return self._string_validate()

    def contains(self, cont: str):
        self.cont = cont
        self.min_len_count = None
        return self

    def min_len(self, num: int):
        self.min_len_count = num
        self.cont = None
        return self

    def required(self):
        self._required = True