a = int(input("Введите число "))
b = int(input("Введите число "))

s = ''

while a <= b:
        if a % 2 == 0: s = s + str(a) + " "
        a += 1

print(s)


