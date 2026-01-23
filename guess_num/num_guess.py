
# guessing game

import contextlib


secret_number = 4
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number (1-10): "))
    if guess != secret_number:
        print("Errr try agan!")

print("Omg u did it!")

dev_names = ['Bob', 'Potato', 'Jerry']

for devs in dev_names:
    if devs == 'Potato':
        continue
    print(devs)


words = ['latter', 'sky', 'blue', 'stars', 'pizza']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"{word} contains a vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels.")


health = 5
attack = 5

if health == attack:
    print("Damage done")
    health -= attack
    print(f"{health}")
else:
    print("No damage done")
    print(f"{health}")


languages = ['English', 'Spanish', 'French']

for index, langauge in enumerate(languages):
    print(f'Index {index} and langauge {langauge}')

numbers = [2, 6, 3, 34, 2, 6, 15]

for index, number in enumerate(numbers, 0):
    print(f"Index {index} and number {number}")

players = ['Cat', 'Human', 'Ape']
ids = [1, 2, 3, 4]

for name, id in zip(players, ids):
    print(f'Name: {name}')
    print(f"ID: {id}")


