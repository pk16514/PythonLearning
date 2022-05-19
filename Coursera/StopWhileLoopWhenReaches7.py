def check_nums(lst):
    i = 0
    updated_list = []
    while(i < len(lst)):
        if lst[i] == 7:
            break
        updated_list.append(lst[i])
        i += 1
    return updated_list


x = check_nums([4, 5, 8])
print(x)
