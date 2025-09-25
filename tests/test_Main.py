import pytest
import main


class TestMain:
    """Тесты для Main"""

    @pytest.fixture
    def str_json(self):
        return ('{"animal": "Parrot", "type_parrot": "Пернатый", "wingspan": 5.5, '
                '"name": "A1", "DateLastVet": "09.09.2025"}')

    @pytest.fixture
    def str_invalid_json(self):
        return ('{"animal": Parrot, "type_parrot": "Пернатый", "wingspan": 5.5, '
                '"name": "A1", "DateLastVet": "09.09.2025"}')

    @pytest.mark.parametrize("data,expected", [
        ("", 1),
        ("Hello World", 2),
        ("Hello  World", 2),
        ("Hello World World", 2),
        ("   Hello World World", 2),
    ])
    def test_split_one_sep(self, data, expected):
        list_result = main.spliter(data)
        assert len(list_result) == expected

    def test_error_path_not_found(self, capsys):
        main.file_read_and_clear("5:\\Users\\79951\\Documents\\GitHub\\OPPPO_lab1\\test1.txt")
        captured = capsys.readouterr()
        assert "❌ Файл не найден:" in captured.out

    def test_convert_str_json_in_json_invalid(self, str_invalid_json):
        with pytest.raises(TypeError):
            main.convert_str_json_in_json(str_invalid_json)

    def test_convert_str_json_in_json_valid(self, str_json):
        main.convert_str_json_in_json(str_json)

