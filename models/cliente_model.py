class Cliente:
    def __init__(self, id=None, nome=None, email=None, telefone=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone
        }