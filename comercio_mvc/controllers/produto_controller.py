from models.produto_model import Produto

class ProdutoController:
    def __init__(self, conn):
        self.conn = conn

    def criar_produto(self, produto):
        sql = '''INSERT INTO produtos(nome, preco, quantidade)
                 VALUES(?,?,?)'''
        cursor = self.conn.cursor()
        cursor.execute(sql, (produto.nome, produto.preco, produto.quantidade))
        self.conn.commit()
        return cursor.lastrowid

    def listar_produtos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        rows = cursor.fetchall()
        
        produtos = []
        for row in rows:
            produto = Produto(row[0], row[1], row[2], row[3])
            produtos.append(produto)
        
        return produtos

    def atualizar_produto(self, produto):
        sql = '''UPDATE produtos
                 SET nome = ?, preco = ?, quantidade = ?
                 WHERE id = ?'''
        cursor = self.conn.cursor()
        cursor.execute(sql, (produto.nome, produto.preco, produto.quantidade, produto.id))
        self.conn.commit()

    def remover_produto(self, id):
        sql = 'DELETE FROM produtos WHERE id = ?'
        cursor = self.conn.cursor()
        cursor.execute(sql, (id,))
        self.conn.commit()