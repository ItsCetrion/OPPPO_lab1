from Model import HomeAnimal


class Dog(HomeAnimal.HomeAnimal):
    def __init__(self, json_data):
        super().__init__()
        self._breed = ""
        self._age = 0
        self._weight = 1
        self.__converting_json_to_object(json_data)

    def __converting_json_to_object(self, json_data):
        try:
            self.breed = json_data["breed"]
            self.age = json_data["age"]
            self.weight = json_data["weight"]
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
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Вес должен быть числом, получено {type(value).__name__}")
        if value <= 0:
            raise ValueError("Вес должен быть положительным")
        self._weight = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Порода должна быть строкой, получено {type(value).__name__}")
        self._breed = value

    def __hash__(self):
        return hash((self._breed, self._age, self._weight))
