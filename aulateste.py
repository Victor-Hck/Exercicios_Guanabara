# for c in range(1, 11):
#     print(c)

c = 1
par = impar = 0

while c != 0:
    c = int(input(("Digite um valor: ")))
    if c % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Foram digitados {par} numeros Pares\nE foram digitados {impar} numeros impares.")
# for e utilizado quando você sabe o inicio e o fim
# ex: Tem 50 pessoas na fila. for i in range(1, 51):

# while e utilizado quando você não sabe o inicio e o fim
# ex: Vão chegar varias pessoas na fila. while nao parar de chegar pessoa na fila:
                                            # Va contando quantas pessoas chegaram.