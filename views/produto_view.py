
class ProdutoView:
    def mostrar_produto(self, produto):
        print(f"ID: {produto.id}")
        print(f"Nome: {produto.nome}")
        print(f"Preço: R${produto.preco:.2f}")
        print(f"Quantidade: {produto.quantidade}")
        print("-" * 30)

    def mostrar_produtos(self, produtos):
        for produto in produtos:
            self.mostrar_produto(produto)

    def obter_dados_produto(self):
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade em estoque: "))
        return nome, preco, quantidade