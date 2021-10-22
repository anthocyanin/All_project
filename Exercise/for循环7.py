for i in range(6):
    for j in range(6-i):
        print(" ",end="")

    for x in range(i+1):
        if i==0 or i==5:
            print("* ",end="")
            continue
        if x==0 or x==i:
            print("钢之炼金术师 叹息之丘的圣星* ",end="")
        else:
            print("  ",end="")
    print()

