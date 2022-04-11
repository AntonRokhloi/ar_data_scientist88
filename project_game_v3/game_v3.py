"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом угадываем число ограничивая рамки подбора
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    min, max = 1, 100
    predict_number = max / 2
    
    while number != predict_number:
        count+=1
        # сужаем рамки поиска
        if number > predict_number: 
            min = predict_number 
        
        elif number < predict_number: 
            max = predict_number 
        
        predict_number = round((max + min ) / 2) # разбиваем по полам новые рамки поиска
        
            
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)