#!/usr/bin/python3
def uniq_add(my_list=[]):
    def sum_list(my_list=[]):
        sum = 0
        for i in range(len(my_list)):
            sum = sum + my_list[i]
        return sum

    def remove_dup(my_list=[]):
        my_list = list(dict.fromkeys(my_list))
        return my_list

    new_list = remove_dup(my_list)
    return sum_list(new_list)
