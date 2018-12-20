"""
Comparing two lists
Lukasz Szulc
lukasz.szulc@op.pl

The function gets 2 variables:
x = the list of numbers in integer format
y = the integer "n" which define the "1-n" elements list to compare
Function compare these lists and print a difference.
"""


def n_list(x, y):
    check_list =[]
    for i in range(y):
        check_list.append(i+1)
    difference_list = list(set(check_list) - set(x))
    print(difference_list)


n_list([2, 3, 7, 4, 9], 10)