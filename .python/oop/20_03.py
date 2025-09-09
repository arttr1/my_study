# def f():
#     global n
#     n = 10
#     print(n)
#     def d2():
#         nonlocal n
#         n = 20 
#         print(n)
#     d2()
#     print(n)

# n = 5
# print(n)
# f()
# print(n)



# def mapping(f, lst):
#     '''
#     map function for iteration object
#     :param f: Function of one argument
#     :param lst: Iteration object
#     :return: Mapping object 
#     '''
#     res = []
#     for i in lst:
#         res.append(f(i))

#     return res 

# def multiply(n):
#     return n*2

# lst = [1, 2, 3, 4, 4]

# print(mapping(multiply, lst))


# print(list(range(10)))
# print(list(range(1, 10)))
# print(list(range(1, 10, 2)))


# def gen(N):
#     for i in range(1, N+1):
#         yield i*i # return without stop function

# g = gen(100)

# print(next(g))
# print(next(g))

# print(next(g))
# print(list(g))


# def my_range (start, stop = None, step = 1):
#     if stop == None:
#         stop = start
#         start = 0

#     index = 0
#     while (step > 0 and start + index * step < stop) or (step < 0 and start + index * step > stop):
#         yield  start + index * step
#         index +=1

# print(list(my_range(10)))
# print(list(my_range(2, 10)))
# print(list(my_range(3, 10, 2)))
# print(list(my_range(10, 3, -1)))




# class MyClass:
#     a = 5
#     b = 20

# mc1 = MyClass()
# mc2 = MyClass()


# mc1.a = 100
# mc2.b = 50

# print


class MyClass:
    def __init__(self):
        self.a = 5
        self.b = 10
        self.lst = [1,2,3,4]

mc1 = MyClass()
mc2 = MyClass()


mc1.a = 100
mc2.b = 50
mc1.lst.append(5)

# инкопсуляция
# 
# 
