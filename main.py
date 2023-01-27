from entity.shop import Shop
from entity.store import Store
from entity.request import Request
from exception import RequestError

store = Store(items={
    "печенька": 25,
    "собачка": 25,
    "елка": 25,
    "пончик": 3,
    "зонт":15,
    "ноутбук": 1
})
#Создаем экземпляр для теста
shop = Shop(items={
"печенька": 2,
    "собачка": 2,
    "елка": 2,
    "пончик": 1,
    "зонт": 1,
})

#mapping
storages = {'магазин': shop, 'склад': store}

def main():
    print('Добрый день!')

    while True:
        #Выводим содержимое складов
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')

        user_input = input(
            "Введите запрос в формате: Доставить 3 печеньки из склад в магазин\n"
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )

        if user_input in ("стоп", "stop"):
            break
        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue

        #Запускаем доставку
        courier = Courier(
            request = request,
            storages = storages,
        )

        try:
            courier.move()
        except CourierError as error:
            print(error.message)
            courier.cancel()


if __name__ == '__main__':
    main()