# Calculadora de multa de velocidade 

velocidade = float(input('Digite a velocidade do carro em km/h: '))

limite_de_velocidade = 80
valor_da_multa_km = 20 

if velocidade > limite_de_velocidade:
    km_excedido = velocidade - limite_de_velocidade
    valor_multa = km_excedido * valor_da_multa_km
    print(f'MULTADO! Você ultrapassou o limite de velocidade e levou uma multa de R${valor_multa:.2f}')
else:
    print('Tudo certo! Dirija com segurança!')