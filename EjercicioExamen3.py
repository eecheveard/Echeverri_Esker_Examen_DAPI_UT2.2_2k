palabra = input("introduce una palabra:")
consonante = input("introduce una constante:")
vocal = input("introduce una vocal")
if len(consonante) != 1 or consonante.lower() not in "bcdfghjklmnñpqrstvwxyz":
    print("la consonante introducida no es valida.")
elif len(vocal) != 1 or vocal.lower() not in "aeiou":
    print("la vocal introducida no es valida.")
else:
    palabra_modificada = palabra.replace(consonante, consonante.upper())
    palabra_modificada = palabra_modificada.replace(vocal, "")
    print("resultado:", palabra_modificada)