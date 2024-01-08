num = int(input("Wie lautet deine Dezimal Zahl?"))
bin_list = []

def calculator(num):
    while num >= 1:
        erg = num % 2
        bin_list.append(erg)
        num = num // 2
        print(num)

calculator(num)
reversed_list = list(bin_list)
reversed_list.reverse()

print(reversed_list)
