def prime_num(x):
    if x==2 or x==3:
        print ("Prime")
    elif x<2 or x%2==0 or x%3==0:
        print ("Not Prime")
    else:
        print ("Prime")

prime_num(75)