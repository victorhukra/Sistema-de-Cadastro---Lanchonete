lista_produtos = [
    {'Produto': 'X-Burguer', 'Preço': 17.00},
    {'Produto': 'Dog Duplo', 'Preço': 13.50},
    {'Produto': 'Dog Bacon', 'Preço': 17.50}
]
lista_vendas = []

def cadastrar_produto():    # função para cadastrar os produtos        
    quantidade_cadastrar = int(input('Quantidade de produtos que deseja cadastrar: '))  # quantidade de produtos que deseja cadastrar
    for i in range(quantidade_cadastrar):   # for com a quantidade de produtos
        nome_produto = str(input(f'Digite o nome do {i + 1}° produto: '))   # variavel para nome do produto
        preco_produto = float(input(f'Digite o preço do {i + 1}° produto: '))   # variavel para o preço do produto

        p = {'Produto': nome_produto, 'Preço': preco_produto}       # dicionario para armazenar, flexível

        lista_produtos.append(p)        # armazena o dicionario na lista de produtos


def listar_produtos():      # função para listar os produtos 
    if len(lista_produtos) == 0:
        print('\nNão há produtos cadastrados!')
        return

    print('\nLista de produtos: ')
    for i, prod in enumerate(lista_produtos):       # for enumerate para pegar indice e valor 
        print(f"{i} - {prod['Produto']} | R${prod['Preço']:.2f}")      # printa de forma mais legível


def modificar_produto():        # função para modificar um produto
    if len(lista_produtos) == 0:
        print('\nNão há produtos cadastrados para modificar!')
        return
    
    listar_produtos()
    indice_modificar = int(input('\nDigite o índice do produto que deseja modificar: '))    # pega o produto por índice

    if  0 <= indice_modificar < len(lista_produtos):        # condição para caso o índice seja inválido

        modificar_nome = str(input('Digite o nome do novo produto: '))      # variavel para guardar o novo nome 
        modificar_preco = float(input('Digite o preço: R$'))        # variavel para guardar o novo preço

        lista_produtos[indice_modificar]['Produto'] = modificar_nome       # atualiza por índice/chave = variavel
        lista_produtos[indice_modificar]['Preço'] = modificar_preco
        print('\n----------------ATUALIZADO----------------')
        listar_produtos()                 # printa a lista de produtos atualizada

    else:
        print('\nÍndice inválido!')     # se o índice não for válido printa erro


def excluir_produto():      # função para excluir o produto
    if len(lista_produtos) == 0:
        print('\nNão há produtos cadastrados para excluir!')
        return

    listar_produtos()
    varexcluir = int(input('\nDigite o índice do produto que deseja excluir: '))        # pega por índice

    if 0 <= varexcluir < len(lista_produtos):       # condição para caso o índice seja inválido

        removido = lista_produtos.pop(varexcluir)        # pop para excluir 
        print(f"\nProduto '{removido['Produto']}' excluído com sucesso!")
        print('\n----------------ATUALIZADO----------------')
        listar_produtos()       # printa a lista atualizada
    
    else:
        print('\nÍndice inválido!')     # erro caso seja inválido


def cliente_que_mais_comprou():     # função cliente que mais comprou
    if len(lista_vendas) == 0:
        print('\nNão há vendas registradas!')
        return

    # em vez de olhar só a maior venda, soma tudo que cada cliente gastou
    gastos_por_cliente = {}

    for venda in lista_vendas:
        nome = venda['Nome']
        total_venda = venda['Total']
        gastos_por_cliente[nome] = gastos_por_cliente.get(nome, 0) + total_venda

    maior_cliente = None
    maior_total = 0

    for nome, total in gastos_por_cliente.items():
        if total > maior_total:
            maior_total = total
            maior_cliente = nome

    print(f'\nO cliente que mais gastou foi {maior_cliente}! Com um total de R${maior_total:.2f}')


def listar_vendas_filtrado_por_data():
    if len(lista_vendas) == 0:
        print('\nNão há vendas registradas!')
        return

    data_busca = input('\nDigite a data da venda (formato livre, ex: 25/11/2025): ')

    encontrou = False
    print(f'\nVendas na data: {data_busca}')
    for i, venda in enumerate(lista_vendas):
        if venda.get('Data') == data_busca:
            print(f"\nVenda {i}:")
            print(f"Cliente: {venda['Nome']}")
            print(f"Data: {venda.get('Data', 'Sem data')}")
            print(f"Produto: {venda['Produto']} x {venda['Quantidade']}")
            print(f"Total: R${venda['Total']:.2f}")
            encontrou = True

    if not encontrou:
        print('\nNenhuma venda encontrada nessa data.')


def listar_vendas_geral():
    if len(lista_vendas) == 0:
        print('\nNão há vendas registradas!')
        return

    print('\nLista geral de vendas:')
    for i, venda in enumerate(lista_vendas):
        print(f"\nVenda {i}:")
        print(f"Cliente: {venda['Nome']}")
        print(f"Data: {venda.get('Data', 'Sem data')}")
        print(f"Produto: {venda['Produto']} x {venda['Quantidade']}")
        print(f"Total: R${venda['Total']:.2f}")


