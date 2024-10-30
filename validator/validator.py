from typing import Callable
from validator.abc import TypeSchema
from validator.strings import StringSchema
from validator.numbers import NumberSchema
from validator.lists import ListsSchema
from validator.dicts import DictSchema


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

        for item in TypeSchema.__subclasses__():
            if val_type == item.name:
                item.set_lambda_validator(name, fn)
                return
