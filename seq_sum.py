a=[1,2,3]
def digit_sum(n):
  sum = 0
  for i in range(len(n)):
    sum = n[i] + n[i+1]
  print sum
  return sum
  
digit_sum(a)