#Question1
#get the input of 2 numbers from the user for each a and b,
#Perform a product of a X b

import itertools

a = [int(x) for x in input().split(',')]
b = [int(x) for x in input().split(',')]

print(' , '.join(str(t) for t in itertools.product(a,b)))

#Question2
#get the input for 2 numbers, try integer division, else raise error

lines = int(input())
for _ in range(lines):
	a,b = input().split()
	try:
		print(int(a) // int(b))
	except (ZeroDivisionError, ValueError) as e:
		print("Error Code: ", e)

#Question 3 
#Task
#You have a non-empty set , and you have to execute  commands given in  lines.

#The commands will be pop, remove and discard.

#Input Format

#The first line contains integer , the number of elements in the set .
#The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
#The third line contains integer , the number of commands.
#The next  lines contains either pop, remove and/or discard commands followed by their associated value.

#Constraints

#Output Format

#Print the sum of the elements of set  on a single line.

#Sample Input
#9
#1 2 3 4 5 6 7 8 9
#10
#pop
#remove 9
#discard 9
#discard 8
#remove 7
#pop 
#discard 6
#remove 5
#pop 
#discard 5

#Sample Output
#4

n = int(input())
s = set(map(int, input().split()))
print(s)
N = int(input())
for i in range(N):
    choice = input().split()
    if choice[0] == "pop":
        s.pop()
    elif choice[0] == "discard":
        s.discard(int(choice[1]))
    elif choice[0] == "remove":
        s.remove(int(choice[1]))
print(sum(s))

#Question
#You are given n words. Some words may repeat. For each word, output its number of occurrences. 
#The output order should correspond with the input order of appearance of the word.

#The first line contains the integer.
#The next n lines each contain a word.
#Output  lines.
#On the first line, output the number of distinct words from the input.
#On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

#4
#bcdef
#abcdefg
#bcde
#bcdef
#Sample Output
#3
#2 1 1
#Explanation
#There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. 
#The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
import collections
n = int(input())
words = [input().strip() for _ in range(n)]
counter_words = collections.Counter(words)
print(len(counter_words))
print(*counter_words.values())











