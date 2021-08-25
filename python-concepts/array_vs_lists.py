#Arrays and lists, in Python, have the same way of storing data. But, arrays can hold only a single data type elements whereas lists can hold any data type elements.




# [0, 4, 3, 1]
def solution (a, s):
    result = 0
    size = len(a)

    for x in range(len(a) + 1):
        for y in range((len(a) - x) + 1):
            arr = a[x:y]
            result += calc(arr, s)

    return result

def calc(arr, s):
    sum = 0
    for x in arr:
        sum = sum + x

    return 1 if sum // s == s else 0

def powerset(s):
    x = len(s)
    arr = []
    for i in range(1 << x):
            for j in range(x):
                if (i & (1 << j)):
                    a = s[j]


    return arr

result = powerset([1,2,3])
print(result)


