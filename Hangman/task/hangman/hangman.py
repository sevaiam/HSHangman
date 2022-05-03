# Write your code here
import random

words_list = ['python', 'java', 'swift', 'javascript']

games_won = 0
games_lost = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print('H A N G M A N')
menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
while menu != 'exit':
    if menu == 'play':
        word = random.choice(words_list)
        word_set = set(word)
        word_cover = "-" * (len(word))
        guess_set = set()
        attempts = 8
        while attempts > 0 and '-' in word_cover:
            print()
            print(word_cover)
            guess = input('Input a letter: ')
            while guess not in alphabet or len(guess) != 1:
                if len(guess) != 1:
                    print('Please, input a single letter.')
                    print()
                    print(word_cover)
                    guess = input('Input a letter: ')
                elif guess not in alphabet:
                    print('Please, enter a lowercase letter from the English alphabet.')
                    print()
                    print(word_cover)
                    guess = input('Input a letter: ')

            if guess in guess_set:
                print("You've already guessed this letter.")
            else:
                guess_set.add(guess)
            if guess.lower() in word_set:
                for num, letter in enumerate(word):
                    if letter == guess.lower():
                        word_cover = word_cover[:num] + letter + word_cover[num+1:]

            else:
                print("That letter doesn't appear in the word.")
                attempts -= 1

        if '-' not in word_cover:
            print()
            print(f'You guessed the word {word_cover}!')
            print('You survived!')
            games_won += 1
            pass
        else:
            print()
            print('You lost!')
            games_lost += 1
            pass
    elif menu == "results":
        print(f'You won: {games_won} times.')
        print(f'You lost: {games_lost} times.')

    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')