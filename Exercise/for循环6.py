for i in range(6):
    for j in range(6-i):
        print(" ",end="")
    for x in range(i+1):
        print("* ",end="")
    print()