"""Скрипт декодирует команды для спутнка """


def init() -> str:
    """

    Функция инициализации, которая проверяет корректность команд
    и возвращает строку с командами

    """
    while True:
        s = input('Введите команды для спутника')
        if s.count(')') == s.count('('):
            return s
        print("Данные введены не корректно!")


def decoder(s: str) -> None:
    """
    
    Заменает цифры и скобки на сообтветвующее число символов
    """
    while True:  # цкил пока есть скобки
        for e, x in enumerate(s):
            if x == ')':  # ищем перувую закрывающую скобку
                # обратный цикл до первой открывающей
                for y in range(e - 1, -1, -1):
                    if s[y] == '(':
                        b = y  # запомнили её индекс
                        break
                # Удаляем скобки.
                temp = s[b:e + 1].replace('(', '')
                temp = temp.replace(')', '')
                # Цифра после скобки.
                if s[b + 1].isdigit():
                    temp = temp[1:] * int(temp[0])
                # Цифра до скобки.
                if s[b - 1].isdigit():
                    b = b - 1
                    temp = temp * int(s[b])
                # Формируем новую строку.
                s = s[:b] + temp + s[e + 1:]
                break
        if s.count(')') == 0:  # Скобки закончились.
            break
    print(s)


if __name__ == "__main__":
    s = init()
    decoder(s)
