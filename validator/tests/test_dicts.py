import pytest

from validator.schemas.dicts import DictSchema
from validator.validator import Validator


@pytest.fixture(name="dct_sch")
def get_schema():
    return DictSchema()


@pytest.fixture(name="v")
def get_validator():
    return Validator()


class TestDictSchema:

    def test_common(self, v, dct_sch):
        dct_sch.shape({
            'name': v.string().required(),
            'age': v.number().positive(),
        })
        assert dct_sch.is_valid({'name': 'kolya', 'age': 100})
        assert dct_sch.is_valid({'name': 'maya', 'age': None})
        assert not dct_sch.is_valid({'name': '', 'age': None})
        assert not dct_sch.is_valid({'name': 'ada', 'age': -5})
