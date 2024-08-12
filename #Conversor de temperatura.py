#Peça ao usuário que insira uma temperatura em graus Celsius
#E converta-a para Fahrenheit. A fórmula de conversão é: Fahrenheit = (Celsius * 9/5) + 32.

temp =  int(input("Insira temperatura em graus Celsius: "))
conversao = (temp * 9/5) + 32
print(conversao , "Em Fahrenheit")
 

#Corrigido pelo chatg
try:
    temp = int(input("Insira temperatura em graus Celsius: "))
    conversao = (temp * 9/5) + 32
    print(conversao, "Em Fahrenheit")
except ValueError:
    print("Por favor, insira um número válido.")
