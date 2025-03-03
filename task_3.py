"""мини игра на принципе бинарного поиска."""
N = 1000


def init() -> int:
    """
    Заправшивает у игрока задуманное целое число и возвращет его

    """
    while True:
        number = input(f'Загадай число от 0 до {N}\n')
        if number.isdigit():
            if 0 <= int(number) <= N:
                return int(number)
            else:
                print("Некорректно введены данные")
        else:
            print("Некорректно введены данные")
            pass


def game(x: int) -> None:
    """
    Функция игра бинарный поиск, число x

    """
    a = 0
    c = N
    b = int((c + a) / 2)
    while True:
        print('П - твоё число больше', b)
        pr = input()
        if pr == 'да':
            a = b
            b = int((c + a) / 2)
        elif pr == 'нет':
            c = b
            b = int((c + a) / 2)
        else:
            print('Некоректный ответ')
        if b == x:
            print('Вы загадали число ', b)
            break


if __name__ == "__main__":
    x = init()
    game(x)
