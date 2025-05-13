class Professor:

    def __init__(self, id=None, nome="", cpf="", email="", telefone="",
                 formacao="", data_cadastro=None, disponibilidade=1):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.formacao = formacao
        self.data_cadastro = data_cadastro
        self.disponibilidade = disponibilidade

    def __str__(self):
        status = "Disponível" if self.disponibilidade == 1 else "Indisponível"
        return f"{self.nome} - {self.cpf} ({status})"

    @property
    def esta_disponivel(self):
        return self.disponibilidade == 1

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'formacao': self.formacao,
            'data_cadastro': self.data_cadastro,
            'disponibilidade': self.disponibilidade
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            nome=data.get('nome', ''),
            cpf=data.get('cpf', ''),
            email=data.get('email', ''),
            telefone=data.get('telefone', ''),
            formacao=data.get('formacao', ''),
            data_cadastro=data.get('data_cadastro'),
            disponibilidade=data.get('disponibilidade', 1)
        )