def x(nums):
    list = []
    for i in nums:
        list.append(i)
    return list

someNums = x([1, 2, 3, 4, 5])

def equivalencia(numero):
    for i in numero:
        yield i

someNums = equivalencia([1,2,3,4])

print(next(someNums))

print(next(someNums))

print(next(someNums))


print(next(someNums))
