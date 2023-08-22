nivelAgua=int(input("Cúal es el nivel de agua: ?"))

#Evaluando multiples condicions
if nivelAgua > 0 and nivelAgua<=200:
    print(f"el nivel de agua es es: {nivelAgua}, esta muy bajo")
elif nivelAgua >200 and nivelAgua<= 400:
    print(f"el nivel de agua es es: {nivelAgua},estamos operando con normalidad")
elif nivelAgua > 400:
    print(f"el nivel de agua es es: {nivelAgua}, inice plan de evacuación...")
else:
    print("por favor revise el sensor de agua, nivel no valido")
