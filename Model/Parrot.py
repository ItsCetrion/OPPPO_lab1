from Model import HomeAnimal


class Parrot(HomeAnimal.HomeAnimal):
    def __init__(self, json_data):
        super().__init__()
        self._type_parrot = ""
        self._wingspan = 1
        self.__converting_json_to_object(json_data)

    def __converting_json_to_object(self, json_data):
        try:
            self.type_parrot = json_data["type_parrot"]
            self.wingspan = json_data["wingspan"]
        except KeyError:
            raise KeyError("В файле не верно указан ключ для значения")

    @property
    def type_parrot(self):
        return self._type_parrot

    @type_parrot.setter
    def type_parrot(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Вид должен быть строкой, получено {type(value).__name__}")
        self._type_parrot = value

    @property
    def wingspan(self):
        return self._wingspan

    @wingspan.setter
    def wingspan(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Размах крыльев должен быть числом, получено {type(value).__name__}")
        if value <= 0:
            raise ValueError("Размах крыльев должен быть положительным")
        self._wingspan = value

    def __hash__(self):
        return hash((self._type_parrot, self._wingspan))