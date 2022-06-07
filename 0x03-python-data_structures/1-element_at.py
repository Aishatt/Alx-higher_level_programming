#!/usr/bin/python3
def element_at(my_list,idx):
    """Return element at index (idx)"""
    listlen= len(my_list)
    if idx >= listlen or idx < 0:
        return None
    for i in range(listlen):
        if i == idx:
            return my_list[i]
