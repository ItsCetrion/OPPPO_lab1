from Model.Parrot import Parrot
import pytest


class TestParrotValidation:
    """Группировка тестов для класса Cat"""

    # Позитивный тест
    def test_valid_cat_creation(self):
        dict_ = {"animal": "Parrot", "type_parrot": "Пернатый", "wingspan": 5.5,
                 "name": "A1", "DateLastVet": "09.09.2025"}
        dog = Parrot(dict_)
        assert dog.type_parrot == "Пернатый"
        assert dog.wingspan == 5.5

    # Параметризованные тесты для TypeError
    @pytest.mark.parametrize("field,invalid_value", [
        ("type_parrot", 5),
        ("wingspan", "5"),
        ("name", 5),
        ("DateLastVet", 5)
    ])
    def test_type_errors(self, field, invalid_value):
        base_data = {"animal": "Parrot", "type_parrot": "Пернатый", "wingspan": 5.5,
                     "name": "A1", "DateLastVet": "09.09.2025"}
        base_data[field] = invalid_value

        with pytest.raises(TypeError):
            Parrot(base_data)

    # Параметризованные тесты для ValueError
    @pytest.mark.parametrize("field,invalid_value", [
        ("type_parrot", ""),
        ("wingspan", -5),
        ("name", ""),
        ("DateLastVet", ""),
        ("DateLastVet", "11-09-2025")
    ])
    def test_value_errors(self, field, invalid_value):
        base_data = {"animal": "Parrot", "type_parrot": "Пернатый", "wingspan": 5.5,
                     "name": "A1", "DateLastVet": "09.09.2025"}
        base_data[field] = invalid_value

        with pytest.raises(ValueError):
            Parrot(base_data)

    # Тесты на отсутствующие ключи
    @pytest.mark.parametrize("missing_key", ["type_parrot", "wingspan", "name", "DateLastVet"])
    def test_missing_keys(self, missing_key):
        base_data = {"animal": "Parrot", "type_parrot": "Пернатый", "wingspan": 5.5,
                     "name": "A1", "DateLastVet": "09.09.2025"}
        del base_data[missing_key]

        with pytest.raises(KeyError):
            Parrot(base_data)