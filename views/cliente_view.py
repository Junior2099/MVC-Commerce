class ClienteView:
    def mostrar_cliente(self, cliente):
        print(f"ID: {cliente.id}")
        print(f"Nome: {cliente.nome}")
        print(f"Email: {cliente.email}")
        print(f"Telefone: {cliente.telefone}")
        print("-" * 30)

    def mostrar_clientes(self, clientes):
        for cliente in clientes:
            self.mostrar_cliente(cliente)

    def obter_dados_cliente(self):
        nome = input("Nome do cliente: ")
        email = input("Email do cliente: ")
        telefone = input("Telefone do cliente: ")
        return nome, email, telefone