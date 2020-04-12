
##write a python program to implement your own myreduce() function which works exactly like python's built in function reduce()
def my_reduce(func,sequence) :
    total=list[0]
    for i in list[1:]:
        total =func(i,total)

    return total


def my_sum(a,b):
    return a+b


list=[1,2,3,4,59,97,65]
print(str(my_reduce(my_sum,list)))

##wrirte a python program to implement your own myfilter() function which works exactly like python's inbuilt function filter().
def my_filter(fun,sequence):
    result=[]
    for i in sequence:
        if i%2==0:
           result.append(i)
    return result
def even_check(n):
    if n%2==0:
        return true

list=[1,2,3,4,5,6,7,8,9,10,24,28]
print(str(my_filter(even_check,list ) ))


##. Implement List comprehensions to produce the following lists.

list="""['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
[4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]"""
print(list)
