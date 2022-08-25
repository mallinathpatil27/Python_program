from itertools import accumulate
import operator

G=[1,2,3,4,5,6,7]

result=accumulate(G,operator.mul)

print(result)

for values  in result:
    print(values)
