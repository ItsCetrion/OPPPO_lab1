from Model.Cat import Cat
import pytest


class TestCatValidation:
    """Группировка тестов для класса Cat"""

    # Позитивный тест
    def test_valid_cat_creation(self):
        dict_ = {"animal": "Cat", "breed": "Британец", "age": 5,
                 "coat_color": "Серый", "name": "A1", "DateLastVet": "11.09.2025"}
        cat = Cat(dict_)
        assert cat.breed == "Британец"
        assert cat.age == 5

    # Параметризованные тесты для TypeError
    @pytest.mark.parametrize("field,invalid_value", [
        ("breed", 5),
        ("age", "5"),
        ("coat_color", 5),
        ("name", 5),
        ("DateLastVet", 5)
    ])
    def test_type_errors(self, field, invalid_value):
        base_data = {"animal": "Cat", "breed": "Британец", "age": 5,
                     "coat_color": "Серый", "name": "A1", "DateLastVet": "11.09.2025"}
        base_data[field] = invalid_value

        with pytest.raises(TypeError):
            Cat(base_data)

    # Параметризованные тесты для ValueError
    @pytest.mark.parametrize("field,invalid_value", [
        ("breed", ""),
        ("age", -5),
        ("coat_color", ""),
        ("name", ""),
        ("DateLastVet", ""),
        ("DateLastVet", "11-09-2025")
    ])
    def test_value_errors(self, field, invalid_value):
        base_data = {"animal": "Cat", "breed": "Британец", "age": 5,
                     "coat_color": "Серый", "name": "A1", "DateLastVet": "11.09.2025"}
        base_data[field] = invalid_value

        with pytest.raises(ValueError):
            Cat(base_data)

    # Тесты на отсутствующие ключи
    @pytest.mark.parametrize("missing_key", ["breed", "age", "coat_color", "name", "DateLastVet"])
    def test_missing_keys(self, missing_key):
        base_data = {"animal": "Cat", "breed": "Британец", "age": 5,
                     "coat_color": "Серый", "name": "A1", "DateLastVet": "11.09.2025"}
        del base_data[missing_key]

        with pytest.raises(KeyError):
            Cat(base_data)