#Crie um programa que utilize uma estrutura de repetição para somar todos os números pares de 1 a 100 e exiba o resultado.
# Inicializa a soma
soma = 0

# Loop para percorrer os números de 1 a 100
for i in range(1, 101):
    # Verifica se o número é par
    if i % 2 == 0:
        soma += i  # Adiciona o número par à soma

# Exibe o resultado
print(f"A soma de todos os números pares de 1 a 100 é {soma}.")