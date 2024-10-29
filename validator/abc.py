from abc import ABC, abstractmethod
from typing import Any


class TypeSchema(ABC):

    def __init__(self):
        self._entity = None
        self._required: bool = False

    def required(self):
        self._required = True
        return self

    def _set_entity(self, entity: Any):
        self._entity = entity

    def _no_required_condition(self) -> bool:
        return self._required is False and self._entity is None

    @abstractmethod
    def _main_condition_for_entity(self) -> bool:
        ...

    @abstractmethod
    def is_valid(self, entity: Any) -> bool:
        ...
