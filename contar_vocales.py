"""

ANGELICA ELIZABETH IBARRA DIAZ
 DIAZARTURO ARJONA HERMOSILLOA
 CHRISTIAN ALONSO FLORES BURGOS
 MARCO FABRIZIO AZPEITIA CASTELLANOS

 10 de octubre 2025

 Contar la cantidad de vocales en una frase
"""

# Declaraciones
vocal="aáeéiíoóuúü"

# Entradas
frase = input("Introduce una frase")
contador = 0
x = 0

# Proceso
frase = frase.lower()

while x < len(frase):
    if frase[x] in vocal:
        contador += 1
    x += 1

# Salidas
print(f"La frase tiene {contador} vocales")
