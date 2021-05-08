#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # build a list with the set's
    unified_list = list(set_1) + list(set_2)
# revisar cada posicion contra todas las demas
    dup = 0
    i = 0
# cicle to count repetition form itmes in a unified list
    for i in unified_list:
        j = 0
        dup = 0
        # verify the item with all index possition in the list
        for j in range(len(unified_list)):
            if i == unified_list[j]:
                dup += 1
        # if ites is more for 1 time in list
        if dup > 1:
            idx = 0
            # cicle to remove repeated items
            while idx < dup:
                unified_list.remove(i)
                idx += 1
    return unified_list
