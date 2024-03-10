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
