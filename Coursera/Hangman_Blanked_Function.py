"""
Consider a function called possible, which determines whether a word is still possible
to play in a game of hangman, given the guesses that have been made and the current
state of the blanked word.
"""

# Method-1


def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == "_" and wc in guesses_made:
            return False
        elif bc != "_" and bc != wc:
            return False
    return True


print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))
print()
# Method-2


def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True


print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))
