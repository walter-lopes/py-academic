import numpy as np

# importing system module
import sys

arr = np.array([1, 2, 4])

print(arr)

multi_arr = np.array([(1, 2, 3), (4, 5, 6)])

print(multi_arr)


# declaring a list of 1000 elements
S = range(1000)

# printing size of each element of the list
print("Size of each element of list in bytes: ", sys.getsizeof(S))

# printing size of the whole list
print("Size of the whole list in bytes: ", sys.getsizeof(S) * len(S))

# declaring a Numpy array of 1000 elements
D = np.arange(1000)

# printing size of each element of the Numpy array
print("Size of each element of the Numpy array in bytes: ", D.itemsize)

# printing size of the whole Numpy array
print("Size of the whole Numpy array in bytes: ", D.size * D.itemsize)

# importing required packages
import numpy
import time

# size of arrays and lists
size = 5

# declaring lists
list1 = range(size)
list2 = range(size)

# declaring arrays
array1 = numpy.arange(size)
array2 = numpy.arange(size)

# capturing time before the multiplication of Python lists
initialTime = time.time()

# multiplying  elements of both the lists and stored in another list
resultantList = [(a * b) for a, b in zip(list1, list2)]

print(resultantList)

# calculating execution time
print("Time taken by Lists to perform multiplication:",
      (time.time() - initialTime),
      "seconds")

# capturing time before the multiplication of Numpy arrays
initialTime = time.time()

# multiplying  elements of both the Numpy arrays and stored in another Numpy array
resultantArray = array1 * array2

print(resultantArray)

# calculating execution time
print("Time taken by NumPy Arrays to perform multiplication:",
      (time.time() - initialTime),
      "seconds")