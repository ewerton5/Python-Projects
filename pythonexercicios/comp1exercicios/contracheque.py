# Ewerton Vieira
# aula 11 de abril
#
# programa monstra um contra-cheque

bruto = float(input('Entre com o valor do salário bruto: R$'))
am = float(input('Entre com o valor do Auxílio Moradia: R$'))
aa = float(input('Entre com o valor do Auxílio Alimentação: R$'))
if bruto < 2500:
	ir = 0
elif bruto <= 6000:
	ir = 18
else:
	ir = 27.5
inss = bruto*11/100
if inss > 600:
	inss = 600
liquido = bruto - bruto*ir/100 - inss + am + aa
print('*'*48)
print('{:<38}= R${:.2f}'.format('Saláro Bruto:', bruto))
print('*'*48)
print('Descontos:')
print('{:<38}= R${:.2f}'.format('Imposto de renda:', bruto*ir/100))
print('{:<38}= R${:.2f}\n'.format('Previdência social:', inss))
print('Auxílios:')
print('{:<38}= R${:.2f}'.format('Auxílio Moradia:', am))
print('{:<38}= R${:.2f}'.format('Auxílio Alimentação:', aa))
print('*'*48)
print('{:<38}= R${:.2f}'.format('Saláro Líquido:', liquido))
print('*'*48)
