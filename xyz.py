# def minion_game(string):
#     # your code goes here
#     vowels_index = []
#     consonants_index = []
#     for idx in range(len(string)):
#         if string[idx] in ['A', 'E', 'I', 'O', 'U']:
            
#             vowels_index.append(idx)
#         else:
#             consonants_index.append(idx)
    
#     kevin_words = []
#     for j in vowels_index:
#         k = j
#         while k != len(string):
#             kevin_words.append(string[j:k + 1])
#             k += 1
            
#     stuart_words = []
#     for l in consonants_index:
#         m = l
#         while m != len(string):
#             stuart_words.append(string[l:m + 1])
#             m += 1
    
#     stuart_score = 0
#     for substring in list(set(stuart_words)):
#         pos_ = 0
#         while pos_ != len(string):
#             x = string.find(substring, pos_)
#             if x != -1:
#                 stuart_score += 1
#                 pos_ = x + 1
#             else:
#                 break
            
#     kevin_score = 0
#     for substring in list(set(kevin_words)):
#         pos_ = 0
#         while pos_ != len(string):
#             x = string.find(substring, pos_)
#             if x != -1:
#                 kevin_score += 1
#                 pos_ = x + 1
#             else:
#                 break
            
#     if stuart_score > kevin_score:
#         print("Stuart %i" % stuart_score)
#     elif stuart_score < kevin_score:
#         print("Kevin %i" % kevin_score)
#     else:
#         print('Draw')
    
#     # if len(stuart_words) > len(kevin_words):
#     #     print("Stuart %i" % len(stuart_words))
#     # elif len(stuart_words) < len(kevin_words):
#     #     print("Kevin %i" % len(kevin_words))
#     # else:
#     #     print('Draw')
        

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
A = input().split
x = list(permutations(A[0], int(A[1])))
for val in x:
    print("".join(list(val)))

from itertools import groupby
s= input()
print(*[(len(list(j)),int(i))  for i, j in groupby(s)])