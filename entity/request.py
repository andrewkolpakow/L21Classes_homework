from exception import InvalidRequest, InvalidStorageName
from entity.abstract_storage import AbstractStorage

class Request:

    def __init__(self, request: str, storages: dict[str, AbstractStorage]):
        #Разделяем запрос пользователя по пробелу
        splitted_request = request.lower().split(' ')
        if len(splitted_request) != 7:
            raise InvalidRequest

        #Сохраняем данные из запроса пользователя в атрибуты класса
        #Доставить (0) 3 (1) печеньки (2) из (3) склад (4) в (5) магазин (6)
        self.amount = int(splitted_request[1])
        self.product = splitted_request[2]
        self.departure = splitted_request[4]
        self.destination = splitted_request[6]

        if self.departure not in storages or self.destination not in storages:
            raise InvalidStorageName