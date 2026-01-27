#!/usr/bin/python
# guessing game




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


HEALTH = 5
ATTACK = 5

if HEALTH == ATTACK:
    print("Damage done")
    HEALTH -= ATTACK
    print(f"{HEALTH}")
else:
    print("No damage done")
    print(f"{HEALTH}")


languages = ['English', 'Spanish', 'French']

for index, langauge in enumerate(languages):
    print(f'Index {index} and langauge {langauge}')

numbers = [2, 6, 3, 34, 2, 6, 15]

for index, number in enumerate(numbers, 0):
    print(f"Index {index} and number {number}")

players = ['Cat', 'Human', 'Ape']
ids = [1, 2, 3, 4]

for name, player_id in zip(players, ids):
    print(f'Name: {name}')
    print(f"ID: {id}")


