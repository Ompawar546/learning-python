'''
Use: Creating datasets, feature vectors, weight matrices quickly.
Example: Initialize weights in Neural Networks with zeros/ones/random arrays.

'''

import numpy as np

arr = np.ones((3,4),float)
print(arr)

arrZero = np.zeros((3,5),int)
print(arrZero)

arrArange = np.arange(1,10)
print(arrArange)

arrLinspace = np.linspace(0,1,6)
print(arrLinspace)


'''
weights are like importance given to each datapoints 

In machine learning, everything is ultimately represented by numbers. Vectors are the fundamental way to convert real-world data, like text, images, or sounds, into a format that algorithms can understand and process. For example:

Images: A color image can be represented as a vector where each number corresponds to the pixel's color and intensity values.

Text: Words can be turned into vectors using techniques like Word2Vec or GloVe. In this case, words with similar meanings are represented by vectors that are close to each other in the vector space.

'''