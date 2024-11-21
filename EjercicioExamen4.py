numero = int(input("Introduce un numero entero:"))
multiplos_de_3 = [n for n in range(3, numero + 1, 3)]
divisibles_por_5 = [n for n in multiplos_de_3 if n % 5 == 0]
print("lista de multiplos de 3:", multiplos_de_3)
print("lista de numeros divisibles por 5:", divisibles_por_5)
    