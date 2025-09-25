'''
Slicing 

'''

import numpy as np
arr = np.linspace(1,5,10)
print(arr[3])
print(arr[-1])
print(arr[1:4])


print(arr[[0,2,4]])
print(arr[arr>3])



'''
Use: Selecting specific features/rows/columns from a dataset.
Example: Extract only certain features (e.g., age column) from a dataset.
Use: Filtering data based on conditions.
Example: Select rows where salary > 50K, or class == “1”.
'''