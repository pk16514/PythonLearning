import pdb


# interactive debugging
def seq(n):
    for i in range(n):
        pdb.set_trace()
        print(i)
        return


seq(5)

# python -m pdb practice.py
# c : continue
# q: quit
# h: help
# list
# p: print
# p locals()
# p globals()
