from models.cliente_model import Cliente

class ClienteController:
    def __init__(self, conn):
        self.conn = conn

    def criar_cliente(self, cliente):
        sql = '''INSERT INTO clientes(nome, email, telefone)
                 VALUES(?,?,?)'''
        cursor = self.conn.cursor()
        cursor.execute(sql, (cliente.nome, cliente.email, cliente.telefone))
        self.conn.commit()
        return cursor.lastrowid

    def listar_clientes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()
        
        clientes = []
        for row in rows:
            cliente = Cliente(row[0], row[1], row[2], row[3])
            clientes.append(cliente)
        
        return clientes

    def atualizar_cliente(self, cliente):
        sql = '''UPDATE clientes
                 SET nome = ?, email = ?, telefone = ?
                 WHERE id = ?'''
        cursor = self.conn.cursor()
        cursor.execute(sql, (cliente.nome, cliente.email, cliente.telefone, cliente.id))
        self.conn.commit()

    def remover_cliente(self, id):
        sql = 'DELETE FROM clientes WHERE id = ?'
        cursor = self.conn.cursor()
        cursor.execute(sql, (id,))
        self.conn.commit()