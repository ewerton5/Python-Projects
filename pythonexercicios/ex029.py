v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h'
          f'\nVocê deve pagar uma multa de \033[33mR${(v-80)*7:.2f}!')
print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')
