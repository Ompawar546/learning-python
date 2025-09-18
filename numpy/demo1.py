import numpy as np
arr = np.array([1, 2, 3])
np.save('my_array.npy', arr)  # save
loaded = np.load('my_array.npy')  # load
print(loaded)
