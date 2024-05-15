# Task_1

# import logging
#
# # Настройка логирования
# logging.basicConfig(filename='my_log_1.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
#
# def sum_numbers(numbers):
#
#     # Функция для суммирования чисел в списке.
#     #
#     # :param numbers: Список чисел для суммирования.
#     # :return: Сумма чисел.
#
#     try:
#         result = sum(numbers)
#         logging.info(f'Сумма чисел в списке {numbers} равна {result}.')
#         return result
#     except TypeError:
#         indices = [index for index, value in enumerate(numbers) if isinstance(value, str)]
#         return logging.error(f'Ошибка: передан неверный тип данных находиться на позиции {indices}')
#
#
# # Пример использования
# sum_numbers([1, 2, 3, 4, 5])
# sum_numbers([6, 7, 8, "A", 10])
# sum_numbers([1, 2, 3, 4, "5"])
# sum_numbers(["ssaoncasl"])

#####################################

# Task_2

# import logging
#
# # Логирование
# logging.basicConfig(filename='my_log_2.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
# def divide_numbers(x, y):
#     try:
#         result = x / y
#         logging.info(f'Division result: {result}')
#         return result
#     except ZeroDivisionError:
#         logging.error('Division by zero!')
#     except Exception as e:
#         logging.error(f'Error during division: {e}')
#
#
# divide_numbers(10, 2)
# divide_numbers(10, 0)
# divide_numbers(10, "5")
# divide_numbers(10, [1, 2, 3])

#############################

#Task_3

# import logging
#
# # Логирование
# logging.basicConfig(filename='my_log_3.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
# def count_words(text):
#     try:
#         words = text.split()
#         num_words = len(words)
#         logging.info(f'Number of words in the text: {num_words}')
#         return num_words
#     except Exception as e:
#         logging.error(f'Error counting words: {e}')
#
# count_words("The sun slowly set behind the mountains, painting the sky in shades of pink and orange.")
# count_words("As she walked through the forest, she could hear the gentle rustling of leaves underfoot.")
# count_words("The old house was rumored to be haunted, as strange noises were often heard coming from within.")
# count_words("After a long day at work, he decided to unwind by taking a stroll along the beach.")
# count_words("The city skyline looked breathtaking at night, with the lights twinkling like stars in the darkness.")
# count_words("")
# count_words(1)
# count_words([1, 2, 3, 4, 5])