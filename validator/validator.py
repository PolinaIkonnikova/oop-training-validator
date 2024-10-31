from typing import Callable
from validator.schemas.base import BaseSchema
from validator.schemas.strings import StringSchema
from validator.schemas.numbers import NumberSchema
from validator.schemas.lists import ListsSchema
from validator.schemas.dicts import DictSchema


class Validator:

    @staticmethod
    def string():
        return StringSchema()

    @staticmethod
    def number():
        return NumberSchema()

    @staticmethod
    def list():
        return ListsSchema()

    @staticmethod
    def dict():
        return DictSchema()

    @staticmethod
    def add_validator(val_type: str, name: str, fn: Callable):

        for item in BaseSchema.__subclasses__():
            if val_type == item.name:
                item.set_lambda_validator(name, fn)
                return
