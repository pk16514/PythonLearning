# Problem-1
"""
Iterate through the list so that if the character ‘m’ is in the string, then it
should be added to a new list called m_list. Hint: Because this isn’t just a list
of lists, think about what type of object you want your data to be stored in. Conditionals may help you.
"""

d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat',
     ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur',
     'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']
strings = []


def word_extracted(lst):
    for item in lst:
        if type(item) == str:
            strings.append(item)
        if type(item) == list:
            word_extracted(item)
    return strings


m_list = list(filter(lambda x: 'm' in x, word_extracted(d)))
print(m_list)
print()

# Problem-2


"""
The nested dictionary, pokemon, shows the number of various Pokemon that each person has
caught while playing Pokemon Go. Find the total number of rattatas, dittos, and pidgeys
caught and assign to the variables r, d, and p respectively. Do not hardcode. Note: Be aware
that not every trainer has caught a ditto.
"""

pokemon = {'Trainer1':
    {'normal': {'rattatas': 15, 'eevees': 2, 'ditto': 1}, 'water': {'magikarps': 3}, 'flying': {'zubats': 8, 'pidgey': 12}},
    'Trainer2':
    {'normal': {'rattatas': 25, 'eevees': 1}, 'water': {'magikarps': 7}, 'flying': {'zubats': 3, 'pidgey': 15}},
    'Trainer3':
    {'normal': {'rattatas': 10, 'eevees': 3, 'ditto': 2}, 'water': {'magikarps': 2}, 'flying': {'zubats': 3, 'pidgey': 20}},
    'Trainer4':
    {'normal': {'rattatas': 17, 'eevees': 1}, 'water': {'magikarps': 9}, 'flying': {'zubats': 12, 'pidgey': 14}}
}

r = 0
d = 0
p = 0
for trainer in pokemon:
    r += pokemon[trainer]['normal'].get('rattatas', 0)
    d += pokemon[trainer]['normal'].get('ditto', 0)
    p += pokemon[trainer]['flying'].get('pidgey', 0)

print(r, p, d)
print()

# Problem-3


"""
Below, we have provided a nested list called big_list. Use nested iteration to create
a dictionary, word_counts, that contains all the words in big_list as keys, and the
number of times they occur as values.
"""

big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]

word_counts = {}

for word in word_extracted(big_list):
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
print()

# Problem-4


"""
Provided is a dictionary that contains pokemon go player data, where each player reveals the
amount of candy each of their pokemon have. If you pooled all the data together, which pokemon
has the highest number of candy? Assign that pokemon to the variable most_common_pokemon.
"""


pokemon_go_data = {'bentspoon':
                  {'Rattata': 203, 'Pidgey': 120, 'Drowzee': 89, 'Squirtle': 35, 'Pikachu': 3, 'Eevee': 34, 'Magikarp': 300, 'Paras': 38},
                  'Laurne':
                  {'Pidgey': 169, 'Rattata': 245, 'Squirtle': 9, 'Caterpie': 38, 'Weedle': 97, 'Pikachu': 6, 'Nidoran': 44, 'Clefairy': 15, 'Zubat': 79, 'Dratini': 4},
                  'picklejarlid':
                  {'Rattata': 32, 'Drowzee': 15, 'Nidoran': 4, 'Bulbasaur': 3, 'Pidgey': 56, 'Weedle': 21, 'Oddish': 18, 'Magmar': 6, 'Spearow': 14},
                  'professoroak':
                  {'Charmander': 11, 'Ponyta': 9, 'Rattata': 107, 'Belsprout': 29, 'Seel': 19, 'Pidgey': 93, 'Shellder': 43, 'Drowzee': 245, 'Tauros': 18, 'Lapras': 18}}

d = {}
for player in pokemon_go_data:
    for pokemon in pokemon_go_data[player]:
        d[pokemon] = d.get(pokemon, 0) + pokemon_go_data[player][pokemon]

sorted_d = sorted(d, key=lambda x: d[x], reverse=True)
most_common_pokemon = sorted_d[0]
print(sorted_d)
