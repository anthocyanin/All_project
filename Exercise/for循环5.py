for i in range(5):
    for j in range(5-i):
        if i == 0:
            print("* ",end="")
            continue
        if j==0 or j==(5-i-1):
            print("* ",end="")
        else:
            print("  ",end="")
    print()