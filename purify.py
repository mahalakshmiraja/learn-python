def purify(sequence):
    result_rem=[]
    result_new=[]
    
    for i in sequence:
        if i % 2 == 0 :
            result_new.append(i)
        else:
            result_rem.append(i)
    print(result_new)

purify([2,3,4,5,6,7])