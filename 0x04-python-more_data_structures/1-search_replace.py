#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: x, my_list))
    for i in range(len(new_list)):
        if search == new_list[i]:
            index = (new_list.index(search))
            new_list.insert(index, replace)
            new_list.remove(search)
    return new_list
