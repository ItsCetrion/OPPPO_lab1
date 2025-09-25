from Model import HomeAnimal


class Cat(HomeAnimal.HomeAnimal):
    def __init__(self, json_data):
        super().__init__(json_data)
        self._breed = ""
        self._age = 0
        self._coat_color = ""
        self.__converting_json_to_object(json_data)

    def __converting_json_to_object(self, json_data):
        try:
            self.breed = json_data["breed"]
            self.age = json_data["age"]
            self.coat_color = json_data["coat_color"]
        except KeyError:
            raise KeyError("В файле не верно указан ключ для значения")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Возраст должен быть числом, получено {type(value).__name__}")
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = value

    @property
    def coat_color(self):
        return self._coat_color

    @coat_color.setter
    def coat_color(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Цвет шерсти должен быть строкой, получено {type(value).__name__}")
        self._coat_color = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Порода должна быть строкой, получено {type(value).__name__}")
        self._breed = value

    def __hash__(self):
        return hash((self._breed, self._age, self._coat_color))