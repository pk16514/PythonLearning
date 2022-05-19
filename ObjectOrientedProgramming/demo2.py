from calc2 import add


def fun1():
    add()
    print('from fun1', __name__)


def fun2():
    print('from fun2')


def main():
    fun1()
    fun2()


main()
