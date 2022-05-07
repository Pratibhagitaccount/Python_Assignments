# def foo():
#     try:
#         return 1
#     finally: 
#         return 2
# k = foo() 
# print(k)

# The output of above block is 2, as finally block always get executed,
# whether try block condition is satisfied or not.

# def a(): 
#     try:
#         f(x, 4) 
#     finally:
#         print('after f')
#         print('after f?') 
# a()

# it will give us an error, as f is not defined, and is used in try block.