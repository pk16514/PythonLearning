"""
1. This project will take you through the process of implementing a simplified version of the game
   Wheel of Fortune. Here are the rules of our game:

   1. There are num_human human players and num_computer computer players.
       --> Every player has some amount of money ($0 at the start of the game)
       --> Every player has a set of prizes (none at the start of the game)

   2. The goal is to guess a phrase within a category. For example:
       --> Category: Artist & Song
       --> Phrase: Whitney Houston’s I Will Always Love You

   3. Players see the category and an obscured version of the phrase where every alphanumeric character
      in the phrase starts out as hidden (using underscores: _):
       --> Category: Artist & Song
       --> Phrase: _______ _______'_ _ ____ ______ ____ ___

   4. Note that case (capitalization) does not matter

   5. During their turn, every player spins the wheel to determine a prize amount and:
       --> If the wheel lands on a cash square, players may do one of three actions:

            --> Guess any letter that hasn’t been guessed by typing a letter (a-z)
                 --> Vowels (a, e, i, o, u) cost $250 to guess and can’t be guessed if the player doesn’t
                     have enough money. All other letters are “free” to guess
                 --> The player can guess any letter that hasn’t been guessed and gets that cash amount
                     for every time that letter appears in the phrase
                 --> If there is a prize, the user also gets that prize (in addition to any prizes they
                     already had)
                 --> If the letter does appear in the phrase, the user keeps their turn. Otherwise, it’s
                     the next player’s turn
                 --> Example: The user lands on $500 and guesses ‘W’
                      --> There are three W’s in the phrase, so the player wins $1500

            --> Guess the complete phrase by typing a phrase (anything over one character that isn’t ‘pass’)
                 --> If they are correct, they win the game
                 --> If they are incorrect, it is the next player’s turn

            --> Pass their turn by entering 'pass'

       --> If the wheel lands on “lose a turn”, the player loses their turn and the game moves on to the
           next player

       --> If the wheel lands on “bankrupt”, the player loses their turn and loses their money but they
           keep all of the prizes they have won so far.

   6. The game continues until the entire phrase is revealed (or one player guesses the complete phrase)

   —

   First, let’s learn about a few functions and methods that we’ll use along the way to do this project.
   There are no questions to answer in the next four active code windows. They are just here to introduce
   you to some functions and methods that you may not be aware of. The active code window that starts with
   “Part A” is where you are first asked to complete code.

   —

   The time.sleep(s) function (from the time module) delays execution of the next line of code for s seconds.
   You’ll find that we can build a little suspense during gameplay with some well-placed delays. The game
   can also be easier for users to understand if not everything happens instantly.

2. The random module includes several useful methods for generating and using random numbers, including:

   1. random.randint(min, max) generates a random number between min and max (inclusive)

   2. random.choice(L) selects a random item from the list L

3. There are also several string methods that we haven’t gone over in detail but will use for this project:

   1. .upper() converts a string to uppercase (the opposite is .lower())

   2. .count(s) counts how many times the string s occurs inside of a larger string

4. We’re going to define a few useful methods for you:

   1. getNumberBetween(prompt, min, max) repeatedly asks the user for a number between 'min' and 'max'
      with the prompt 'prompt'

   2. spinWheel() simulates spinning the wheel and returns a dictionary with a random prize

   3. getRandomCategoryAndPhrase() returns a tuple with a random category and phrase for players to guess

   4. obscurePhrase(phrase, guessed) returns a tuple with a random category and phrase for players to guess

   — Take some time to read their implementations below.

Part A: WOFPlayer
We’re going to start by defining a class to represent a Wheel of Fortune player, called WOFPlayer.
Every instance of WOFPlayer has three instance variables:
   1. .name: The name of the player (should be passed into the constructor)
   2. .prizeMoney: The amount of prize money for this player (an integer, initialized to 0)
   3. .prizes: The prizes this player has won so far (a list, initialized to [])

Of these instance variables, only name should be passed into the constructor.
It should also have the following methods (note: we will exclude self in our descriptions):
   1. .addMoney(amt): Add amt to self.prizeMoney
   2. .goBankrupt(): Set self.prizeMoney to 0
   3. .addPrize(prize): Append prize to self.prizes
   4. .__str__(): Returns the player’s name and prize money in the following format:
      Steve ($1800) (for a player with instance variables .name == 'Steve' and prizeMoney == 1800)

Part B: WOFHumanPlayer
Next, we’re going to define a class named WOFHumanPlayer, which should inherit from WOFPlayer (part A).
This class is going to represent a human player. In addition to having all of the instance variables
and methods that WOFPlayer has, WOFHumanPlayer should have an additional method:
   1. .getMove(category, obscuredPhrase, guessed): Should ask the user to enter a move (using input())
      and return whatever string they entered.
      .getMove()’s prompt should be:
        {name} has ${prizeMoney}

        Category: {category}
        Phrase:  {obscured_phrase}
        Guessed: {guessed}

        Guess a letter, phrase, or type 'exit' or 'pass':

      For Example:
        Steve has $200

        Category: Places
        Phrase: _L___ER N____N_L P_RK
        Guessed: B, E, K, L, N, P, R, X, Z

        Guess a letter, phrase, or type 'exit' or 'pass':

The user can then enter:
   1. 'exit' to exit the game
   2. 'pass' to skip their turn
   3. a single character to guess that letter
   4. a complete phrase (a multi-character phrase other than 'exit' or 'pass') to guess that phrase

Note- .getMove() does not need to enforce anything about the user’s input; that will be done via
      the game logic that we define in the next ActiveCode window.

Part C: WOFComputerPlayer
Finally, we’re going to define a class named WOFComputerPlayer, which should inherit from WOFPlayer
(part A). This class is going to represent a computer player.

Every computer player will have a difficulty instance variable. Players with a higher difficulty
generally play “better”. There are many ways to implement this. We’ll do the following:
   1. If there aren’t any possible letters to choose (for example: if the last character is a vowel
      but this player doesn’t have enough to guess a vowel), we’ll 'pass'
   2. Otherwise, semi-randomly decide whether to make a “good” move or a “bad” move on a given turn
      (a higher difficulty should make it more likely for the player to make a “good” move)

       --> To make a “bad” move, we’ll randomly decide on a possible letter.

       --> To make a “good” move, we’ll choose a letter according to their overall frequency in the
           English language.

In addition to having all of the instance variables and methods that WOFPlayer has, WOFComputerPlaye
should have:

Class variable
   1. .SORTED_FREQUENCIES: Should be set to 'ZQXJKVBPYGFWMUCLDRHSNIOATE', which is a list of English
      characters sorted from least frequent ('Z') to most frequent ('E'). We’ll use this when trying
      to make a “good” move.

Additional Instance variable
   1. .difficulty: The level of difficulty for this computer (should be passed as the second argument
      into the constructor after .name)

Methods
   1. .smartCoinFlip(): This method will help us decide semi-randomly whether to make a “good” or “bad”
      move. A higher difficulty should make us more likely to make a “good” move. Implement this by
      choosing a random number between 1 and 10 using random.randint(1, 10) (see above) and returning
      True if that random number is greater than self.difficulty. If the random number is less than or
      equal to self.difficulty, return False.

   2. .getPossibleLetters(guessed): This method should return a list of letters that can be guessed.

       --> These should be characters that are in LETTERS ('ABCDEFGHIJKLMNOPQRSTUVWXYZ') but not in the
           guessed parameter.

       --> Additionally, if this player doesn’t have enough prize money to guess a vowel
           (variable VOWEL_COST set to 250), then vowels (variable VOWELS set to 'AEIOU') should not be
           included

   3. .getMove(category, obscuredPhrase, guessed): Should return a valid move.

       --> Use the .getPossibleLetters(guessed) method described above.

       --> If there aren’t any letters that can be guessed (this can happen if the only letters left
           to guess are vowels and the player doesn’t have enough for vowels), return 'pass'

       --> Use the .smartCoinFlip() method to decide whether to make a “good” or a “bad” move
            --> If making a “good” move (.smartCoinFlip() returns True), then return the most frequent
                (highest index in .SORTED_FREQUENCIES) possible character

            --> If making a “bad” move (.smartCoinFlip() returns False), then return a random character
                from the set of possible characters (use random.choice())

Putting it together: Wheel of Python

Below is the game logic for the rest of the “Wheel of Python” game. We have implemented most of the game
logic. Start by carefully reading this code and double checking that it all makes sense. Then, paste your
code from the previous code window in the correct places below.

Note 1: we added the following code to ensure that the Python interpreter gives our game time to run:
               import sys
               sys.setExecutionLimit(600000)
        sys.setExecutionLimit(ms) says that we should be able to run our program for ms milliseconds
        before it gets stopped automatically.

Note 2: As you play, you will need to keep scrolling down to follow the game.
"""

