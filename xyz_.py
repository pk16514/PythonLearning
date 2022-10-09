# # my_string = "Hello"
# # print(int("0111",2))

# # x = ['educative', 'fun'][bool('')]
# # print(x)

# recipe_1 = [1, 1, 1, 3, 3, 5, 6, 5, 5, 9]
# recipe_2 = [1, 1, 5, 5, 3, 8, 4, 6]

# def func(recipe_1, recipe_2):
#     dic1 = dict()
#     dic2 = dict()

#     for i in recipe_1:
#         dic1[i] = dic1.get(i, 0) + 1

#     for j in recipe_2:
#         dic2[j] = dic2.get(j, 0) + 1

#     set1 = set(dic1)
#     set2 = set(dic2)
#     common = list(set1.intersection(set2))

#     count = [min(dic1[k], dic2[k]) for k in common]
#     lst_ = []
#     for k, c in zip(common,count):
#         lst = [k] * c
#         lst_.extend(lst)
#     return lst_


# x = func(recipe_1, recipe_2)
# print(x)

def minion_game(string):
    # your code goes here
    vowels_index = []
    consonants_index = []
    for idx in range(len(string)):
        if string[idx] in ['A', 'E', 'I', 'O', 'U']:
            vowels_index.append(idx)
        else:
            consonants_index.append(idx)
    
    kevin_score = 0
    for j in vowels_index:
        k = j
        while k != len(string):
            substring = string[j:k + 1]
            kevin_score += 1
            k += 1
            
    stuart_score = 0
    for l in consonants_index:
        m = l
        while m != len(string):
            substring = string[l:m + 1]
            stuart_score += 1
            m += 1
            
    if stuart_score > kevin_score:
        print("Stuart %i" % stuart_score)
    elif stuart_score < kevin_score:
        print("Kevin %i" % kevin_score)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)