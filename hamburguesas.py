# Precios de las hamburguesas
precio_s = 20.0
precio_d = 25.0
precio_t = 28.0

# Cargo por pago con tarjeta
cargo_tarjeta = 1.05

# Inicializar cantidades de hamburguesas
cantidad_s = 0
cantidad_d = 0
cantidad_t = 0

# Número total de hamburguesas a comprar
n = int(input("Ingrese el número total de hamburguesas a comprar: "))

# Solicitar tipo y cantidad de cada hamburguesa
for i in range(n):
    print("que tipo de hamburguesa desea?")
    print("Sencilla(S), Doble(D), Triple(T)")
    tipo = input(f"Ingrese el tipo de la hamburguesa {i + 1} (S, D, T): ").strip().upper()
    if tipo == 'S':
        cantidad_s += 1
    elif tipo == 'D':
        cantidad_d += 1
    elif tipo == 'T':
        cantidad_t += 1
    else:
        print("Tipo de hamburguesa no válido. Intente de nuevo.")
        print("que tipo de hamburguesa desea?")
        print("Sencilla(S), Doble(D), Triple(T)")
        tipo = input(f"Ingrese el tipo de la hamburguesa {i + 1} (S, D, T): ").strip().upper()
        if tipo == 'S':
            cantidad_s += 1
        elif tipo == 'D':
            cantidad_d += 1
        elif tipo == 'T':
            cantidad_t += 1

# Calcular el costo total
total = (cantidad_s * precio_s) + (cantidad_d * precio_d) + (cantidad_t * precio_t)

# Preguntar si el pago es con tarjeta de crédito
pago_con_tarjeta_input = input("¿El pago es con tarjeta de crédito? (si/no): ").strip().lower()
if pago_con_tarjeta_input == "si":
    total_final = total*cargo_tarjeta
else:
    total_final= total
    

# Mostrar el total a pagar
print(f"El total a pagar es: ${total_final:.2f}")
