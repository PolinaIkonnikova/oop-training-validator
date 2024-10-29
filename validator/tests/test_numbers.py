import pytest

from validator.numbers import NumberSchema


@pytest.fixture(name="num_sch")
def get_schema():
    return NumberSchema()


class TestNumberSchema:

    def test_common(self, num_sch):
        assert num_sch.is_valid(None)
        num_sch.required()
        assert num_sch.is_valid(5)
        assert not num_sch.is_valid(None)

    def test_with_positive_validate(self, num_sch):
        num_sch.positive()
        assert not num_sch.is_valid(-5)
        assert num_sch.is_valid(None)
        num_sch.required()
        assert not num_sch.is_valid(None)

    def test_with_range_validate(self, num_sch):
        num_sch.range(-5, 5)
        assert num_sch.is_valid(1)
        assert num_sch.is_valid(None)
        num_sch.required()
        assert not num_sch.is_valid(None)

    def test_with_all_validates(self, num_sch):
        assert num_sch.range(-5, 0).positive().is_valid(10)
        assert not num_sch.positive().range(-5, 0).is_valid(10)
        assert num_sch.range(-5, 0).range(0, 5).is_valid(3)
