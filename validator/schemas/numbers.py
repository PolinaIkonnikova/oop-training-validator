from validator.schemas.base import BaseSchema


class NumberSchema(BaseSchema):

    name = "number"

    def __init__(self):
        super().__init__()
        self._range_nums: tuple[int, int] | None = None

    def _main_condition_for_entity(self):
        return isinstance(self._entity, float) or isinstance(self._entity, int)

    def _positive_validate(self):
        if self._main_condition_for_entity():
            return self._entity > 0
        return False

    def _range_validate(self):
        if self._main_condition_for_entity():
            return self._range_nums[0] <= self._entity <= self._range_nums[1]
        return False

    def positive(self):
        self.active_validator = self._positive_validate.__name__
        return self

    def range(self, num1, num2):
        self._range_nums = (num1, num2)
        self.active_validator = self._range_validate.__name__
        return self
