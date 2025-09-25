from datetime import date, datetime


class HomeAnimal:
    def __init__(self, json_data):
        self._name = ""
        self._DateLastVet = date.today()
        self._converting_json_to_object(json_data)

    def _converting_json_to_object(self, json_data):
        try:
            self.name = json_data["name"]
            self.date_last_veterinarian = json_data["DateLastVet"]
        except KeyError:
            raise KeyError("В файле не верно указан ключ для значения")

    @property
    def name(self):
        return self._name

    @property
    def date_last_veterinarian(self):
        return self._DateLastVet

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Имя должен быть строкой, получено {type(value).__name__}")
        if not value.strip():
            raise ValueError(f"Имя не может быть пустой строкой, получено {type(value).__name__}.")
        self._name = value

    @date_last_veterinarian.setter
    def date_last_veterinarian(self, str_date):
        if not isinstance(str_date, str):
            raise TypeError(f"Дата должна быть строкой, получено {type(str_date).__name__}")
        if not str_date.strip():
            raise ValueError(f"Дата не может быть пустой строкой, получено {type(str_date).__name__}.")
        try:
            parsed_date = datetime.strptime(str_date, '%d.%m.%Y').date()  # Парсинг dd.mm.yyyy
            self._DateLastVet = parsed_date
        except ValueError:
            raise ValueError(f"Дата указана не в формате dd.mm.yyyy: '{str_date}'")