from typing import Any

from validator.abc import TypeSchema

class NumberSchema(TypeSchema):

    def __init__(self):
        super().__init__()
        self._positive: bool = False
        self._range_nums: tuple[int, int] | None = None

    @property
    def _main_condition_for_num(self):
        return isinstance(self._entity, float) or isinstance(self._entity, int)

    def _num_validate(self) -> bool:
        if self._required:
            return self._main_condition_for_num
        return self._main_condition_for_num or self._entity is None

    def _positive_validate(self):
        if self._main_condition_for_num:
            return self._entity >= 0
        return False

    def _range_validate(self):
        if self._main_condition_for_num:
            return self._range_nums[0] <= self._entity <= self._range_nums[1]
        return False

    def is_valid(self, entity: Any) -> bool:
        self._entity = entity
        if self._positive:
            return self._positive_validate()
        if self._range_nums:
            return self._range_validate()
        return self._num_validate()

    def positive(self):
        self._positive = True
        self._range_nums = None
        return self

    def range(self, num1, num2):
        self._range_nums = (num1, num2)
        self._positive = False
        return self
