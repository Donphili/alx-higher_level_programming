#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > len(my_list):
        return (None)
    else:
        for j in range(len(my_list)):
            if idx == j:
                return (my_list[i])
