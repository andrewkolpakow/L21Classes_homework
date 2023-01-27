from entity.base_storage import BaseStorage
from exception import TooManyDifferentProducts

class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int=20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
    #Проверяем, что в магазине хранится менее 5 уникальных товаров
        if self.get_unique_items_count >= 5:
            raise TooManyDifferentProducts

        super().add(name, amount)