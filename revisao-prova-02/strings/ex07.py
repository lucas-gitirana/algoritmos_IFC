s1 = input("String 01: ")
s2 = input("String 02: ")

if s1 in s2:
    print("Posição de início: ", s2.find(s1))
else:
    print("A string não contém a anterior")
