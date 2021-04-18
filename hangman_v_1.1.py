# import additional functions
from random import choice
from IPython.display import clear_output

# Declare game variables
words = ['fortnite', 'tony', 'chess', 'florida', 'coding' ]
word = choice(words)# randomly chooses a word from words list`
guessed, lives, game_over, try_again = [], 7, False, None # multi variable assignment

# create a list of underscores to the length of the word
guesses = ["_"] * len(word)

# create main game loop
while not game_over:
    # output game information
    hidden_word = "".join(guesses)
    print(f"Your guessed letters: {guessed}")
    print(f"Word to guess: {hidden_word}")
    print(f"Lives: {lives}")
    if hidden_word == word:
        game_over = True
        print("You win!")
        try_again = input("play again? y/n\n").lower()
        try_again = try_again.strip()

        if try_again == "y":
                game_over = False
                clear_output()
                word =choice(words)
                words.remove(word)
                lives = 7
                guessed = []
                guesses = ["_"] * len(word)

        elif try_again == "yes":
                game_over = False
                clear_output()
                word =choice(words)
                words.remove(word)
                lives = 7
                guessed = []
                guesses = ["_"] * len(word)

        elif try_again == 'n':
                print('Thanks for playing!')
                game_over = True
                continue
        elif try_again == 'no':
            print("Thanks for playing!")
            game_over = True
            continue

        else:
            try_again('Try again y/n?\n')


        if len(words) > 0 and try_again == True:
            word = choice(words)
        if len(words) == 0:
            print("I'm all out of words. You win!")
            game_over == True
            break



    ans = input("type quit or guess a letter: ").lower()
    ans = ans.strip()
    clear_output()
    if ans == "quit":
        print("Thanks for playing.")
        game_over = True
    elif len(ans) > 1:
        print("Please only type 1 letter at a time.")
    elif ans == None or ' ':
        print('Please type a single letter')
    elif ans in word and ans not in guessed: #check if letter in word
        print("You guessed correctly!")
        # create a loop to change underscore to proper letter
        for i in range (len(word)):
            if word [i] == ans: #Compares values at indexes
                guesses[i] = ans
    elif ans in guessed:
            print("You already guessed that. Try again")
    else:
        lives -= 1
        print("Incorrect, you lost a life.")
        if ans not in guessed:
            guessed.append(ans) # adds ans to guessed list
        if lives <= 0:
            print("You lost all your lives, you lost!")
            game_over = True
        elif word == hidden_word:
            print("Congratulations, you guessed it correctly!")
            game_over = True
