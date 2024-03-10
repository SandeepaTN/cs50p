

def main():
    x=int(input("enter the number "))
    print("x squared is", square(x))
    x=int(input("Enter the first operator "))
    y=int(input("Enter the second operator "))
    print(f"{x+y:,}")

def square(n):
    return n+n 


if __name__=="__main__":
    main()




