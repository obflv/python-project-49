#!/usr/bin/env python
from brain_games.cli import welcome_user
from random import randint
import prompt


def even(name=''):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    ROUNDS_COUNT = 3
    while ROUNDS_COUNT > 0:
        number = randint(1, 99)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if (number % 2 == 0 and answer == 'yes') or (number % 2 == 1 and answer == 'no'):
            print('Correct')
            ROUNDS_COUNT -= 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{'no' if answer == 'yes' else 'yes'}'.")
            print(f"'Let's try again, {name}!")
            return
    return

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    even(name)

if __name__ == '__main__':
    print('Welcome to the Brain Games!')
    main()