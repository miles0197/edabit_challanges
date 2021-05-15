#Your job is to create a function, that takes 3 numbers: a, b, c and returns True if the last digit of
#(the last digit of a * the last digit of b) = the last digit of c. Check examples for explanation.
#
#EXAMPLE
#last_dig(25, 21, 125) ➞ True
# The last digit of 25 is 5, the last digit of 21 is 1, and the last
# digit of 125 is 5, and the last digit of 5*1 = 5, which is equal
# to the last digit of 125(5).

def last_dig(a, b, c):
    a = int(str(a)[-1])
    b = int(str(b)[-1])
    c = int(str(c)[-1])
    d = a*b
    e = int(str(d)[-1])
    if e == c:
        return True
    else:
        return False
		

#OR
    
#def last_dig(a, b, c):
    
#   return str(a*b)[-1] == str(c)[-1]
