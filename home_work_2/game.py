import random


def display_game_field() -> None:
    """
    Функция, отображающая игровое поле.
    :return: None
    """
    for ind in range(10):
        for i in range(ind * 10, ind * 10 + 10):
            print(GAME_FIELD[i], end=' ')
        print()


def are_5_together(number: int, symbol: str, step: int, range_start: int, range_end: int) -> bool:
    """
    Функция, проверяющая есть-ли 5 заданных знаков подряд вокруг текущей точки
    (направление проверки задаётся параметрами).
    :param number: текущая точка
    :param symbol: какой знак проверяем
    :param step: шаг перемещения для проверки
    :param range_start: ограничение диапазона проверки - в начало
    :param range_end: ограничение диапазона проверки - в конец
    :return: True - есть 5 заданных знаков подряд вокруг заданной точки, False - нет
    """
    count = 1
    ind = number
    for _ in range(range_start):
        if GAME_FIELD[ind - step] == symbol:
            count += 1
            if count == 5:
                break
            ind -= step
        else:
            break
    if count < 5:
        ind = number
        for _ in range(range_end):
            if GAME_FIELD[ind + step] == symbol:
                count += 1
                if count == 5:
                    break
                ind += step
            else:
                break
    return count >= 5


def is_party_over(number: int, player: str) -> bool:
    """
    Функция, вызывающая are_5_together для проверки по горизонтали, вертикали и по двум диагоналям.
    :param number: текущая точка
    :param player: текущая игрок
    :return: True - если хоть в одном направлении есть 5 знаков подряд, False - если нет
    """
    diagonal_left_start = min(number % 10, number // 10)
    diagonal_left_end = min(9 - number % 10, 9 - number // 10)
    if (number % 10 + number // 10) > 9:
        diagonal_right_start = 9 - number % 10
        diagonal_right_end = 9 - number // 10
    else:
        diagonal_right_start = number // 10
        diagonal_right_end = number % 10
    end_party = are_5_together(number=number, symbol=player, step=1,
                               range_start=number % 10, range_end=9 - number % 10) or \
                are_5_together(number=number, symbol=player, step=10,
                               range_start=number // 10, range_end=9 - number // 10) or \
                are_5_together(number=number, symbol=player, step=11,
                               range_start=diagonal_left_start, range_end=diagonal_left_end) or \
                are_5_together(number=number, symbol=player, step=9,
                               range_start=diagonal_right_start, range_end=diagonal_right_end)
    return end_party


def human_choice() -> int:
    """
    Функция, запрашивающая выбор игрока. Проверяет корректность выбора. Если выбор некорректен, запрашивает заново.
    :return: выбор игрока
    """
    while True:
        choice = input('Выберете ячейку: ')
        if choice.isdigit() and int(choice) in EMPTY_SELLS:
            choice = int(choice)
            GAME_FIELD[choice] = ' X'
            EMPTY_SELLS.remove(choice)
            break
        else:
            print('Только цифра из свободных ячеек.')
    return choice


def machine_choice() -> int:
    """
    Функция, получающая и отображающая выбор компьютера.
    :return: выбор компьютера
    """
    choice = random.choice(EMPTY_SELLS)
    print(f'Выбор машины: {choice}')
    GAME_FIELD[choice] = ' O'
    EMPTY_SELLS.remove(choice)
    return choice


if __name__ == '__main__':
    while True:
        print('\nИгра "Обратные крестики-нолики".\nЗнак игрока - X, он ходит первым.\n'
              'Знак компьютера - O, он отвечает на ход игрока.\n')
        EMPTY_SELLS = [num for num in range(100)]
        GAME_FIELD = [str(num).zfill(2) for num in EMPTY_SELLS]
        display_game_field()
        move_count = 1
        while True:
            if move_count % 2 != 0:
                current_player = ' X'
                current_choice = human_choice()
            else:
                current_player = ' O'
                current_choice = machine_choice()
            move_count += 1
            display_game_field()
            party_over = is_party_over(number=current_choice, player=current_player)
            if party_over:
                break
        print(f'Партия окончена, знак {current_player} проиграл.')
        game_over = input('Закончить игру? (да / нет): ')
        if game_over.lower() == 'да':
            print('Игра окончена.')
            break
