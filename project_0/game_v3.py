"""Угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

def game_predict(number: int = 1) -> int:
    """Угадываем число с учетом диапазона
    Args:
        number (int, optinal): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    
    count = 0
    first = 1
    last = 100
    
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


def score_game(game_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывается число
    
    Args:
        game_predict ([type]): функция угадывания
       
    Retuns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_predict(number))

    score = int(np.mean(count_ls))
    print(f'Алгоритм угадывает число в среднем на 1000 подходов за {score} попыток')
    return score

score_game(game_predict)
