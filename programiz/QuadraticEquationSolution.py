import cmath

a, b, c = input('Enter cofficients of Quadratic Equation:- ').split(', ')
a = int(a)
b = int(b)
c = int(c)

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/2*a
sol2 = (-b+cmath.sqrt(d))/2*a

print(' The solutions are {0} and {1}'.format(sol1, sol2))
