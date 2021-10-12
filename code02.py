from copy import deepcopy
from random import randint
def shuffle_list(lst):
    temp_1st = deepcopy(lst)
    m = len(temp_lst)
    while (m):
        m -= 1
        i = randit(0,m)
        temp_1st[m], temp_1st[i] = temp_1st[i], temp_1st[m]
        return temp_1st
        num = [1,2,3,4,5,6]
        print("Original list:", nums)
        print("\nShuffle the elements of said list:")
        print(shuffle_list(nums))