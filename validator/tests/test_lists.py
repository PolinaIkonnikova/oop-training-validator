import pytest

from validator.schemas.lists import ListsSchema


@pytest.fixture(name="lst_sch")
def get_schema():
    return ListsSchema()


class TestListsSchema:

    def test_common(self, lst_sch):
        assert lst_sch.is_valid([])
        assert lst_sch.is_valid(None)
        assert lst_sch.is_valid([1])
        lst_sch.required()
        assert not lst_sch.is_valid(None)
        assert not lst_sch.is_valid(1)

    def test_sizeof(self, lst_sch):
        lst_sch.sizeof(2)
        assert lst_sch.is_valid([1, 2])
        assert not lst_sch.is_valid([1])
