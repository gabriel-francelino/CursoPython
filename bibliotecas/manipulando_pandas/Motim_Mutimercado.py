import pandas as pd 

def procura_prod():
  # lê o arquivo 'dados.xlsx' que está na mesma pasta do código
  df = pd.read_excel('Motim_Mutimercado.xlsx')
  nome = input('Digite o nome da busca:')
  produto = df.loc[df['Nome']==nome]
  return produto

def vender(produto):
  print(produto)
  quantidade = int(input('Insira a quantidade que deseja vender: '))
  valor_u = float(input('Insira o valor por unidade para a venda: '))
  valor_total = valor_u*quantidade

  p = produto.values.tolist()
  print(p)
  p = p[0]
  if quantidade <= p[1]:
    valor_min = p[3]*(1-p[4])
    if valor_u >= valor_min:
      print(f'Venda aurotizada pelo valor : {valor_total}')
      df = pd.read_excel('Motim_Mutimercado.xlsx')
      df.loc[df['Nome']==p[0], 'Quantidade'] = p[1]-quantidade
      df.loc[df['Nome']==p[0], 'Valor vendido'] = p[5]-valor_total
      df.to_excel('Motim_Mutimercado.xlsx', index=False)
    else:
      print(f'Venda negada! Valor mínimo por unidade é de {valor_min} reais;')
  else:
    print(f'Venda negada! Falta de estoque, você possui {p[1]} unidades.')

while True:
  ver = input('Digite p para parar o caixa: ')
  if ver == 'p':
    print('Caixa fechado!')
    break
  else:
    produto = procura_prod()
    vender(produto)