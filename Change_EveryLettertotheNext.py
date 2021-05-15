#def move(word):
#    alpha='abcdefghijklmnopqrstuvwxyz'
#    new_word=''
#    for i in word:
#        new_word+=alpha[alpha.index(i)+1]
#    return new_word
	
import string 

def move(word):
    alpha = string.ascii_lowercase
    new = ""
    for i in word:
        if i in alpha:
            new += alpha[alpha.index(i) + 1]
    return new

print(move("ahmet"))
