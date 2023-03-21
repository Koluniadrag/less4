import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

operator = random.choice(['+', '-', '*'])

if operator == '+':
    answer = num1 + num2
elif operator == '-':
    answer = num1 - num2
else:
    answer = num1 * num2

user_answer = input(f"Решите выражение: {num1} {operator} {num2} = ")

if user_answer.isdigit() and int(user_answer) == answer:
    print("Правильно")
else:
    print("Неправильно")