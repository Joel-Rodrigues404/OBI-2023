N = int(input())

nomes =  []
valores = []

for numero_de_lances in range(N):
    C = str(input()).strip()
    V = int(input())
    if len(C) >= 1 and len(C) <= 10:
        nomes.append(C)
    if V >= 1 and V <= 100000:
        valores.append(V)

maior = max(valores)

indice_maior = valores.index(maior)

print(nomes[indice_maior])
print(maior)