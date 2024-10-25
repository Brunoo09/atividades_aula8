# Desafio 1 Condicionais

# Crie um sistema de e-commerce, onde o usuário possa:

# cadastrar-se
# comprar um produto
# descobrir o valor total
# pagar


email = 'bruno@'
senha = 12345


meu_email = input('digite seu email:')
minha_senha = int(input('digite uma senha:'))
if meu_email == email and minha_senha == senha:
    print('lista')
else:
    print('algo deu errado')
lista =['arroz', 'feijão', 'ovo']
print(lista)
escolha = input('fazer pedido:')

carrinho = []
meu_valor = []
valores = [5.00, 4.50, 10.00 ]


if escolha == lista[0]:
    print('arroz')
    carrinho.append(lista[0])
elif escolha == lista[1]:
    print('feijão')
    carrinho.append(lista[1])
elif escolha == lista[2]:
    print('ovo')
    carrinho.append(lista[2])
else:
    print('não disponivel')


    
