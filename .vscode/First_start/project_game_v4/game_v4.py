"""Игра угадай число.
Компьютер сам загадывает и угадывает число меньше чем за 20 попыток
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    min, max = 1, 100
    middle = round((max+min)/2)
    count = 0
    while middle != number:
        count +=1
        if middle > number:
            max = middle - 1
            middle = (max+min)//2
        else:
            min = middle + 1
            middle = (max+min)//2
            
    return (count)

def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size =(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток.")
    return (score)

# RUN
if __name__ == '__main__':
    score_game(random_predict) 