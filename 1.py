a=80000000
print("hi %d" %a,a,end="\t")
print(f"hi {a:,}")

astring = "Hello world!"
print('a','b','d',sep='dd')
print(astring[-5:9])
a={0:"sandeepa",'branch':"Is"}
print(a[0])
print("mce\n" * 3, end="")
name = input("What is your name ").strip().title()

print(f"how are you, {name}")
name, y = name.split(" ")
print(name)
print(y)
match name:
    case "Sandy":
        print("IS")
    case "Kris":
        print("CSE")
    case _:
        print("no")

for _ in range(3):
    print("mce")
while True:
    try:
        n = int(input("enter number "))
        if n > 0:
            break
    except:
        print("n is not a integer")



a=8
print({"hi"},a)