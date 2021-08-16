#The fundamental difference between a list and an iterator is that a list contains a number of objects in
# a specific order - so you can, for instance, pull one of them out from somewhere in the middle:

list = [1,2,3,4,5,5,6,7,8,96,5,3]

print(list[3])

#... whereas an iterator yields a number of objects in a specific order, often creating them on the fly as requested:

my_iter = iter(range(1000000000000))
next(my_iter)


#Notice the trade-off: a list of a trillion integers would use more memory than most machines have available,
# which makes the iterator much more efficient ... at the cost of not being able to ask for an object somewhere in the middle:
