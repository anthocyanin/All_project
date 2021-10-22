for i in range(4):
    if i == 0 or i == 3:
        for x in range(5):
            print("* ",end="")
        print()
    else:
        for j in range(5):
            if j == 0 or j==4:
                print("* ",end="")
            else:
                print("  ",end="")
        print()