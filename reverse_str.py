def reverse_str(x):
    rnge = len(x)
    rev = []
    for i in range(rnge):
        rev.append(x[rnge-1])
        rnge-=1
    print(''.join(map(str, rev)))
     

reverse_str("WELCOME")