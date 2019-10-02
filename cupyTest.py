import numpy as np
import cupy as cp
import time

s = time.time()
x_cpu = np.ones((1000,1000,1000))
x_cpu *= 5
x_cpu *= x_cpu
x_cpu *= x_cpu
x_cpu *= x_cpu
x_cpu *= x_cpu
x_cpu *= x_cpu
e = time.time()
print(e-s)

s = time.time()
x_gpu = cp.ones((1000,1000,1000))
x_gpu *= 5
x_gpu *= x_gpu
x_gpu *= x_gpu
x_gpu *= x_gpu
x_gpu *= x_gpu
x_gpu *= x_gpu
e = time.time()
print(e-s)


