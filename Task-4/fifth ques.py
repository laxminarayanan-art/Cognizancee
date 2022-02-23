i = int(input("Enter the number of rows:"))
j = (2 * i) - 2
for m in range(0, i):
    for n in range(0, j):
        print(end=" ")
    j = j - 1
    for n in range(0, m + 1):
        print("*", end=" ")
    print(" ")