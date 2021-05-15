#Filtering primes from a list

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True

    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

def filter_primes(num):
    return [i for i in num if is_prime(i)]

    
print(filter_primes([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]))


