def isPrime(factor):
  if factor <= 1:
    return False
  if factor == 2:
    return True
  
  n = 3

  while n * n <= factor:
    if factor % n == 0:
      return False
    else: n += 2
  return True

# test isPrime() 
# print(isPrime(29))

def isPrimeForOdd(evenNumber):
  if evenNumber % 2 == 0:
    return False
  n = 3
  while n * n <= evenNumber:
    if evenNumber % n == 0:
      return False
    else: n += 2
  return True

#test isPrimeForOdd
# print(isPrimeForOdd(29))

factors = []

def findFactorsForOddNumber(oddNumber):
  for n in range(3, oddNumber):
    if oddNumber % n == 0:
      factors.append(n)
    n += 2
    continue
  return factors

# test findFactorsForOddNumber
# print(findFactorsForOddNumber(600851475143))

def findLargestFactorForOddNumber(oddNumber):
  for n in range(3, oddNumber):
    if oddNumber % n == 0:
      langesetFactor = n
      n += 2
  return langesetFactor

# test findLargestFactorForOddNumber()
# print(findLargestFactorForOddNumber(15))

def findLargestPrimeFactorForOddNumber(oddNumber):
    for n in range(3, oddNumber):
      if oddNumber % n == 0:
        if isPrimeForOdd(n) :
          langesetFactor = n
      else: n += 2
    return langesetFactor

# test findLargestPrimeFactorForOddNumber
print(findLargestPrimeFactorForOddNumber(13579))