from itertools import permutations

# Example-1


def get_permutation(string, i=0):
    if(i == len(string)):
        print("".join(string))

    for j in range(i, len(string)):
        words = [c for c in string]
        words[i], words[j] = words[j], words[i]
        words = "".join(words)
        get_permutation(words, i + 1)


get_permutation('days')

# Example-2


words = [''.join(p) for p in permutations('days')]

print(words)
