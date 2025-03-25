
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
patterns(n)