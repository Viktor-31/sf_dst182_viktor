import numpy as np

#np.random.seed(1) # фиксируем сид для воспроизводимости
number = np.random.randint(1, 101) # загадываем число

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Начинаем угадывать с числа 50
    predict = 50
    a, b = 1, 101
    count = 0
    
    # С учетом условия больше-меньше поэтапно уменьшаем область выбора
    # случайных чисел
    while number != predict:
        count +=1
        if predict > number:
            b = predict
            predict = np.random.randint(a, predict)
        elif predict < number:
            a = predict
            predict = np.random.randint(predict, b)
            
    return count

print(game_core_v3(number))