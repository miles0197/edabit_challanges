
def digit_occurences(start,end,digit):
	count = 0
	for i in range(start,end+1):
		count += str(i).count(str(digit))
	return count


print(digit_occurences(0,11,1))
