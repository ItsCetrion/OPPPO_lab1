from Checker import Checker
import pytest


class TestCheckerValidation:
    """Группировка тестов для класса Checker"""

    @pytest.fixture()
    def list_command(self):
        return ["add", "rem", "print", "clear"]

    @pytest.fixture()
    def list_animal(self):
        return ["dog", "cat", "parrot"]

    def test_error_animal(self, list_animal):
        with pytest.raises(ValueError):
            Checker.check_command("Rabbit", list_animal)

    def test_error_command(self, list_command):
        with pytest.raises(ValueError):
            Checker.check_command("Update", list_command)

    def test_error_type_date(self):
        with pytest.raises(TypeError):
            Checker.check_date_str(1)

    def test_error_date_empty(self):
        with pytest.raises(ValueError):
            Checker.check_date_str("")

    def test_error_date_format(self):
        with pytest.raises(ValueError):
            Checker.check_date_str("01-01-2024")

    def test_valid_command(self, list_command):
        Checker.check_command("add", list_command)

    def test_valid_animal(self, list_animal):
        Checker.check_animal("dog", list_animal)

    def test_valid_date(self):
        Checker.check_date_str("01.01.2024")

    def test_command_case_insensitive(self, list_command):
        """Проверка нечувствительности к регистру"""
        Checker.check_command("ADD", list_command)  # Верхний регистр
        Checker.check_command("Add", list_command)  # Смешанный регистр

    def test_animal_case_insensitive(self, list_animal):
        """Проверка нечувствительности к регистру"""
        Checker.check_animal("DOG", list_animal)
        Checker.check_animal("Cat", list_animal)