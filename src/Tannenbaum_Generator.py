def tannenbaum():
    size = int(input("Wie Groß soll der Tannenbaum werden: "))

    for x in range(size):
        for j in range(size - x - 1):
            print(" ", end="")
        for i in range(2 * x + 1):
            print("X", end="")
        print()
def dreieck():
    size = int(input("Wie Groß soll das Dreieck werden: "))

    for i in range(1, size + 1):
        print("x" * i)

    for i in range(size, 0, -1):
        print("x" * i)

form = input("Dreieck oder Tannenbaum?")

if form in ["Tannenbaum", "T","t"]:
    tannenbaum()
else:
    dreieck()