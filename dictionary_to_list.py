import math
import random

def to_list(dct):
    list = []
    for key,value in dct.items():
        list.append([key,value])
    list.sort()
    return list

print(to_list({ 'a': 1, 'b': 2 }))


##OR
#def to_list(dct):
#	return sorted(list(i) for i in d.items())


#Test.assert_equals(to_list({ 'a': 1, 'b': 2 }), [["a", 1], ["b", 2]])
#Test.assert_equals(to_list({ 'foo': 33, 'bar': 45, 'baz': 67 }), [["bar", 45], ["baz", 67], ["foo", 33]])
#Test.assert_equals(to_list({ 'shrimp': 15, 'tots': 12 }), [["shrimp", 15], ["tots", 12]])
#Test.assert_equals(to_list({}), [])
