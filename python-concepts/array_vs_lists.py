#Arrays and lists, in Python, have the same way of storing data. But, arrays can hold only a single data type elements whereas lists can hold any data type elements.

import array

arr = array.array('b', [1,2,3,4])
#arr = array.array('b', [1,'a',3,4]) fail
list = [1, 'a', '1']
print(arr)
print(list)