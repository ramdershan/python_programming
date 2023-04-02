# def sum_of(a, b):
#     return a + b

###args
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4,5,6,4))

##kwargs
def sum_of(**kwargs):
    sum = 0
    for k, x in kwargs.items():
        sum += x
    return sum

print(sum_of(coffee=2, cake=4.55, juice=3))