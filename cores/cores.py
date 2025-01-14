# Version 1
# nome = "Victor Antônio Gomes"
# print(f"Olá ! Muito prazer em te conhecer, {'\033[4;34m'+ nome +'\033[m'} !!!")

# Version 2
nome = "Victor Antônio Gomes"
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30'}
print(f"Olá ! Muito prazer em te conhecer, {cores['amarelo'] + nome + cores['limpa']} !!!")

#Proposta dessa aula é colocar cores em todos os exercicios anteriores
