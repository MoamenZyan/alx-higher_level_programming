#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    total = 0
    length = len(new_list)
    for i in range(0, length):
        total += new_list[i]
        for j in range(i + 1, length):
            if new_list[i] == new_list[j]:
                new_list[j] = 0
    return (total)
