def outer(n):
    
    def inner(temp):
        return lambda res : res + temp

    res_inner = inner(15)
    return lambda x : x * res_inner(n)

res_outer  = outer(5)
print(res_outer(10))
