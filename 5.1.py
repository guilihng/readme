import numpy.matlib
import numpy as np

A = np.random.seed(612)
A = np.random.uniform(0, 1, 1000)
i = 1
n = int(input('请输入一个1-100之间的整数：'))
print('序号\t索引值\t随机数')
for x in range(0, 1000, n):
    print(i, x, A[x], sep='\t')
    i = i + 1
