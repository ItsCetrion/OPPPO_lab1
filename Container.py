class Container:
    def __init__(self):
        self.__list_object = list()

    def add(self, obj):
        self.__list_object.append(obj)

    def deleted_with_condition(self, value, relationship, target):
        buffer_list_object = []
        for obj in self.__list_object:
            for field, data in vars(obj).items():
                if field.lstrip("_") == value and self.__comparison(data, relationship, target):
                    buffer_list_object.append(obj)
        self.__list_object = self.__xor_lists_by_id(buffer_list_object)

    @staticmethod
    def __comparison(data, relationship, target):
        if relationship == ">=":
            return data >= target
        elif relationship == "<=":
            return data <= target
        elif relationship == "==":
            return data == target
        elif relationship == "!=":
            return data != target
        elif relationship == ">":
            return data > target
        elif relationship == "<":
            return data < target
        else:
            raise ValueError(f"Неизвестный оператор: {relationship}")

    def __xor_lists_by_id(self, buffer_list_object):
        set1 = set(buffer_list_object)
        set2 = set(self.__list_object)
        return list(set1 ^ set2)

    def print(self):
        for obj in self.__list_object:
            print(f"\033[96m\033[1mAnimal: {type(obj).__name__}")
            for field, value in vars(obj).items():
                print(f"  {field.lstrip('_')}: {value}")
            print("\033[0m-" * 20)

    def clear(self):
        self.__list_object.clear()
