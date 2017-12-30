def remove_duplicates(seq):
    first_num=seq[0]
    res=[]
    for i in seq:
        if i not in res:
            res.append(i)
    print (res)


remove_duplicates([1,2,1,2,3,3])
