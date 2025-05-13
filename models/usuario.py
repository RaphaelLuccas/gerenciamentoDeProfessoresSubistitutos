class Usuario:

    def __init__(self, id=None, nome_usuario="", senha="", nivel_acesso=1):
        self.id = id
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.nivel_acesso = nivel_acesso

    def __str__(self):
        return f"Usuário: {self.nome_usuario} (Nível: {self.nivel_acesso})"

    @property
    def is_admin(self):
        return self.nivel_acesso >= 2

    def to_dict(self):
        return {
            'id': self.id,
            'nome_usuario': self.nome_usuario,
            'senha': self.senha,
            'nivel_acesso': self.nivel_acesso
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            nome_usuario=data.get('nome_usuario', ''),
            senha=data.get('senha', ''),
            nivel_acesso=data.get('nivel_acesso', 1)
        )