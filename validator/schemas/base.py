from abc import ABC, abstractmethod
from typing import Any, Callable


class BaseSchema(ABC):

    name = ""
    _lambda_validators: dict = {}

    def __init__(self):
        self._entity = None
        self._required: bool = False
        self.active_validator: str | None = None
        self.lambda_params: Any = None

    @classmethod
    def set_lambda_validator(cls, name: str, fn: Callable):
        cls._lambda_validators[name] = fn

    def _set_entity(self, entity: Any):
        self._entity = entity

    def _no_required_condition(self) -> bool:
        return self._required is False and self._entity is None

    @abstractmethod
    def _main_condition_for_entity(self) -> bool:
        ...

    def is_valid(self, entity: Any) -> bool:
        self._set_entity(entity)
        if self._no_required_condition():
            return True
        if self.active_validator is None:
            return self._main_condition_for_entity()
        if self.active_validator in self._lambda_validators:
            return self._lambda_validators[self.active_validator](self._entity,
                                                                  *self.lambda_params)

        return getattr(self, self.active_validator)()

    def test(self, lambda_name: str, *args):
        if lambda_name in self._lambda_validators:
            self.active_validator = lambda_name
            self.lambda_params = args if args else None
        return self

    def required(self):
        self._required = True
        return self
