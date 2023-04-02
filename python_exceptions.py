def divide_by(a, b):
    return a/b

try:
    ans = divide_by(40/0)
# except Exception as E:
#     print('Something went wrong!', E)
#     print(E.__class__)

except ZeroDivisionError as E:
    print(E, 'we cannot divide by zero')
except Exception as E:
    print(E, 'something went wrong')

# print(divide_by(40, 0))