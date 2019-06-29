c = float(input('Preço das compras: R$'))
f = int(input("Formas de pagamento:"
              "\n[1] à vista dinheiro/cheque"
              "\n[2] à vista cartão"
              "\n[3] 2x no carão"
              "\n[4] 3x ou mais no cartão\nQual a opção? "))
if f == 1:
    print(f'Sua compra de R${c:.2f} vai custar R${c*0.9:.2f}')
elif f == 2:
    print(f'Sua compra de R${c:.2f} vai custar R${c*0.95:.2f}')
elif f == 3:
    print(f'Sua compra será parcelada em 2x de R${c/2} sem juros.'
          f'\nSua compra de R${c:.2f} vai custar R${c:.2f} no final.')
elif f == 4:
    p = int(input('Quantas parcelas?'))
    print(f'Sua compra será parcelada em 2x de R${c*1.2/p} com juros.'
          f'\nSua compra de R${c:.2f} vai custar R${c*1.2:.2f} no final.')
else:
    print('Opção inválida. Tente novamente.')
