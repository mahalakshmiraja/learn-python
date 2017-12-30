from operator import itemgetter
x = {'d': 2, 'a': 4, 'b': 3, 'f': 1, 'c': 0}
sorted_x = sorted(x.items(), key=itemgetter(0))
print (sorted_x)
d = dict(sorted_x)
print (d['a'])