def consultar_produto():
    if len(lista_vendas) == 0:      # se não tiver vendas registradas (len == 0) printa erro
        print('\nNão há vendas registradas!')
    
    else:       # se já tiver vendas chama função menu consultar produto 
        while True:
            menu_consultar_produto()
            try:
                escolha_consultar = int(input('\nEscolha uma das opções acima: '))      # escolhe a opção
            except ValueError:
                print('\nOpção inválida!')
                continue

            if escolha_consultar == 1:     
                # aqui você pode usar tanto como "data específica" quanto:
                # se quiser ver todas, basta dar Enter vazio na data -> eu usei função separada pra geral
                listar_vendas_filtrado_por_data()
            
            elif escolha_consultar == 2:      # se a escolha for 2 vai printar o cliente que mais gastou
                cliente_que_mais_comprou()

            elif escolha_consultar == 3:
                listar_vendas_geral()

            elif escolha_consultar == 0:
                break

            else:
                print('\nOpção inválida!')


def menu_consultar_produto():       # menu consultar produto
    print('\n--------------MENU CONSULTAR--------------')
    print('\n(1) - Vendas em data específica')
    print('(2) - Cliente que mais gastou')
    print('(3) - Lista geral de vendas')
    print('(0) - Sair')  


def mostrar_menu_principal():       # menu principal
    print('\n--------------MENU PRINCIPAL--------------')
    print('\n(1) - Vendedor')
    print('(2) - Cliente')
    print('(0) - Sair')


def mostrar_menu_vendedor():        # menu vendedor
    print('\n--------------MENU VENDEDOR--------------')
    print('\n(1) - Cadastrar produtos')
    print('(2) - Modificar produtos')
    print('(3) - Excluir produtos')
    print('(4) - Consultar vendas')
    print('(0) - Voltar')


def comprar_produto(cliente):       # função para compra/venda de produtos
    if len(lista_produtos) == 0:
        print('\nNão há produtos cadastrados! Peça para o vendedor cadastrar primeiro.')
        return

    data_venda = input('\nDigite a data da venda (ex: 25/11/2025): ')

    lanche = int(input('\nDigite o índice do lanche que deseja comprar: '))     # pega o lanche que deseja comprar por índice
    quantidade_lanche = int(input('\nQuantidade: '))        # digita a quantidade

    if  0 <= lanche < len(lista_produtos):      # condicional para caso seja índice inválido

        produto_comprar = lista_produtos[lanche]['Produto']     # armazena numa variável pegando por índice/chave da lista produto
        preco_comprar = lista_produtos[lanche]['Preço']
        total = quantidade_lanche * preco_comprar       # total é a multiplicação pelo preço

        compras_dict = {
            'Nome': cliente,
            'Produto': produto_comprar,
            'Quantidade': quantidade_lanche,
            'Total': total,
            'Data': data_venda
        }       # armazena num dicionário

        lista_vendas.append(compras_dict)       # dicionário é armazenada na lista

        print(f'\nVenda concluída {cliente}! {produto_comprar} x {quantidade_lanche} = R${total:.2f} na data {data_venda}')  # printa que a venda concluída (e as informações sobre a venda)

    else:
        print('\nÍndice inválido!')     # erro caso índice seja inválido


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

                if escolha_vendedor == 1:       # Cadastrar produtos
                    cadastrar_produto()
                    listar_produtos()
                    
                elif escolha_vendedor == 2:       # Modificar produtos
                    modificar_produto()
                
                elif escolha_vendedor == 3:       # Excluir produtos
                    excluir_produto()

                elif escolha_vendedor == 4:       # Consultar vendas
                    consultar_produto()

                elif escolha_vendedor == 0:       # Voltar
                    break

                else:
                    print('\nOpção inválida!')   
    
        if escolha == 2:

            nome_cliente = str(input('\nNome do cliente: '))
            while True: 
                print('\n--------------MENU CLIENTE--------------')
                print('\n(1) - Comprar produtos')
                print('(2) - Ver cardápio')
                print('(0) - Voltar') 
                escolha_cliente = int(input(f'\nOlá {nome_cliente}! Escolha uma das opções acima: '))

                if escolha_cliente == 1:        # Comprar produto
                    listar_produtos()
                    comprar_produto(nome_cliente)

                elif escolha_cliente == 2:        # Ver cardápio
                    listar_produtos()
                    deseja = str(input('\nDeseja fazer algum pedido? (s/n): '))
                    if deseja == 's':
                        comprar_produto(nome_cliente)
                    else:
                        break

                elif escolha_cliente == 0:        # Voltar
                    break

                else:
                    print('\nOpção inválida!')
                

    except ValueError:
        print('ERRO! Digite um valor válido')
