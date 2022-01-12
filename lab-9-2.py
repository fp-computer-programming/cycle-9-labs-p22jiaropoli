# Author JRI 1/10/22

def double_stuff(lst):
    for i, v in enumerate(lst):
        lst[i] *= 2
    return lst

list1 = [1, 3, "meadmeadmeadmeadmeadmeadmeadmead", 10.0]

print(double_stuff(list1))
