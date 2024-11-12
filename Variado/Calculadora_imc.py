import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 160
                   )

#Entrada de dados
engine.say("Digite seu peso em quilos")
engine.runAndWait()
peso = float(input("Digite seu peso em quilos:"))
engine.say("Digite sua altura em metros")
engine.runAndWait()
altura = float(input("Digite sua altura em metros:"))

#Desenvolvimento e calculos
imc = peso/altura**2

#Peso ideal
pesoMaximo = 24.99*altura*altura
pesoMinimo = 18.5*altura*altura

print(f"Peso minimo ideal: {pesoMinimo:.3f}")
print(f"peso máximo ideal: {pesoMaximo:.3f}")

if imc < 17:
    engine.say("Muito abaixo do peso!")
    engine.runAndWait()
    print("Muito abaixo do peso!")
elif imc <= 18.49:
    engine.say("Abaixo do peso!")
    engine.runAndWait()
    print("Abaixo do peso!")
elif imc <= 24.99:
    engine.say("Peso Normal")
    engine.runAndWait()
    print("Peso Normal")
elif imc <= 29.99:
    engine.say("Acima do peso")
    engine.runAndWait()
    print("Acima do peso")
elif imc <= 34.99:
    engine.say("Obesidade I")
    engine.runAndWait()
    print("Obesidade I")
elif imc <= 39.99:
    engine.say("obesidade II (servera)")
    engine.runAndWait()
    print("obesidade II (servera)")
else:
    engine.say("obesidade III(mórbida)")
    engine.runAndWait()
    print("obesidade III(mórbida)")
engine.stop()






