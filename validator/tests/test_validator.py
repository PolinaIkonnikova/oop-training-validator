from typing import Callable
from validator.numbers import NumberSchema
from validator.validator import Validator


def test_change_validators():
    v = Validator()
    sch = v.number()
    assert isinstance(sch, NumberSchema)


def test_add_validator():
    v = Validator()
    fn = lambda num: num % 2 == 0
    v.add_validator("number", "even", fn)
    assert isinstance(v.number()._lambda_validators.get('even'), Callable)
    assert v.number().test("even", 5)
