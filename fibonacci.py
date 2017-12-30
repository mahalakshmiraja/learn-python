def fibonacci(number):
   first_num=0
   sec_num=1
   series=[0,1,]
   for i in range(2,number):
       result=first_num+sec_num
       series.append(result)
       first_num=sec_num
       sec_num=result
   print(series)

fibonacci(100)