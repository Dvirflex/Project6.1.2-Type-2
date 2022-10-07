


def shift_left(my_list):
    my_list.append(my_list.pop(len(my_list)-3))
    print(my_list)


shift_left(['monkey', 2.0, 1])