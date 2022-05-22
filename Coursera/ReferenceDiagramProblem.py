"""
Which of these is a correct reference diagram following the execution
of the following code?
"""

# Problem-1


lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn',
       'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]

"Check image weeka1_1 & weeka1_2 for option"

# Problem-2


x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']
print(x)
print(y)

"Check image weeka3_1, weeka3_2, weeka3_3 & weeka3_4 for option"

# Problem-3


sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = " ".join(wrds)

"Check image weeka2_1, weeka2_2, weeka2_3 & weeka2_4 for option"
