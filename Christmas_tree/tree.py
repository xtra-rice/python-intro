print("Welcome! To create your triangle, enter the number of rows.")
rows = int(input("Rows: "))

for x in range(rows):
    for y in range(rows - x - 1):
        print(" ", end=" ")

    for z in range(2 * x + 1):
        print("*", end="")

    print()
