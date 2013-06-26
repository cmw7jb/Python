'''
Created on May 28, 2013

@author: Cameron Wyatt
'''

"""
2 lists, a and b
a is unsorted
b is sorted
after b is entered it is padded with 0s at the beginning of len(a)
a will be merged into b, removing the 0s at the beginning
as each element is successfully inserted
"""


def get_list(list_identifier):
    """
    Prompts the user for a list identified by <list_identifier>,
        strips the whitespace around the input, and
        creates the list by splitting on the spaces in the input
    """

    return [int(x) for x in raw_input("List {}: ".format(list_identifier))
            .strip().split(" ")]


def pad_b(a, b):
    """
    Pads the beginning of list b with 0s in the amount of len(a)
    Lists are mutable and passed by reference, so we should be able to
    modify b in the function and have it change
    """

    for i in range(len(a)):
        b.insert(i, 0)


def insert_sorted(a, b):
    """
    Inserts a into b in sorted order
    Rearranges list b as it goes through, shifting elements to the left if
        they are less than the current element from list a
    """
    i = 0
    while i < len(a):
        j = 0
        while j < len(b) and a[i] > b[j]:
            if b[j] != 0:
                b[j - 1] = b[j]
            j += 1
        b[j - 1] = a[i]
        i += 1


if __name__ == '__main__':
    a = get_list("a")
    b = get_list("b")
    print "a: {}".format(a)
    print "b: {}".format(b)
    pad_b(a, b)
    print "Padded b: {}".format(b)
    insert_sorted(a, b)
    print "Sorted b: {}".format(b)
