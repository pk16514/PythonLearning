"""
   1. The syntax of the sort() method is: list.sort(key=..., reverse=...)

      Alternatively, you can also use Python's built-in sorted() function
      for the same purpose.
      sorted(list, key=..., reverse=...)

      Note- The simplest difference between sort() and sorted() is: sort()
            changes the list directly and doesn't return any value, while
            sorted() doesn't change the list and returns the sorted list.

   2. By default, sort() doesn't require any extra parameters. However,
      it has two optional parameters:

      --> reverse-
          If True, the sorted list is reversed (or sorted in Descending order)

      --> key- function that serves as a key for the sort comparison

   3. The sort() method doesn't return any value. Rather, it changes the
      original list.
      If you want a function to return the sorted list rather than change
      the original list, use sorted().

   4. List items should be of same data types, otherwise it will give TypeError
"""
# Example-1


vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()

print('Sorted list:', vowels)
print('\r')

# Example-2


vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)

print('Sorted list (in Descending):', vowels)
print('\r')

# Exaample-3


def takeSecond(elem):
    return elem[1]


random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=takeSecond)

print('Sorted list:', random)
print('\r')

# Example-4


employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]


def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


employees.sort(key=get_name)
print(employees, end='\n\n')

employees.sort(key=get_age)
print(employees, end='\n\n')

employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')

# Example-4(Using Lambda function)


employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')
