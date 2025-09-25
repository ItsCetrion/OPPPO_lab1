import json
from Model import Cat, Dog, Parrot
from Container import Container
from Checker import Checker
import time
import sys
import keyboard
import tkinter as tk
from tkinter import filedialog

LIST_COMMAND = ["add", "rem", "print", "clear"]
LIST_ANIMAL = ["dog", "cat", "parrot"]


def spliter(string: str) -> list:
    split_list = string.split(" ", 1)
    return split_list


def controller_command(split_data: list) -> None:
    command = split_data[0].lower()
    Checker.check_command(command, LIST_COMMAND)
    if command == LIST_COMMAND[0]:
        obj = create_object(split_data[1])
        container.add(obj)
    elif command == LIST_COMMAND[1]:
        json_data = convert_strJSON_in_JSON(split_data[1])
        container.deleted_with_condition(json_data["value"], json_data["operator"], json_data["target"])
    elif command == LIST_COMMAND[2]:
        container.print()
    elif command == LIST_COMMAND[3]:
        container.clear()


def create_object(json_string):
    json_data = convert_strJSON_in_JSON(json_string)
    try:
        animal = json_data["animal"].lower()
    except KeyError:
        raise KeyError("Неизвестный ключ для животного. Допустимый ключ: animal")
    Checker.check_animal(animal, LIST_ANIMAL)
    if animal == LIST_ANIMAL[0]:
        object_ = Dog.Dog(json_data)
        return object_
    elif animal == LIST_ANIMAL[1]:
        object_ = Cat.Cat(json_data)
        return object_
    elif animal == LIST_ANIMAL[2]:
        object_ = Parrot.Parrot(json_data)
        return object_


def convert_strJSON_in_JSON(json_string):
    try:
        json_data = json.loads(json_string)
        return json_data
    except json.JSONDecodeError:
        raise TypeError("Объект невозможно преобразовать в JSON")
def file_read_and_clear(file_path):
    counter_line = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                counter_line += 1
                line = line.strip()
                if line == "":
                    continue
                try:
                    split_data = spliter(line)
                    for index, par in enumerate(split_data):
                        split_data[index] = par.strip()
                    controller_command(split_data)
                except Exception as ex:
                    error_msg = f"Ошибка в строке {counter_line}: {line}"
                    print(f"❌ {error_msg}")
                    raise
    except FileNotFoundError:
        print(f"❌ Файл не найден: {file_path}")
    except Exception as ex:
        print(f"❌ Общая ошибка: {str(ex)}")


def waiting_dots_until_keypress():
    print("Ждем ответа пользователя (нажмите любую клавишу)\n", end="", flush=True)

    sleeping_faces = ["😴", "🥱", "😪"]
    face_index = 0
    key_pressed = False

    def on_key_press(event):
        nonlocal key_pressed
        key_pressed = True

    keyboard.on_press(on_key_press)

    try:
        while not key_pressed:
            for j in range(4):
                if key_pressed:
                    break
                sys.stdout.write('\b' * (j + 2))
                sys.stdout.write(sleeping_faces[face_index] + " " + '.' * j)
                sys.stdout.flush()
                time.sleep(0.3)
            if key_pressed:
                break
            face_index = (face_index + 1) % len(sleeping_faces)
            sys.stdout.write('\b' * 5)
            sys.stdout.flush()
    finally:
        keyboard.unhook_all()
    sys.stdout.write('\b' * 50)


def select_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilename(
        title="Выберите файл для загрузки",
        filetypes=[
            ("Текстовые файлы", "*.txt"),
        ]
    )
    root.destroy()
    return file_path


if __name__ == '__main__':
    print(f"\033[36mПример заполнения файла животными:\n"
          "ADD {'Animal': 'Cat', 'breed': 'Британец', 'age': 5, 'coat_color': 'Серый'}\n"
          "ADD {'Animal': 'Dog', 'breed': 'Бульдог', 'age': 4, 'weight': '34'}\n"
          "ADD {'Animal': 'Parrot', 'type_parrot': 'Пернатый', 'wingspan': 5.5}\n"
          "----------------------\n"
          "Пример условного удаления:\n"
          "REM {'value': 'age','operator': '>' , 'target': 4}\n"
          "----------------------\n"
          "PRINT - Функция вывода содержимого внутреннего контейнера на экран\n"
          "CLEAR - Полная очистка контейнера\n"
          "----------------------\n")

    container = Container()
    while True:
        answer = input("\033[32mХотите загрузить файл? (Да/Нет): \033[0m")
        if answer.lower() == "да":
            file_read_and_clear(select_file())
        elif answer.lower() == "нет":
            waiting_dots_until_keypress()
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'")

