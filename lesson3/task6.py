# Task 6 Сapital letters
def int_func(text):
    return text.title()

print(int_func('text'))
user_text = input('Введите несколько слов: ')
result = int_func(user_text)
print(result)