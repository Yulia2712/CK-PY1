import doctest


class Buildings:
    """ Базовый класс здания. """

    def __init__(self, name: str, area: float):
        """
        Создание и подготовка к работе объекта класса здания

        :param name: Наименование здания
        :param area: Площадь здания, м2

        Примеры:
        >>> some_building = Buildings("Библиотека", 281.2)
        """
        self.name = name
        self.area = area

    @property
    def name(self):
        """
        Декоратор свойств атрибута (не позволяет его изменять)
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Проверка правильности значений атрибута
        """
        if not isinstance(name, str):
            raise TypeError("Наименование здания должно быть типа str")
        self._name = name

    @property
    def area(self):
        """
        Декоратор свойств атрибута (не позволяет его изменять)
        """
        return self._area

    @area.setter
    def area(self, area):
        """
        Проверка правильности значений атрибута
        """
        if not isinstance(area, float):
            raise TypeError("Площадь здания должна быть типа float")
        if area < 0:
            raise ValueError("Площадь здания должна быть больше или равна 0")
        self._area = area

    def __str__(self) -> str:
        """
        Метод возвращает атрибуты в виде строки

        Примеры:
        >>> some_building = Buildings("Библиотека", 281.2)
        >>> some_building.__str__()
        'Наименование здания - Библиотека. Площадь здания - 281.2 м2'
        """
        return f"Наименование здания - {self.name}. Площадь здания - {self.area} м2"

    def __repr__(self) -> str:
        """
        Метод возвращает атрибуты в виде строки Python

        Примеры:
        >>> some_building = Buildings("Библиотека", 281.2)
        >>> some_building.__repr__()
        "Buildings(name='Библиотека', area=281.2)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, area={self.area!r})"

    def fire_class(self, building_height: float) -> str:
        """
        Определение класса пожарной опасности здания

        :param building_height: Высота здания, м

        :return Класс пожарной опасности здания

        Примеры:
        >>> some_building = Buildings("Библиотека", 281.2)
        >>> some_building.fire_class(15.1)
        """
        ...

    def construction_cost(self, works_amount: (float, int)) -> (float, int):
        """
        Расчет стоимости здания

        :param works_amount: Расчетная единица объема работ

        :return Стоимость работ, у.е.

        Примеры:
        >>> some_building = Buildings("Библиотека", 281.2)
        >>> some_building.construction_cost(145.8)
        """
        ...


class Skyscrapers(Buildings):
    """ Дочерний класс небоскребы. """

    def __init__(self, name: str, area: float):
        """
        Создание и подготовка к работе объекта дочернего класса небоскребы

        :param name: Наименование здания
        :param area: Площадь здания, м2

        Примеры:
        >>> some_skyscraper = Buildings("Офисное здание", 30852.5)
        """
        super().__init__(name, area)

    # метод __str__ унаследован от базового класса

    def __repr__(self) -> str:
        """
        Метод возвращает атрибуты в виде строки Python

        Примеры:
        >>> some_skyscraper = Buildings("Офисное здание", 30852.5)
        >>> some_skyscraper.__repr__()
        "Buildings(name='Офисное здание', area=30852.5)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, area={self.area!r}"

    # метод fire_class унаследован от базового класса

    def construction_cost(self, works_amount: (float, int)) -> (float, int):
        """
        Расчет стоимости здания (причина перегрузки метода: изменение принципа расчета стоимости)

        :param works_amount: Расчетная единица объема работ

        :return Стоимость работ, у.е.
         Примеры:
        >>> some_building = Buildings("Библиотека", 281.2)
        >>> some_building.construction_cost(145.8)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
