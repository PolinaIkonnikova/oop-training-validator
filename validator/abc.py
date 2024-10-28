from abc import ABC, abstractmethod
from typing import Any


class TypeSchema(ABC):

    def __init__(self):
        self._entity = None
        self._required: bool = False

    def _required_off(self):
        self._required = False

    def required(self):
        self._required = True

    @abstractmethod
    def is_valid(self, entity: Any) -> bool:
        ...
