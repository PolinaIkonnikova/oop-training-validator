from validator.strings import StringSchema
from validator.numbers import NumberSchema


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
        return