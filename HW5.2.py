import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Функція-генератор, яка ідентифікує всі дійсні числа текста та повертає їх.

    :param text: Вхідний текст для аналізу
    :return: Генератор чисел
    """
    # Регулярний вираз для знаходження дійсних чисел
    number_pattern = re.compile(r'\b\d+(\.\d+)?\b')
    for match in number_pattern.finditer(text):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Функція для обчислення загальної суми дійсних чисел текста,
    використовуючи генератор чисел.

    :param text: Вхідний текст для аналізу
    :param func: Функція-генератор для отримання чисел
    :return: Загальна сума чисел
    """
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 та 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

