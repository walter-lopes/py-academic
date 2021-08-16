# lists are mutable, they can be edited
# tuples are immutable (tuples are lists which cant be edited)

list = [10, 'liverpool', 99]
tup = (10, 'liverpool', 20)

list[1] = 11
#tup[1] = 11 # fail
#tup(1) = 11 #fail

print(list)

from dis import dis

#Tuples can be constant folded
#Tuples of constants can be precomputed by Python's peephole optimizer or AST-optimizer. Lists, on the other hand, get built-up from scratch:
dis(compile("(10, 'abc')", '', 'eval'))

dis(compile("[10, 'abc']", '', 'eval'))

#Tuples do not need to be copied
#Running tuple(some_tuple) returns immediately itself. Since tuples are immutable, they do not have to be copied:


#Tuples do not over-allocate

#Since a tuple's size is fixed, it can be stored more compactly than lists which need to over-allocate to make append() operations efficient.
#This gives tuples a nice space advantage:

# This over-allocates proportional to the list size, making room
# for additional growth.  The over-allocation is mild, but is
# enough to give linear-time amortized behavior over a long
# sequence of appends() in the presence of a poorly-performing
# system realloc().
# The growth pattern is:  0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...
# Note: new_allocated won't overflow because the largest possible value
#       is PY_SSIZE_T_MAX * (9 / 8) + 6 which always fits in a size_t.
 #/