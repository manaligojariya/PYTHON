# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300})

from collections import Counter

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}

counter1 = Counter(d1)
counter2 = Counter(d2)

combine_counter= counter1 + counter2
print(combine_counter)




