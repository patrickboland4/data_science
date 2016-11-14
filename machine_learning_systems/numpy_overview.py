'''
- matrix manipulation, linear algebra, optimization, clustering, spatial operations, or even Fast Fourier transformation
- scipy.stats, scipy. interpolate, scipy.cluster, and scipy.signal.
'''

import numpy as np
import timeit

#create a one-dimensional array
#recall two useful methods for seeing dimension and shape of array
print('Array creation and information example')
a = np.array(range(6))
print(a)
print(type(a))
print(a.ndim)
print(a.shape)
print('\n')

#reshape the one dimensional array above
#note the importanc of using .copy() method
print('Reshape and .copy()')
b = a.reshape(3, 2)
print(b)
b[1][0] = 77
print(b)
print(a)
c = b.copy()
c[1][0] = 2
print(c)
print(b)
print('\n')

#broadcasting to elements within an array
print('Broadcasting example')
a1 = np.array(range(6))
print(a1)
a2 = a1.copy()
a2 **= 2
print(a2)
print('\n')

print('Indexing example')
print(a)
#index with a new numpy array - 3 identical solutions below
print(a[np.array(range(2,5))])
print(a[np.array([2, 3, 4])])
print(a[[2, 3, 4]])
#index with a boolean statement - notice that the statement is propogated throughout the array
print('~~Boolean indexing~~')
print(a>4)
print(a[a>4])
print('~~Trimming outliers manually and with .clip()~~')
a1 = a.copy()
a[a>4] = 4
print(a)
a1 = a1.clip(0, 4)
print(a1)
#how to negate a logical statement
print(a1[a1>1],'Negate the statement with "~"', a1[~(a1>1)])
#how to return all nan values within an array
#np.isnan(array)
print('\n')

# print('~~using timeit package to compare performance')
# normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))', number=10000)
# naive_np_sec = timeit.timeit('sum(na*na)', setup="import numpy as np; na=np.arange(1000)", number=10000)
# good_np_sec = timeit.timeit('na.dot(na)', setup="import numpy as np; na=np.arange(1000)", number=10000)
# print("Normal Python: %f sec"%normal_py_sec)
# print("Naive NumPy: %f sec"%naive_np_sec)
# print("Good NumPy: %f sec"%good_np_sec)
# #important to consider how loops/iteration can be utilized within a highly optimized library



'''
General np knowledge
Q) how many data types can an array hold?
    1
Q) what happens when multiple data types are passed to a single array?
    coercion to a common dtype
'''













