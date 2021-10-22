for i in range(5):
    for x in range(i+1):
        if i == 4:
            print("* ",end="")
            continue
        if x == 0 or x ==i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
