
def calcular_declividade(cota_inicial, cota_final, distancia):
    if distancia <= 0:
        raise ValueError("A distância deve ser maior que zero.")

    desnivel = cota_final - cota_inicial
    declividade = (desnivel / distancia) * 100

    return declividade


# Dados de exemplo
cota_inicial = 850.0
cota_final = 845.0
distancia = 100.0

resultado = calcular_declividade(
    cota_inicial,
    cota_final,
    distancia
)

print(f"Declividade: {resultado:.2f}%")
