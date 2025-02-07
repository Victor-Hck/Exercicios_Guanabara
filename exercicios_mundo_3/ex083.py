"""
Desafio 083

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
E fechados na ordem correta.
"""
exp = input("Digite a expressão: ")
pilha = list()

for simb in exp:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print(f"Sua expressão está válida!")
else:
    print(f"Sua expressão está errada!")