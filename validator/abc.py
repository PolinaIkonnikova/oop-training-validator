from abc import ABC, abstractmethod
from typing import Any


class TypeSchema(ABC):

    def __init__(self):
        self._entity = None
        self._required: bool = False

    def required(self):
        self._required = True

    def _set_entity(self, entity: Any):
        self._entity = entity

    @property
    @abstractmethod
    def _main_condition_for_entity(self) -> bool:
        ...

    def _main_validate(self) -> bool:
        if self._required is True:
            return self._main_condition_for_entity
        return self._main_condition_for_entity or self._entity is None

    @abstractmethod
    def is_valid(self, entity: Any) -> bool:
        ...