import random
import json
import time


letters = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'


def getNumberBetween(prompt, min, max):
    userinp = input(prompt)

    while True:
        try:
            n = int(userinp)

            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError:
            errmessage = '{} is not a number'.format(userinp)

        userinp = input('{}\n{}'.format(errmessage, prompt))


def spinWheel():
    with open("wheel.json", "r") as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)


def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase = random.choice(phrases[category])
        return (category, phrase.upper())


def obscurePhrase(phrase, guessed):
    rv = ""
    for char in phrase:
        if (char in letters) and (char not in guessed):
            rv += "_"
        else:
            rv += char
    return (rv, guessed)


def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))


class WOFPlayer:

    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)


class WOFHumanPlayer(WOFPlayer):

    def getMove(self, category, obscuredPhrase, guessed):
        prompt = """
            {name} has ${prizeMoney}

            Category: {category}
            Phrase:  {obscured_phrase}
            Guessed: {guessed}

            Guess a letter, phrase, or type 'exit' or 'pass':
            """.format(name=self.name, prizeMoney=self.prizeMoney, category=category, obscured_phrase=obscuredPhrase, guessed=guessed)
        move = input(prompt)
        return move


class WOFComputerPlayer(WOFPlayer):

    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.name = name
        self.difficulty = difficulty

    def smartCoinFlip(self):
        rand_no = random.randint(1, 10)
        if rand_no > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        possible_guess = []
        possible_guess_without_vowels = []

        for letter in LETTERS:
            if letter not in guessed:
                possible_guess.append(letter)

        for char in possible_guess:
            if char not in VOWELS:
                possible_guess_without_vowels.append(char)

        if self.prizeMoney < 250:
            return possible_guess_without_vowels
        elif self.prizeMoney > 250:
            return possible_guess

    def getMove(self, category, obscuredPhrase, guessed):
        can_be_guessed = self.getPossibleLetters(guessed)

        if can_be_guessed == []:
            return 'pass'
        else:
            if self.smartCoinFlip is True:
                x = self.SORTED_FREQUENCIES[:]
                for char in self.SORTED_FREQUENCIES:
                    if char not in can_be_guessed:
                        x = x.replace(char, "")
                return x[-1]
            else:
                return random.choice(can_be_guessed)


