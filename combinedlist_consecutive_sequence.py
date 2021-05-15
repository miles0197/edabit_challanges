#Combined Consecutive Sequence
#Write a function that returns True if two lists, when combined, form a consecutive sequence.

#Examples
#consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

#consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

#consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

#consecutive_combo([44, 46], [45]) ➞ True


#def consecutive_combo(lst1,lst2):
#    lst3 = lst1 + lst2
#    if sorted(lst3) == list(range(min(lst3), max(lst3)+1)):
#        return True
#    else:
#        return False


#print(consecutive_combo([1,2,3,4,5,10,11],[32,10,11,123]))


def consecutive(lst1):
    if sorted(lst1) == list(range(min(lst1), max(lst1)+1)):
        return True
    else:
        return False

print(consecutive([1,2,3,4,5,9,8,6,10]))
