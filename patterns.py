
n = int(input("Enter the length of patterns : "))


print("1'st Question")

for i in range(n):
    for j in range(n):
        print("* ",end="")
    print()


print("2'th Question")

for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()

print("3'th Question")

for i in range(n):
    for j in range(i+1):
        print(j + 1 ,end="")
    print()

print("4'th Question")

for i in range(n):
    for j in range(i+1):
        print(i+1,end="")
    print()

print("5'th Question")

for i in range(n,0,-1):
    for j in range(i):
        print("* ",end="")
    print()

print("6'n Question")

for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end="")
    print()

print("7'th question ")

print("test")
