"""
Explanation

1. The default tabsize is 8. The tab stops are 8, 16 and so on. Hence, there is 5 spaces after 'xyz'
   and 3 after '12345' when you print the original string.
2. When you set the tabsize to 2. The tab stops are 2, 4, 6, 8 and so on. For 'xyz', the tab stop is 4,
   and for '12345', the tab stop is 10. Hence, there is 1 space after 'xyz' and 1 space after '12345'.
3. When you set the tabsize to 3. The tab stops are 3, 6, 9 and so on. For 'xyz', the tab stop is 6,
   and for '12345', the tab stop is 12. Hence, there are 3 spaces after 'xyz' and 1 space after '12345'.
4. When you set the tabsize to 4. The tab stops are 4, 8, 12 and so on. For 'xyz', the tab stop is 4 and
   for '12345', the tab stop is 12. Hence, there is 1 space after 'xyz' and 3 spaces after '12345'.
5  When you set the tabsize to 5. The tab stops are 5, 10, 15 and so on. For 'xyz', the tab stop is 5 and
   for '12345', the tab stop is 15. Hence, there are 2 spaces after 'xyz' and 5 spaces after '12345'.
6. When you set the tabsize to 6. The tab stops are 6, 12, 18 and so on. For 'xyz', the tab stop is 6 and
   for '12345', the tab stop is 12. Hence, there are 3 spaces after 'xyz' and 1 space after '12345'.
"""

str = "xyz\t12345\tabc"
print('Original String:', str)
print('Original String:', str.expandtabs())

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))

# tabsize is set to 3
print('Tabsize 3:', str.expandtabs(3))

# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))

# tabsize is set to 5
print('Tabsize 5:', str.expandtabs(5))

# tabsize is set to 6
print('Tabsize 6:', str.expandtabs(6))
