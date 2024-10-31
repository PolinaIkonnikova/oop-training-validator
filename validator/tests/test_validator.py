from typing import Callable
from validator.schemas.numbers import NumberSchema
from validator.validator import Validator


def test_change_validators():
    v = Validator()
    sch = v.number()
    assert isinstance(sch, NumberSchema)


def my_func(num):
    return num % 2 == 0


def test_add_validator():
    v = Validator()
    v.add_validator("number", "even", my_func)
    assert isinstance(v.number()._lambda_validators.get('even'), Callable)
    assert v.number().test("even", 5)
