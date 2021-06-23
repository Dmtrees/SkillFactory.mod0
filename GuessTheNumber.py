from typing import Any, Union
import numpy as np  # Импорт библиотеки numpy
# Для оптимального кол-ва попыток в угадывании числа воспользуемся алгоритмом бинарного поиска

def game_core(number):  # Функция, которая возвращает кол-во попыток, в зависимости от загадонного числа
    low_number = 1  # Первое значение интервала, в котором угадывается число
    high_number = 101  # Последнее значение интервала, в котором угадывается число
    count = 0  # Счетчик попыток
    while True:  # Бесконечный цикл
        predict = (low_number + high_number) // 2  # Присваиваем значение переменной predict
        count += 1  # Увеличиваем значение счетчика на 1 с каждой итерацией цикла
        if number > predict:  # Проверка условия путем сравнения двух чисел
            low_number = predict + 1  # При выполнении условия, присваиваем первому значению интервала - значение
            # predict, увеличенным на 1
        elif number < predict:  # Проверка условия путем сравнения двух чисел
            high_number = predict - 1 # При выполнении условия, присваиваем последнему значению интервала - значение
            # predict уменьшенным на 1
        elif number == predict: # Проверка условия, при котором осуществляется выход из цикла
            break  # Выход из цикла
    return count  # Возвращаем функции значение кол-ва попыток


def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score: Union[int, Any] = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


number = np.random.randint(1, 101)  # Загадываем случайное число
print(score_game(game_core))  # Выводим на экран значение функции
