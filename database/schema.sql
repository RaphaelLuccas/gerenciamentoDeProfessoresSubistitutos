-- Criação das tabelas para o Sistema de Gerenciamento de Professores Substitutos

-- Tabela de Usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_usuario TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    nivel_acesso INTEGER DEFAULT 1
);

-- Tabela de Professores Substitutos
CREATE TABLE IF NOT EXISTS professores_substitutos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    email TEXT,
    telefone TEXT,
    formacao TEXT,
    data_cadastro TEXT,
    disponibilidade INTEGER DEFAULT 1
);

-- Tabela de Disciplinas
CREATE TABLE IF NOT EXISTS disciplinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    codigo TEXT UNIQUE NOT NULL,
    carga_horaria INTEGER,
    departamento TEXT
);

-- Tabela de Substituições
CREATE TABLE IF NOT EXISTS substituicoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    professor_id INTEGER,
    disciplina_id INTEGER,
    data_inicio TEXT,
    data_fim TEXT,
    status TEXT DEFAULT 'Agendada',
    observacoes TEXT,
    FOREIGN KEY (professor_id) REFERENCES professores_substitutos(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
);

-- Inserção de usuário administrador padrão (se não existir)
INSERT OR IGNORE INTO usuarios (nome_usuario, senha, nivel_acesso)
VALUES ('admin', 'admin123', 2);