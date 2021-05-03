from random import choice
from os import system

# Declare game variables

words = ['fortnite', 'tony', 'chess', 'florida', 'coding', 'apple', 'beach', 'raptor', 'charlie']
game_over = False



#### Functions that help run game
def hangman():
    global game_over
    word = choice(words) # randomly chooses a word from words list and it becomes the word the user tries to guess
    words.remove(word)
    guessed, lives, try_again = [], 7, None
    hidden_word = ["_"] * len(word)
    while game_over is False:
        #Creates underscores of the length of word for user to visualize the word and fills when guessed correctly.

        print(f"Your guessed letters: {guessed}")
        print(f"Word to guess: {''.join(hidden_word)}")
        print(f"Lives: {lives}")
        if hidden_word == word:
            print("You win!")
            if len(words) > 0:
                play_again()
            else:
                print("I'm all out of words. You win!")
                game_over == True
                break
        ans = input("type quit or guess a letter: ").lower().strip()
        system("clear")
        if ans == "quit":
            print("Thanks for playing.")
            game_over = True
            break
        elif ans == word:
            print(word)
            print("congratulations, you guessed the word correctly!")
            play_again()
        elif len(ans) != 1:
            print("Please only type 1 letter at a time.")
        elif ans == False or ans == " ":
            print('Please type a single letter')
        elif ans in word and ans not in guessed: #check if letter in word
            print("You guessed correctly!")
            guessed.append(ans)
            # create a loop to change underscore to proper letter
            for i in  range(len(word)):
                if word[i] == ans: #Compares values at indexes
                    hidden_word[i] = ans
            if word == ''.join(hidden_word):
                print("Congratulations, you guessed it correctly!")
                play_again()
        elif ans in guessed:
                print("You already guessed that. Try again")
        else:
            lives -= 1
            print("Incorrect, you lost a life.")
            guessed.append(ans) # adds ans to guessed list
            if lives == 0:
                print("You lost all your lives, you lost!")
                play_again()




def play_again():
    global game_over
    try_again = None
    while try_again not in ("yes", 'y', 'n', 'no'):
        try_again = input("play again? y/n\n").lower().strip()
    if try_again == "y" or try_again == "yes":
        system("clear")
        hangman()
    else:
        print('Thanks for playing!')
        game_over = True

hangman()
