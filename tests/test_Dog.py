from Model.Dog import Dog
import pytest


class TestDogValidation:
    """Группировка тестов для класса Cat"""

    # Позитивный тест
    def test_valid_cat_creation(self):
        dict_ = {"animal": "Dog", "breed": "Алабай", "age": 4, "weight": 34, "name": "A1", "DateLastVet": "10.09.2025"}
        dog = Dog(dict_)
        assert dog.breed == "Алабай"
        assert dog.age == 4

    # Параметризованные тесты для TypeError
    @pytest.mark.parametrize("field,invalid_value", [
        ("breed", 5),
        ("age", "5"),
        ("weight", "5"),
        ("name", 5),
        ("DateLastVet", 5)
    ])
    def test_type_errors(self, field, invalid_value):
        base_data = {"animal": "Dog", "breed": "Алабай", "age": 4,
                     "weight": 34, "name": "A1", "DateLastVet": "10.09.2025"}
        base_data[field] = invalid_value

        with pytest.raises(TypeError):
            Dog(base_data)

    # Параметризованные тесты для ValueError
    @pytest.mark.parametrize("field,invalid_value", [
        ("breed", ""),
        ("age", -5),
        ("weight", -5),
        ("name", ""),
        ("DateLastVet", ""),
        ("DateLastVet", "11-09-2025")
    ])
    def test_value_errors(self, field, invalid_value):
        base_data = {"animal": "Dog", "breed": "Алабай", "age": 4,
                     "weight": 34, "name": "A1", "DateLastVet": "10.09.2025"}
        base_data[field] = invalid_value

        with pytest.raises(ValueError):
            Dog(base_data)

    # Тесты на отсутствующие ключи
    @pytest.mark.parametrize("missing_key", ["breed", "age", "weight", "name", "DateLastVet"])
    def test_missing_keys(self, missing_key):
        base_data = {"animal": "Dog", "breed": "Алабай", "age": 4,
                     "weight": 34, "name": "A1", "DateLastVet": "10.09.2025"}
        del base_data[missing_key]

        with pytest.raises(KeyError):
            Dog(base_data)