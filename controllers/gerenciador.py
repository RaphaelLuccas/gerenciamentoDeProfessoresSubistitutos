from models.usuario import Usuario
from database.database import Database


class UsuarioController:

    def __init__(self, db):
        self.db = db

    def autenticar(self, nome_usuario, senha):
        query = """
                SELECT id, nome_usuario, senha, nivel_acesso
                FROM usuarios
                WHERE nome_usuario = ? \
                  AND senha = ? \
                """
        resultados = self.db.executar_select(query, (nome_usuario, senha))

        if resultados:
            return Usuario.from_dict(resultados[0])
        return None

    def criar(self, usuario):
        dados = {
            'nome_usuario': usuario.nome_usuario,
            'senha': usuario.senha,
            'nivel_acesso': usuario.nivel_acesso
        }

        usuario_id = self.db.inserir('usuarios', dados)
        if usuario_id:
            usuario.id = usuario_id
            return True
        return False

    def listar_todos(self):
        query = "SELECT * FROM usuarios"
        resultados = self.db.executar_select(query)
        return [Usuario.from_dict(user) for user in resultados]

    def buscar_por_id(self, usuario_id):
        query = "SELECT * FROM usuarios WHERE id = ?"
        resultados = self.db.executar_select(query, (usuario_id,))

        if resultados:
            return Usuario.from_dict(resultados[0])
        return None

    def atualizar(self, usuario):
        dados = {
            'nome_usuario': usuario.nome_usuario,
            'senha': usuario.senha,
            'nivel_acesso': usuario.nivel_acesso
        }

        return self.db.atualizar('usuarios', dados, 'id = ?', (usuario.id,)) > 0

    def remover(self, usuario_id):
        return self.db.remover('usuarios', 'id = ?', (usuario_id,)) > 0