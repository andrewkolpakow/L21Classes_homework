from entity.abstract_storage import AbstractStorage

class BaseStorage(AbstractStorage):

    def __init__(self, items, capacity):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:
        #Проверяем достаточно ли места
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        #Добавляем товар
        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name: str, amount: int) -> None:
        #Проверяем достаточно ли товара на складе
        if name not in self.__items or self.__items[name] < amount:
            raise NotEnoughProduct

        #Вычитаем необходимое количество товара, если количество товара становится 0, удаляем позицию со склада
        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self) -> int:
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)

