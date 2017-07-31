a = 1
list1 = []


def f():
    # a = "w"
    # a = a+1
    # global list1
    # list1.append()
    print a
    t = (1, 2)
    l = list(t)
    print l


f()
print a

print "ase".split("?")[0]

import numpy as np
import pandas as pd

var = np.arange(3 * 2).reshape((3, 2))
fr = pd.DataFrame(var, columns=['a', 'b'], index=range(np.shape(var)[0]))
fr
# Out[6]:
#        a  b
#     0  0  1
#     1  2  3
#     2  4  5


        