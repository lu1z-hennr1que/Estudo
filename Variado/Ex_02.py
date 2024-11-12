masa = int(input("Quantas maças você vai levar:"))
if masa <= 11:
    total = masa*1.40
    print("Levando", masa, "maçãs custara: R$", total)
else:
    total2 = masa*1.25
    print("Levando", masa, "maçãs custara: R$", total2)