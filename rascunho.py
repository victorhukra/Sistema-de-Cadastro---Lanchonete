# Desenvolva um sistema de informação que auxilie no controle de vendas em uma lanchonete.

# O sistema deverá permitir o cadastro, modificação, exclusão e consulta de "produtos" e "vendas".

# Cada produto deve conter as seguintes informações:
# - Nome
# - Preço

# Cada venda deve conter:
# - Cliente
# - Data
# - produtos
# - Total

# O programa deve produzir os seguintes relatórios:

# Lista de vendas geral (todas) contemplando nome do cliente, data e os produtos que comprou;
# Lista de vendas em uma determinada data contemplando nome do cliente, data e os produtos que comprou;
# Quem é o cliente que mais gastou.

lista_produtos = [{'Produto': 'X-Burguer', 'Preço': 17.00}, {'Produto': 'Dog Duplo', 'Preço': 13.50}, {'Produto': 'Dog Bacon', 'Preço': 17.50}]
lista_vendas = []

def cadastrar_produto():    #função para cadastrar os produtos        
    quantidade_cadastrar = int(input('Quantidade de produtos que deseja cadastrar: '))  #quantidade de produtos que deseja cadastrar
    for i in range(quantidade_cadastrar):   #for com a quantidade de produtos
        nome_produto = str(input(f'Digite o nome do {i + 1}° produto: '))   #variavel para nome do produto
        preco_produto = float(input(f'Digite o preço do {i + 1}° produto: '))   #variavel para o preço do produto

        p = {'Produto': nome_produto, 'Preço': preco_produto}       #dicionario para armazenar, flexível

        lista_produtos.append(p)        #armazena o dicionario na lista de produtos


def listar_produtos():      #função para listar os produtos 
    print('\nLista de produtos: ')
    for i, prod in enumerate(lista_produtos):       #for enumerate para pegar indice e valor 
        print(f'{i} - {prod}')      #printa


def modificar_produto():        #função para modificar um produto
    
    indice_modificar = int(input('\nDigite o índice do produto que deseja modificar: '))    #pega o produto por índice

    if  0 <= indice_modificar < len(lista_produtos):        #condição para caso o índice seja inválido


        modificar_nome = str(input('Digite o nome do novo produto: '))      #variavel para guardar o novo nome 
        modificar_preco = float(input('Digite o preço: R$'))        #variavel para guardar o novo preço

        lista_produtos[indice_modificar]['Produto'] = modificar_nome       #atualiza por índice/chave = variavel
        lista_produtos[indice_modificar]['Preço'] = modificar_preco
        print('\n----------------ATUALIZADO----------------')
        listar_produtos()                 #printa a lista de produtos atualizada

    else:
        print('\nÍndice inválido!')     #se o índice não for válido printa erro


def excluir_produto():      #função para excluir o produto
    varexcluir = int(input('\nDigite o índice do produto que deseja excluir: '))        #pega por índice

    if 0 <= varexcluir < len(lista_produtos):       #condição para caso o índice seja inválido

        lista_produtos.pop(varexcluir)        #pop para excluir 
        print('\n----------------ATUALIZADO----------------')
        listar_produtos()       #printa a lista atualizada
    
    else:
        print('\nÍndice inválido!')     #erro caso seja inválido

def consultar_produto():
    if len(lista_vendas) == 0:      #se não tiver vendas registradas (len == 0) printa erro
        print('\nNão há vendas registradas!')
    
    else:       #se ja tiver vendas chama função menu consultar produto 
        menu_consultar_produto()
        escolha_consultar = int(input('\nEscolha uma das opções acima: '))      #escolhe a opção

        if escolha_consultar == 1:     
            for i, prod in enumerate(lista_vendas):
                print(f'{i} - {prod}')
        
        if escolha_consultar == 2:      #se a escolha for 2 vai printar o cliente que mais gastou
            cliente_que_mais_comprou()


def menu_consultar_produto():       #menu consultar produto
    print('\n--------------MENU CONSULTAR--------------')
    print('\n(1) - Data específica')
    print('(2) - Cliente que mais gastou')
    print('(0) - Sair')  


