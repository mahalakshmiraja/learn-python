def factorial(x):
    fact=x
    for i in range(1,x):
        fact *= i
    print (fact)
    return fact
  	
  
factorial(6)