
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

    print("Question :11 ")
    for i in range(1,value+1):
        for j in range(i):
            print((j%2)," ",end="")
        print()

    print("Question :12")
    for i in range(1,value+1):
        for j in range(1,i+1):
            print(j,end="")
        print(" "*(2*(value-i)),end="")
        for j in range(i,0,-1):
            print(j,end="")
        print()

    print("Question : 13")
    holder=1
    for i in range(1,value+1):
        for j in range(i):
            print(holder,end="")
            holder+=1
        print()

    print("Question :14")
    for i in range(1,value+1):
        for j in range(i):
            print(chr(65+j),end="")
        print()

    print("Question :15")
    for i in range(value+1,0,-1):
        for j in range(i):
            print(chr(65+j),end="")
        print()

    print("Question :16")
    for i in range(value+1):
        for j in range(i+1):
            print(chr(65+i),end="")
        print()

    print("Question: 17")
    for i in range(1,value+1):
        print(" " * (value - i), end="")
        for j in range(1,i+1):
            print(chr(64+j),end="")
        for j in range(i-1,0,-1):
            print(chr(64+j),end="")
        print()

    print("Questions :18")
    for i in range(value,0,-1):
        for j in range(i,value+1):
            print(chr(64+j),end="")
        print()
    
    print("Question :19")
    for i in range(value,0,-1):
        print("*" * i + " " * (2 * (value - i)) + "*" * i)
    for i in range(1,value+1):
        print("*" * i + " " * (2 * (value - i)) + "*" * i)

    print("Question :20")
    for i in range(1, value + 1):
        print("*" * i + " " * (2 * (value - i)) + "*" * i)
    for i in range(value - 1, 0, -1):
        print("*" * i + " " * (2 * (value - i)) + "*" * i)

    print("Question :21")
    for i in range(value):
        if i == 0 or i == value - 1:
            print("* " * value)
        else: 
            print("* " + "  " * (value - 2) + "* ")
    

    print("Question :22")
    size = 2 * value - 1  
    for i in range(size):
        for j in range(size):
            num = value - min(i, j, size - i - 1, size - j - 1)
            print(num, end=" ")
        print()


patterns(n)