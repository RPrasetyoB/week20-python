def FactorialRecursion(num):

  if num == 0:
      return 1

  return num * FactorialRecursion(num - 1)

# keep this function call here 
print(FactorialRecursion(input()))