from models.database import criar_conexao, criar_tabelas
from controllers.produto_controller import ProdutoController
from controllers.cliente_controller import ClienteController
from views.produto_view import ProdutoView
from views.cliente_view import ClienteView

def main():

    database = "comercio.db"
    conn = criar_conexao(database)
    if conn is not None:
        criar_tabelas(conn)
    else:
        print("Erro! Não foi possível conectar ao banco de dados.")
        return

    produto_controller = ProdutoController(conn)
    cliente_controller = ClienteController(conn)
    produto_view = ProdutoView()
    cliente_view = ClienteView()

    while True:
        print("\nSistema de Comércio")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Clientes")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            gerenciar_produtos(produto_controller, produto_view)
        elif opcao == "2":
            gerenciar_clientes(cliente_controller, cliente_view)
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

    conn.close()

def gerenciar_produtos(controller, view):
    while True:
        print("\nGerenciamento de Produtos")
        print("1. Listar Produtos")
        print("2. Adicionar Produto")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            produtos = controller.listar_produtos()
            view.mostrar_produtos(produtos)
        elif opcao == "2":
            nome, preco, quantidade = view.obter_dados_produto()
            produto = Produto(None, nome, preco, quantidade)
            controller.criar_produto(produto)
            print("Produto adicionado com sucesso!")
        elif opcao == "3":
            id = int(input("ID do produto a ser atualizado: "))
            nome, preco, quantidade = view.obter_dados_produto()
            produto = Produto(id, nome, preco, quantidade)
            controller.atualizar_produto(produto)
            print("Produto atualizado com sucesso!")
        elif opcao == "4":
            id = int(input("ID do produto a ser removido: "))
            controller.remover_produto(id)
            print("Produto removido com sucesso!")
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

def gerenciar_clientes(controller, view):
    while True:
        print("\nGerenciamento de Clientes")
        print("1. Listar Clientes")
        print("2. Adicionar Cliente")
        print("3. Atualizar Cliente")
        print("4. Remover Cliente")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            clientes = controller.listar_clientes()
            view.mostrar_clientes(clientes)
        elif opcao == "2":
            nome, email, telefone = view.obter_dados_cliente()
            cliente = Cliente(None, nome, email, telefone)
            controller.criar_cliente(cliente)
            print("Cliente adicionado com sucesso!")
        elif opcao == "3":
            id = int(input("ID do cliente a ser atualizado: "))
            nome, email, telefone = view.obter_dados_cliente()
            cliente = Cliente(id, nome, email, telefone)
            controller.atualizar_cliente(cliente)
            print("Cliente atualizado com sucesso!")
        elif opcao == "4":
            id = int(input("ID do cliente a ser removido: "))
            controller.remover_cliente(id)
            print("Cliente removido com sucesso!")
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()