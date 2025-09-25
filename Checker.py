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