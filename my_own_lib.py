def main():
    print(fact(4))
    print(sum(10,40))

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)


def sum(x,y):
    return x+y


main()
    