"""Угадай число"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    first = 1
    last = 101

    while True:
        count+=1
        number_predict = (first + last)//2 # выбираем число в середине диапазона
        
        if number_predict == number:
            break # выход из цикла, если число угадано
        
        elif number_predict > number:
            last = number_predict # диапазон смещаем влево
            
        else:
            first = number_predict # диапазон смещаем вправо
           
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)