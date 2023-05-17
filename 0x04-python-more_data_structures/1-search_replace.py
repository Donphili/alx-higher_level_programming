#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for j in range(len(my_list)):
        if my_list[j] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[j])
    return (new_list)
