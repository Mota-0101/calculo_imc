# Programa para calcular a massa corpórea.

massa = 78 # Parâmetro.
altura = 1.75# Parâmetro.
imc = massa / (altura ** 2) # Cálculo.
imc_arredondado = round(imc, 2) # Arredondamento do Cálculo.

if imc < 19: # 1ª Condição
    print("Abaixo do peso.")
elif imc >= 19 and imc < 25: #(senão se) Se o 'if' não for atendindo, cairá em um dos 'elif' ou so 'else'.
    print("peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 35: # Ou '30 <= imc < 35:'.
    print("Obesidade grau I")
elif imc >= 35 and imc < 40:
    print("Obesidade grau II")
else: #else
    print("Obesidade grau III") 
print(f"Seu imc está em {imc_arredondado}. Todos devemos cuidar da saúde!") #Mensagem com o fstring, para retornar 
                                                                            #o imc formatado pelo 'round'.