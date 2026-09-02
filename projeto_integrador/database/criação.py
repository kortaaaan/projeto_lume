import sqlite3

CAMINHO_BANCO = "database/lume.db"

conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()

# =========================
# USUÁRIOS
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    bio TEXT,
    foto_perfil TEXT,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# =========================
# CATEGORIAS
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL UNIQUE
)
""")

categorias = [
    ("Arte",),
    ("Poesia",),
    ("Fotografia",),
    ("Música",),
    ("Desenho",),
    ("Vídeo",)
]

cursor.executemany("""
INSERT OR IGNORE INTO categorias (nome)
VALUES (?)
""", categorias)

# =========================
# PUBLICAÇÕES
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS publicacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT,
    arquivo TEXT NOT NULL,
    data_publicacao DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
)
""")

# =========================
# CURTIDAS
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS curtidas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    publicacao_id INTEGER NOT NULL,

    UNIQUE(usuario_id, publicacao_id),

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id)
)
""")

# =========================
# COMENTÁRIOS
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS comentarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    publicacao_id INTEGER NOT NULL,
    texto TEXT NOT NULL,
    data_comentario DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id)
)
""")

# =========================
# SEGUIDORES
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS seguidores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    seguidor_id INTEGER NOT NULL,
    seguido_id INTEGER NOT NULL,

    UNIQUE(seguidor_id, seguido_id),
    CHECK(seguidor_id != seguido_id),

    FOREIGN KEY (seguidor_id) REFERENCES usuarios(id),
    FOREIGN KEY (seguido_id) REFERENCES usuarios(id)
)
""")

# =========================
# AMIZADES
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS amizades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    amigo_id INTEGER NOT NULL,

    UNIQUE(usuario_id, amigo_id),
    CHECK(usuario_id != amigo_id),

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (amigo_id) REFERENCES usuarios(id)
)
""")

# =========================
# TAGS
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS publicacao_tags (
    publicacao_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,

    PRIMARY KEY (publicacao_id, tag_id),

    FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
)
""")

# =========================
# FAVORITOS
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS favoritos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    publicacao_id INTEGER NOT NULL,

    UNIQUE(usuario_id, publicacao_id),

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id)
)
""")

# =========================
# PROJETOS
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS projetos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT,
    capa TEXT,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS projeto_publicacoes (
    projeto_id INTEGER NOT NULL,
    publicacao_id INTEGER NOT NULL,

    PRIMARY KEY (projeto_id, publicacao_id),

    FOREIGN KEY (projeto_id) REFERENCES projetos(id),
    FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id)
)
""")

# =========================
# TRIGGER DE AMIZADE
# =========================

cursor.execute("""
CREATE TRIGGER IF NOT EXISTS criar_amizade
AFTER INSERT ON seguidores
WHEN EXISTS (
    SELECT 1
    FROM seguidores
    WHERE seguidor_id = NEW.seguido_id
    AND seguido_id = NEW.seguidor_id
)
BEGIN
    INSERT OR IGNORE INTO amizades (usuario_id, amigo_id)
    VALUES (NEW.seguidor_id, NEW.seguidor_id);

    INSERT OR IGNORE INTO amizades (usuario_id, amigo_id)
    VALUES (NEW.seguidor_id, NEW.seguidor_id);
END
""")

# =========================
# TRIGGER DE REMOÇÃO
# =========================

cursor.execute("""
CREATE TRIGGER IF NOT EXISTS remover_amizade
AFTER DELETE ON seguidores
BEGIN
    DELETE FROM amizades
    WHERE (usuario_id = OLD.seguidor_id AND amigo_id = OLD.seguido_id)
        OR (usuario_id = OLD.seguido_id AND amigo_id = OLD.seguidor_id);
END
""")

conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso!")