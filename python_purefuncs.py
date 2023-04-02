myList = [1, 2, 3]

def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(myList, 4)

print(myList)
print(new_list)