import doctest

class PoorStudent:
    def __init__(self, hunger_level: int, amount_of_money: (int, float)):
        """
        Создание и подготовка к работе объекта "БедныйСтудент"
        :param hunger_level: Уровень голода
        :param amount_of_money: Количеество денег
        Примеры:
        >>> poor_student = PoorStudent(100, 0)  # инициализация экземпляра класса
        """
        if not isinstance(hunger_level, int):
            raise TypeError("Уровень голода должен быть типа int")
        if hunger_level <= 0:
            raise ValueError("Уровень голода должен быть положительным числом")
        self.hunger_level = hunger_level
        if not isinstance(amount_of_money, (int, float)):
            raise TypeError("Количество денег должно быть int или float")
        if amount_of_money < 0:
            raise ValueError("Количество денег не может быть отрицательным числом")
        self.amount_of_money = amount_of_money

    def is_hungry_student(self) -> bool:
        """
        Функция которая проверяет голодный ли студент
        :return: Голодный ли студент
        Примеры:
        >>> poor_student = PoorStudent(100, 0)
        >>> poor_student.is_hungry_student()
        """
        ...

    def give_money_for_student (self, money: float) -> None:
        """
        Прибавление денег студенту
        :param money: Количество денег, клоторые нужно дать студенту

        >>> poor_student = PoorStudent(100, 0)
        >>> poor_student.give_money_for_student(500)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Деньги должны быть типа int или float")
        if money < 0:
            raise ValueError("Количество денег должно быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()


import doctest

class Car:
    def __init__(self, amount_of_gasoline: (int, float), cabin_temperature: int):
        """
        Создание и подготовка к работе объекта "Машина"
        :param amount_of_gasoline: Количество бензина в бензобаке
        :param cabin_temperature: Температура в салоне
        Примеры:
        >>> car = Car (10, 20)  # инициализация экземпляра класса
        """
        if not isinstance(amount_of_gasoline, (int, float)):
            raise TypeError("Количество бензина в бензобаке должен быть типа int или float")
        if amount_of_gasoline <= 0:
            raise ValueError("Количество бензина должна быть положительным")
        self.amount_of_gasoline = amount_of_gasoline
        if not isinstance(cabin_temperature, int):
            raise TypeError("Уровень температуры в кабине должен быть типа int")
        if cabin_temperature < 20:
            raise ValueError("Температура в кабине не должна быть меньше 20")
        self.cabin_temperature = cabin_temperature

    def add_gasoline (self, gasoline: (int, float)) -> None:
        """
        Добавление бензина в бензобак
        :param gasoline: Количество добавляемого бензина
        Примеры:
        >>> car = Car (10, 20)
        >>> car.add_gasoline(10)
        """
        if not isinstance(gasoline, (int, float)):
            raise TypeError("Количество добавляемого бензина в бензобаке должен быть типа int или float")
        if gasoline < 0:
            raise ValueError("Количество добавляемого бензина должно быть положительным числом")
        ...

    def is_temperature_normal (self) -> bool:
        """
         Функция которая проверяет является ли температура нормальной
        :return: Является ли температура нормальной
        Примеры:
        >>> car = Car (10, 20)
        >>> car.is_temperature_normal()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()


import doctest

class FlowerVase:
    def __init__(self, amount_of_water: (int, float), amount_of_flowers: int):
        """
        Создание и подготовка к работе объекта "Ваза с цветами"
        :param amount_of_water: Количество воды в вазе
        :param amount_of_flowers:Количество цветов в вазе
        Примеры:
        >>> flower_vase = FlowerVase (2, 20)  # инициализация экземпляра класса
        """
        if not isinstance(amount_of_water, (int, float)):
            raise TypeError("Количество воды в вазе должно быть типа int или float")
        if amount_of_water <= 0:
            raise ValueError("Количество воды должно быть положительным")
        self.amount_of_water = amount_of_water
        if not isinstance(amount_of_flowers, int):
            raise TypeError("Количество цветов в вазе должно быть типа int")
        if amount_of_flowers < 0:
            raise ValueError("Количество цветов должно быть положительным")
        self.amount_of_flowers = amount_of_flowers

    def add_flowers (self, fresh_flower: int) -> None:
        """
        Добавление свежих цветов в вазу
        :param fresh_flower: Количество свежих цветов в вазе
        Примеры:
        >>> flower_vase = FlowerVase (2, 20)
        >>> flower_vase.add_flowers(5)
        """
        if not isinstance(fresh_flower, int):
            raise TypeError("Количество добавленных свежих цветов должно быть типа int")
        if fresh_flower < 0:
            raise ValueError("Количество добавленных свежих цветов должно быть положительным числом")
        ...

    def is_empty_vase (self) -> bool:
        """
         Функция которая проверяет есть ли в вазе вода
        :return: Является ли ваза пустой
        Примеры:
        >>> flower_vase = FlowerVase (2, 20)
        >>> flower_vase.is_empty_vase()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()