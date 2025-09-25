from datetime import datetime


class Checker:
    @staticmethod
    def check_command(command: str, list_command: list):
        command = command.lower()
        for com in list_command:
            if com.lower() == command:
                return
        else:
            raise ValueError(f"Неизвестная команда: '{command}'. Допустимые команды: {list_command}")

    @staticmethod
    def check_animal(animal: str, list_animal: list):
        animal = animal.lower()
        for anim in list_animal:
            if anim.lower() == animal:
                return
        else:
            raise ValueError(f"Неизвестное животное: '{animal}'. Допустимые животные: {list_animal}")

    @staticmethod
    def check_date_str(str_date: str):
        if not isinstance(str_date, str):
            raise TypeError(f"Дата должна быть строкой, получено {type(str_date).__name__}")
        if not str_date.strip():
            raise ValueError(f"Дата не может быть пустой строкой, получено {type(str_date).__name__}.")
        try:
            datetime.strptime(str_date, '%d.%m.%Y').date()  # Парсинг dd.mm.yyyy
            return
        except ValueError:
            raise ValueError(f"Дата указана не в формате dd.mm.yyyy: '{str_date}'")