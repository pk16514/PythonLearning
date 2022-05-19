# Problem-1


"""
Challenge The nested for loop given takes in a list of lists and combines the
elements into a single list. Do the same thing using a list comprehension for the
list L. Assign it to the variable result2.
"""


def onelist(lst):
    result = []
    for each_list in lst:
        for item in each_list:
            result.append(item)
    return result


L = [["hi", "bye"], ["hello", "goodbye"], ["hola", "adios", "bonjour", "au revoir"]]

result2 = [word for list in L for word in list]
print(result2)
print()

# Problem-2


"""
Challenge: Write code to assign to the variable class_sched all the values of the key important
classes. Do this using list comprehension.
"""


tester = {'info': [
         {"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science", 'important classes': ['SI 106', 'ENGLISH 125', 'SI 110', 'AMCULT 202']},
         {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science', "important classes": ['SI 106', 'SI 410', 'PSYCH 111']},
         {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology', 'important classes': ['WOMENSTD 220', 'SOC 101', 'ENS 384']},
         {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science', "important classes": ['SOC 101', 'AMCULT 334', 'EECS 281']},
         {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History', 'important classes': ['ENGLISH 125', 'HIST 259', 'ENGLISH 130']},
         {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior', 'important classes': ['PIANO 101', 'STUDIO 300', 'THEORY 229', 'MUSC 356']}]}


class_sched = [word for list in [item['important classes'] for item in tester['info']] for word in list]
print(class_sched)
print()

# Problem-3


"""
Challenge: Below, we have provided a list of lists that contain numbers. Using list comprehension,
create a new list threes that contains all the numbers from the original list that are divisible
by 3. This can be accomplished in one line of code.
"""

nums = [[4, 3, 12, 10], [8, 7, 6], [5, 18, 15, 7, 11], [9, 4], [24, 20, 17], [3, 5]]

threes = [num for list in nums for num in list if num % 3 == 0]
print(threes)
