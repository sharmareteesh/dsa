
n = int(input("Enter the length of patterns : "))

def patterns(value):
    print("Question : 1")
    for i in range(value):
        for j in range(value):
            print("* ", end="")
        print()
    
    print("Question : 2")
    for i in range(1,value+1):
        print("*" * i) 

    print("Question : 3")
    for i in range(1,value+1):
        for j in range(1,i+1):
            print(j,end="")
        print()

    print("Question : 4")
    for i in range(1,value+1):
        for j in range(1,i+1):
            print(i,end="")
        print()

    print("Question : 5")
    for i in range(value,0,-1):
        print("*" * i)
    
    print("Question :6")
    for i in range(value,0,-1):
        for j in range(1,i+1):
            print(j,end="")
        print()

    print("Question :7")
    for i in range(1,value+1):
        print(" "*(value-i),end="")
        print("* "*i)

    print("Question :8")
    for i in range(value,0,-1):
        print(" "*(value-i),end="")
        print("* "*i)

    print("Question :9")
    for i in range(1,value+1):
        print(" "*(value-i),end="")
        print("* "*i)
    for j in range(value,0,-1):
        print(" "*(value-j),end="")
        print("* "*j)

    print("Question :10")
    for i in range(1,value+1):
        print("* "*i)
    for j in range(value-1,0,-1):
        print("* "*j)
patterns(n)