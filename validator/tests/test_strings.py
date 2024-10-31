import pytest

from validator.schemas.strings import StringSchema


@pytest.fixture(name="str_sch")
def get_schema():
    return StringSchema()


class TestStringSchema:

    def test_common(self, str_sch):
        assert str_sch.is_valid("")
        str_sch.required()
        assert not str_sch.is_valid("")
        str_sch.min_len(10)
        assert not str_sch.is_valid("")
