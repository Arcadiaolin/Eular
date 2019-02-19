import numpy as ny
answer = 0

for i in ny.arange(1, 200):
  answer += 5 * i

for i in ny.arange(1, 334):
  if 3 * i % 5 == 0:
    continue

  answer += 3 * i 

print(answer)