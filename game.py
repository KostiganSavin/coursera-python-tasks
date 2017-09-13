import random

number = random.randint(0, 101)

while True:

    answer = input("Введите числло: ")

    if not answer or answer == "exit":
        print("До скорой встречи!")
        break

    if not answer.isdigit():
        print("Введите правильное число")
        continue

    user_answer = int(answer)

    if user_answer > number:
        print("Число меньше")
    elif user_answer < number:
        print("Число больше")
    else:
        print("Поздравляем вы угадали!")
        break
