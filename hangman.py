import random

# define a dictionary of words and hints
word_dict = {"amber": "Fossil resin",
             "badge": "Authority emblem",
             "chaos": "Total disorder",
             "dwarf": "Mythical small",
             "ethos": "Moral code",
             "flair": "Stylish talent",
             "gauge": "Measure tool",
             "hatch": "Egg opening",
             "icily": "Coldly",
             "jolly": "Cheerful",
             "knack": "Skill",
             "lurks": "Hides",
             "mango": "Tropical fruit",
             "noble": "Honorable",
             "oasis": "Desert spring",
             "punch": "Hit",
             "quell": "Suppress",
             "razor": "Sharp blade",
             "sable": "Dark fur",
             "thief": "Stealer",
             "uncle": "Father's brother",
             "vixen": "Female fox",
             "witty": "Cleverly amusing",
             "xenon": "Chemical element",
             "yacht": "Luxury boat",
             "zebra": "Striped animal",
             "abide": "Live with",
             "bison": "Large mammal",
             "crave": "Desire",
             "dough": "Bread mixture"}

# pick a random word from the list
word = random.choice(list(word_dict.keys()))

# create a list to store the correctly guessed letters
correct_letters = []

# create a list to store the incorrectly guessed letters
incorrect_letters = []

# define the maximum number of incorrect guesses allowed
max_incorrect_guesses = 6

# define the hangman stages
hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

num_incorrect_guesses = 0

# loop until the game is over
while True:
    # print the current status of the game
    word_display = ""
    for letter in word:
        if letter in correct_letters:
            word_display += letter + " "
        else:
            word_display += "_ "
    
    print("Word: " + word_display)
    print("Incorrect guesses: " + ", ".join(incorrect_letters))
    print("Hint: " + word_dict[word])
    print()
    
    # check if the player has won
    if set(word) <= set(correct_letters):
        print("Congratulations, you won!")
        break
    
    # check if the player has lost
    if len(incorrect_letters) >= max_incorrect_guesses:
        print(hangman_stages[len(incorrect_letters)])
        print("Sorry, you lost. The word was " + word + ".")
        break
    
    # ask the player for a guess
    guess = input("Guess a letter: ").lower()
    if guess in word:
        print()
        print("You've got this! There is a letter "+ guess + " in this word.")
        print()
    
    # check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid guess. Please enter a single letter.")
        continue
    
    # check if the guess has already been made
    if guess in correct_letters or guess in incorrect_letters:
        print("You already guessed that letter. Please try again.")
        continue
    
    # check if the guess is correct
    if guess in word:
        correct_letters.append(guess)
    else:
        incorrect_letters.append(guess)

    # print the hangman stages
    if guess not in word:
        index = len(incorrect_letters)-1
        print()
        print(hangman_stages[index])
        print()