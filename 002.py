sum = 0
calculatedResult = []

def fibonacci(n):
  if n == 1 :
    return 1
  if n == 2 :
    return 2
  return fibonacci(n-1) + fibonacci(n-2)

isContinue = True
n=0
while (isContinue):
  n+=1
  fibNumber = fibonacci(n)
  if fibNumber % 2 ==0 :
    sum += fibNumber
  if n > 32 :
    isContinue = False
    print(sum) 



def getProperN():
  n=0
  isContinue = True
  while (isContinue):
    n+=1
    if fibonacci(n) >= 4000000 :
      isContinue = False
      break
  calculatedResult.extend([n,fibonacci(n)])

getProperN()
if calculatedResult[1] > 4000000:
  for i in range(calculatedResult[0]):
    if fibonacci(i) % 2 ==0:
      sum+=fibonacci(i)
else:
  for i in range (calculatedResult[0]+1):
        if fibonacci(i) % 2 ==0:
          sum+=fibonacci(i)

print(calculatedResult)