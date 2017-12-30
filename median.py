def med(sequence):
    rng = len(sequence)
    sequence.sort()
    a=round(rng/2)
    if rng%2==0:
        b=a-1
        medin=(sequence[a] + sequence[b] )/2
        print (medin)
    else:
        print (sequence[a])

med([1, 3, 8, 7, 12])