#global
myGlobal = 10

def fn1():
    enclosedV = 8
    def fn2():
        localV = 5
        print('access to global', myGlobal)
        print('access to enclosed', enclosedV)
    fn2()

fn1()