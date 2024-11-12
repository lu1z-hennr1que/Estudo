altura = float(input("Digite sua altura em metros:"))
peso = float(input("Digite seu peso em kg:"))

imcc: peso/(altura**2)

if imcc >= 40:
    print("Obesidade III (mórbida)")
elif imcc >= 35.0 and 39.9:
    print("Obesidade II (severa)")
elif imcc >= 30.0 and 34.0:
    print("Obsidade grau I")
elif imcc >= 25.0 and 29.9:
    print("Levemente acima do peso")
elif imcc >= 18.6 and 24.9:
    print("Peso ideal (parabéns)")
else:
    print("abaico do peso")