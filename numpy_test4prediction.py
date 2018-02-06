import numpy as np
aa = np.array([[1,2,3],[2,4,6]])
bb = aa>2

idx = np.array([1,3,5])
x = np.zeros((6,))
x[idx] = np.array([1.1,1.4,1.5])



a = np.arange(10).reshape(2, 5)
indexer = np.array([[1,3,2],[2,4,3]])
sup = np.repeat(np.arange(2).reshape(2,1),3,axis=1)
a[sup,indexer] # this is what I need

np.ix_([0, 1], [2, 4])
print('eof')