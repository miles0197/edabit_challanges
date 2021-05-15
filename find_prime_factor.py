
def is_prime(n):
	factors = list()
	divisor = 2 
	while divisor <= n:
		if (n%divisor) == 0:
			factors.append(divisor)
			n = n/divisor
		else:
			divisor +=1 
	return factors


print(is_prime(100))