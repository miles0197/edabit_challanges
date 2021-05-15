def list_of_multiples(num, length):
    #return [i*num for i in range(1,length+1)]
    lst = []
    for i in range(1,length+1):
    	lst.append(i*num)
    return lst


def list_of_multiplesss (num, length):
  factor_number = 1
  factors = []
  while factor_number <= length:
    factors.append(factor_number * num)
    factor_number += 1
  return factors


print(list_of_multiples(5,10))