import random

print(20/0)
guess = int(random.randint() * 10)
n = int(input("son kirit"))
guesses = 0
while True:
    if n == guess:
        print("topding")
        break
    guesses += 1

    if guess >= 3:
        print("yutqading")
