import sqlite3
import os
from datetime import datetime

class Database:

    def __init__(self, db_file="professores_substitutos.db"):
        self.db_file = db_file
        self.conn = None
        self.cursor = None
        self.conectar()

    def conectar(self):
        try:
            db_exists = os.path.exists(self.db_file)
            self.conn = sqlite3.connect(self.db_file)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False

    def executar_script(self, script_file):
        try:
            with open(script_file, 'r') as f:
                sql_script = f.read()

            self.cursor.executescript(sql_script)
            self.conn.commit()
            return True
        except (sqlite3.Error, IOError) as e:
            print(f"Erro ao executar script: {e}")
            return False

    def executar_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao executar query: {e}")
            return False

    def executar_select(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            return [dict(row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Erro ao executar select: {e}")
            return []

    def inserir(self, tabela, dados):
        try:
            colunas = ', '.join(dados.keys())
            placeholders = ', '.join(['?' for _ in dados])
            valores = tuple(dados.values())

            query = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"
            self.cursor.execute(query, valores)
            self.conn.commit()

            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")
            return None

    def atualizar(self, tabela, dados, condicao, valores_condicao):
        try:
            set_clause = ', '.join([f"{coluna} = ?" for coluna in dados.keys()])
            valores = tuple(dados.values()) + valores_condicao

            query = f"UPDATE {tabela} SET {set_clause} WHERE {condicao}"
            self.cursor.execute(query, valores)
            self.conn.commit()

            return self.cursor.rowcount
        except sqlite3.Error as e:
            print(f"Erro ao atualizar dados: {e}")
            return 0

    def remover(self, tabela, condicao, valores_condicao):
        try:
            query = f"DELETE FROM {tabela} WHERE {condicao}"
            self.cursor.execute(query, valores_condicao)
            self.conn.commit()

            return self.cursor.rowcount
        except sqlite3.Error as e:
            print(f"Erro ao remover dados: {e}")
            return 0

    def fechar(self):
        if self.conn:
            self.conn.close()