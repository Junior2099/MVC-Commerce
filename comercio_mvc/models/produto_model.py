class Produto:
    def __init__(self, id=None, nome=None, preco=None, quantidade=None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco,
            'quantidade': self.quantidade
        }