# GAME LOGIC CODE
print('=' * 15)
print('WHEEL OF PYTHON')
print('=' * 15)
print('')

num_human = getNumberBetween('How many human players?', 0, 10)

# Create the human player instances
human_players = [WOFHumanPlayer(input('Enter the name for human player #{}'.format(i + 1))) for i in range(num_human)]

num_computer = getNumberBetween('How many computer players?', 0, 10)

# If there are computer players, ask how difficult they should be
if num_computer >= 1:
    difficulty = getNumberBetween('What difficulty for the computers? (1-10)', 1, 10)

# Create the computer player instances
computer_players = [WOFComputerPlayer('Computer {}'.format(i + 1), difficulty) for i in range(num_computer)]

players = human_players + computer_players

# No players, no game :(
if len(players) == 0:
    print('We need players to play!')
    raise Exception('Not enough players')

# category and phrase are strings.
category, phrase = getRandomCategoryAndPhrase()
# guessed is a list of the letters that have been guessed
guessed = []

# playerIndex keeps track of the index (0 to len(players)-1) of the player whose turn it is
playerIndex = 0

# will be set to the player instance when/if someone wins
winner = False


def requestPlayerMove(player, category, guessed):
    while True:
        time.sleep(0.1)

        move = player.getMove(category, obscurePhrase(phrase, guessed), guessed)
        move = move.upper()
        if move == 'EXIT' or move == 'PASS':
            return move
        elif len(move) == 1:
            if move not in LETTERS:
                print('Guesses should be letters. Try again.')
                continue
            elif move in guessed:
                print('{} has already been guessed. Try again.'.format(move))
                continue
            elif move in VOWELS and player.prizeMoney < VOWEL_COST:
                print('Need ${} to guess a vowel. Try again.'.format(VOWEL_COST))
                continue
            else:
                return move
        else:
            return move


while True:
    player = players[playerIndex]
    wheelPrize = spinWheel()

    print('')
    print('-' * 15)
    print(showBoard(category, obscurePhrase(phrase, guessed), guessed))
    print('')
    print('{} spins...'.format(player.name))
    time.sleep(2)
    print('{}!'.format(wheelPrize['text']))
    time.sleep(1)

    if wheelPrize['type'] == 'bankrupt':
        player.goBankrupt()
    elif wheelPrize['type'] == 'loseturn':
        pass
    elif wheelPrize['type'] == 'cash':
        move = requestPlayerMove(player, category, guessed)
        if move == 'EXIT':
            print('Until next time!')
            break
        elif move == 'PASS':
            print('{} passes'.format(player.name))
        elif len(move) == 1:
            guessed.append(move)

            print('{} guesses "{}"'.format(player.name, move))

            if move in VOWELS:
                player.prizeMoney -= VOWEL_COST

            count = phrase.count(move)
            if count > 0:
                if count == 1:
                    print("There is one {}".format(move))
                else:
                    print("There are {} {}'s".format(count, move))

                player.addMoney(count * wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])

                if obscurePhrase(phrase, guessed) == phrase:
                    winner = player
                    break

                continue

            elif count == 0:
                print("There is no {}".format(move))
        else:
            if move == phrase:
                winner = player

                player.addMoney(wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])

                break
            else:
                print('{} was not the phrase'.format(move))

    # Move on to the next player (or go back to player[0] if we reached the end)
    playerIndex = (playerIndex + 1) % len(players)

if winner:
    # In your head, you should hear this as being announced by a game show host
    print('{} wins! The phrase was {}'.format(winner.name, phrase))
    print('{} won ${}'.format(winner.name, winner.prizeMoney))
    if len(winner.prizes) > 0:
        print('{} also won:'.format(winner.name))
        for prize in winner.prizes:
            print('    - {}'.format(prize))
else:
    print('Nobody won. The phrase was {}'.format(phrase))
