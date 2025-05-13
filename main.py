from database.database import Database
import os


def inicializar_banco():
    db = Database()

    script_path = os.path.join('database', 'schema.sql')

    if db.executar_script(script_path):
        print("Banco de dados inicializado com sucesso!")
    else:
        print("Falha ao inicializar o banco de dados.")

    db.fechar()


if __name__ == "__main__":
    inicializar_banco()
    print("Sistema de Gerenciamento de Professores Substitutos - Inicializado")