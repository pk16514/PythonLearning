"""
Read in the contents of the file SP500.txt which has monthly data for 2016 and
2017 about the S&P 500 closing prices as well as some other financial
indicators including the “Long Term Interest Rate”, which is interest rate paid
on 10-year U.S. government bonds.
Write a program that computes the average closing price (the second column,
labeled SP500) and the highest long-term interest rate(6th column). Both should
be computed only for the period from June 2016 through May 2017. Save the
results in the variables mean_SP and max_interest.
"""

fhand = open('SP500.txt')

lst1 = []
lst2 = []

for line in fhand:
    data = line.split(',')
    lst1.append(data[1])
    lst2.append(data[5])

SP = lst1[6:18]
Interest = lst2[6:18]
mean_SP = sum([float(i) for i in SP]) / len(SP)
max_interest = max([float(i) for i in Interest])

print(mean_SP, max_interest)
