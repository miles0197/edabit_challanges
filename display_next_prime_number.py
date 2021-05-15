# If the number is not prime, print the next number that is prime

def is_prime(num):
    for i in range(2,num):
        if num % i ==0:
            return False
    return True

def next_prime(num):
    if not is_prime(num):
        n = num + 1
        while not is_prime(n):
            n += 1
        return n
    else:
        return num


print(next_prime(6))