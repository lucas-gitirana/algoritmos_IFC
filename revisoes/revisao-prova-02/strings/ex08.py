s = input("String: ").upper()
acumulador = ""

for i in s:
    if i not in acumulador:
        print(i, ": ", s.count(i), "X")
        acumulador += i