def mostrar_menu_principal():       #menu principal
    print('\n--------------MENU PRINCIPAL--------------')
    print('\n(1) - Vendedor')
    print('(2) - Cliente')
    print('(0) - Sair')


def mostrar_menu_vendedor():        #menu vendedor
    print('\n--------------MENU VENDEDOR--------------')
    print('\n(1) - Cadastrar produtos')
    print('(2) - Modificar produtos')
    print('(3) - Excluir produtos')
    print('(4) - Consultar produtos')
    print('(0) - Voltar')


def comprar_produto(cliente):       #função para compra/venda de produtos

    lanche = int(input('\nDigite o índice do lanche que deseja comprar: '))     #pega o lanche que deseja comprar por índice
    quantidade_lanche = int(input('\nQuantidade: '))        #digita a quantidade

    if  0 <= lanche < len(lista_produtos):      #condicional para caso seja índice inválido

        produto_comprar = lista_produtos[lanche]['Produto']     #armazena numa variável pegando por índice/chave da lista produto
        preco_comprar = lista_produtos[lanche]['Preço']
        total = quantidade_lanche * preco_comprar       #total é a multiplicação pelo preço

        compras_dict = {'Nome': cliente, 'Produto': produto_comprar, 'Quantidade': quantidade_lanche, 'Total': total}       #armazena num dicionário
        lista_vendas.append(compras_dict)       #dicionário é armazenada na lista

        print(f'\nVenda concluída {cliente}! {produto_comprar} x {quantidade_lanche} = R${total}')  #printa que a venda concluída (e as informações sobre a venda)

    else:
        print('\nÍndice inválido!')     #erro caso índice seja inválido


def cliente_que_mais_comprou():     #função cliente que mais comprou
    maior = lista_vendas[0]['Total']            #inicia a variável maior pegando o primeiro elemento da lista vendas e chave "total"(preço)
    maior_cliente = lista_vendas[0]['Nome']     #inicia uma variável pegando cliente

    for i in range(len(lista_vendas)):      #for que percorre a lista de vendas #obs: esse for percorre a lista inteira
        if lista_vendas[i]['Total'] > maior:        #se o elemento i(chave: total) for > maior, maior recebe o cliente e o maior total 
            maior_cliente = lista_vendas[i]['Nome']     #ou seja, o cliente que mais gastou
            maior = lista_vendas[i]['Total']

    print(f'\nO cliente que mais gastou foi {maior_cliente}! Com um total de R${maior}')    #printa

while True:
    try:
        mostrar_menu_principal()
        escolha = int(input('\nEscolha uma das opções acima: '))

        if escolha == 0:
            print('\nPrograma Encerrado!')
            break
        
        if escolha == 1:
            while True:
                mostrar_menu_vendedor()
                escolha_vendedor = int(input('\nEscolha uma das opções acima: '))

                if escolha_vendedor == 1:       #Cadastrar produtos
                    cadastrar_produto()
                    listar_produtos()
                    
                if escolha_vendedor == 2:       #Modificar produtos
                    listar_produtos()
                    modificar_produto()
                
                if escolha_vendedor == 3:       #Excluir produtos
                    listar_produtos()
                    excluir_produto()
                while True:
                    if escolha_vendedor == 4:       #Consultar produtos
                        consultar_produto()
                        break
                if escolha_vendedor == 0:       #Voltar
                    break
    
        
        if escolha == 2:

            nome_cliente = str(input('\nNome do cliente: '))
            while True: 
                print('\n--------------MENU CLIENTE--------------')
                print('\n(1) - Comprar produtos')
                print('(2) - Ver cardápio')
                print('(0) - Voltar') 
                escolha_cliente = int(input(f'\nOlá {nome_cliente}! Escolha uma das opções acima: '))

                if escolha_cliente == 1:        #Comprar produto
                    listar_produtos()
                    comprar_produto(nome_cliente)

                if escolha_cliente == 2:        #Ver cardápio
                    listar_produtos()
                    deseja = str(input('\nDeseja fazer algum pedido? (s/n): '))
                    if deseja == 's':
                        comprar_produto(nome_cliente)
                        
                    else:
                        break

                if escolha_cliente == 0:        #Voltar
                    break
                

    except ValueError:
        print('ERRO! Digite um valor válido')

