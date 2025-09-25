import pytest
from Container import Container
from Model.Cat import Cat
from Model.Dog import Dog
from Model.Parrot import Parrot


class TestContainer:
    """Тесты для класса Container"""

    @pytest.fixture
    def container(self):
        return Container()

    @pytest.fixture
    def sample_cat(self):
        return Cat({
            "animal": "Cat", "breed": "Британец", "age": 3,
            "coat_color": "Серый", "name": "Мурзик", "DateLastVet": "15.09.2024"
        })

    @pytest.fixture
    def sample_dog(self):
        return Dog({
            "animal": "Dog", "breed": "Овчарка", "age": 5,
            "weight": 25, "name": "Барсик", "DateLastVet": "10.09.2024"
        })

    @pytest.fixture
    def sample_parrot(self):
        return Parrot(
            {"animal": "Parrot", "type_parrot": "Пернатый", "wingspan": 5.5,
             "name": "A1", "DateLastVet": "19.09.2025"})

    @pytest.fixture
    def populated_container(self, container, sample_cat, sample_dog, sample_parrot):
        """Контейнер с несколькими животными"""
        container.add(sample_cat)
        container.add(sample_dog)
        container.add(sample_parrot)
        return container

    def test_add_object(self, container, sample_cat):
        """Тест добавления объекта в контейнер"""
        container.add(sample_cat)
        # Проверяем, что объект добавлен (через печать или другие методы)
        assert container.count_obj() == 1  # Не идеально, но работает

    def test_add_multiple_objects(self, container, sample_cat, sample_dog):
        """Тест добавления нескольких объектов"""
        container.add(sample_cat)
        container.add(sample_dog)
        assert container.count_obj() == 2

    def test_delete_by_age_equal(self, populated_container, sample_cat):
        """Удаление объектов с возрастом равным 3"""
        populated_container.deleted_with_condition("age", "==", 3)
        remaining_objects = populated_container.list_object
        assert len(remaining_objects) == 2  # Собака и попугай
        assert sample_cat not in remaining_objects

    def test_delete_by_age_greater_than(self, populated_container):
        """Удаление объектов с возрастом больше 3"""
        populated_container.deleted_with_condition("age", ">", 3)
        remaining_objects = populated_container.list_object
        assert len(remaining_objects) == 2

    def test_delete_by_name(self, populated_container, sample_dog):
        """Удаление по имени"""
        populated_container.deleted_with_condition("name", "==", "Барсик")
        remaining_objects = populated_container.list_object
        assert len(remaining_objects) == 2
        assert sample_dog not in remaining_objects

    def test_delete_by_date(self, populated_container, sample_parrot):
        """Удаление по дате последнего визита к ветеринару"""
        populated_container.deleted_with_condition("DateLastVet", ">", "15.09.2024")
        remaining_objects = populated_container.list_object
        assert len(remaining_objects) == 2
        assert sample_parrot not in remaining_objects

    def test_delete_nonexistent_condition(self, populated_container):
        """Удаление по условию, которому никто не удовлетворяет"""
        initial_count = len(populated_container.list_object)
        populated_container.deleted_with_condition("age", "==", 100)
        assert len(populated_container.list_object) == initial_count

    def test_delete_invalid_relationship(self, populated_container):
        """Тест на неверный оператор сравнения"""
        with pytest.raises(ValueError, match="Неизвестный оператор: <>"):
            populated_container.deleted_with_condition("age", "<>", 3)

    def test_delete_invalid_date_format(self, populated_container):
        """Тест на неверный формат даты"""
        with pytest.raises(ValueError, match="Дата указана не в формате dd.mm.yyyy"):
            populated_container.deleted_with_condition("DateLastVet", ">", "2024-09-10")

    def test_delete_nonexistent_field(self, populated_container):
        """Тест на несуществующее поле"""
        # Не должно быть ошибки, просто никто не удалится
        initial_count = len(populated_container.list_object)
        populated_container.deleted_with_condition("nonexistent_field", "==", "value")
        assert len(populated_container.list_object) == initial_count

    @pytest.mark.parametrize("data,relationship,target,expected", [
        (5, ">", 3, True),
        (5, "<", 3, False),
        (5, "==", 5, True),
        (5, "!=", 5, False),
        (5, ">=", 5, True),
        (5, "<=", 5, True),
    ])
    def test_comparison_method(self, data, relationship, target, expected):
        """Тест статического метода сравнения"""
        result = Container._Container__comparison(data, relationship, target)
        assert result == expected

    def test_clear_container(self, populated_container):
        """Тест очистки контейнера"""
        populated_container.clear()
        assert len(populated_container.list_object) == 0

    def test_print_method(self, populated_container, capsys):
        """Тест, что метод print не вызывает ошибок"""
        populated_container.print()
        captured = capsys.readouterr()
        assert "Animal:" in captured.out

    def test_complex_scenario(self, container, sample_cat, sample_dog, sample_parrot):
        """Комплексный тест: добавление → удаление → добавление → очистка"""
        # Добавляем
        container.add(sample_cat)
        container.add(sample_dog)
        assert len(container.list_object) == 2

        container.deleted_with_condition("age", ">", 3)
        assert len(container.list_object) == 1  # sample_cat (age=3) удален?

        container.add(sample_parrot)
        assert len(container.list_object) == 2

        container.clear()
        assert len(container.list_object) == 0