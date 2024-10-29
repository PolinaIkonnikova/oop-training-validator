from typing import Any

from validator.abc import TypeSchema

class DictSchema:

    def __init__(self):
        self._targets = None

    def shape(self, items: dict[Any, TypeSchema]):
        self._targets = items

    def _validate_key(self, key, val):
        return self._targets.get(key).is_valid(val)

    def is_valid(self, entities: dict) -> bool:

        if not self._targets and not entities:
            return False

        return all(list(map(lambda item: self._targets.get(item[0]).is_valid(item[1]),
                            entities.items())))
