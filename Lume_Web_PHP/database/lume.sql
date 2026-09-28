CREATE DATABASE IF NOT EXISTS lume CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE lume;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS galeria_publicacoes;
DROP TABLE IF EXISTS compartilhamentos;
DROP TABLE IF EXISTS salvamentos;
DROP TABLE IF EXISTS publicacao_tags;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS comentarios;
DROP TABLE IF EXISTS curtidas;
DROP TABLE IF EXISTS publicacoes;
DROP TABLE IF EXISTS galerias;
DROP TABLE IF EXISTS preferencias_usuario;
DROP TABLE IF EXISTS objetivos_usuario;
DROP TABLE IF EXISTS perfil_artista;
DROP TABLE IF EXISTS seguidores;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS usuarios;

SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    foto_perfil VARCHAR(255) NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL UNIQUE
) ENGINE=InnoDB;

CREATE TABLE perfil_artista (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL UNIQUE,
    bio TEXT NULL,
    area_principal VARCHAR(120) NULL,
    estilo VARCHAR(255) NULL,
    tecnicas VARCHAR(255) NULL,
    ferramentas VARCHAR(255) NULL,
    experiencia VARCHAR(255) NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE objetivos_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
) ENGINE=InnoDB;

CREATE TABLE preferencias_usuario (
    usuario_id INT NOT NULL,
    categoria_id INT NOT NULL,
    PRIMARY KEY (usuario_id, categoria_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE publicacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    categoria_id INT NULL,
    titulo VARCHAR(180) NOT NULL,
    descricao TEXT NULL,
    imagem VARCHAR(255) NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE curtidas (
    usuario_id INT NOT NULL,
    publicacao_id INT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (usuario_id, publicacao_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    publicacao_id INT NOT NULL,
    texto TEXT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE seguidores (
    seguidor_id INT NOT NULL,
    seguido_id INT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (seguidor_id, seguido_id),
    FOREIGN KEY (seguidor_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (seguido_id) REFERENCES usuarios(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE tags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL UNIQUE
) ENGINE=InnoDB;

CREATE TABLE publicacao_tags (
    publicacao_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (publicacao_id, tag_id),
    FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE salvamentos (
    usuario_id INT NOT NULL,
    publicacao_id INT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (usuario_id, publicacao_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE galerias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE galeria_publicacoes (
    galeria_id INT NOT NULL,
    publicacao_id INT NOT NULL,
    PRIMARY KEY (galeria_id, publicacao_id),
    FOREIGN KEY (galeria_id) REFERENCES galerias(id) ON DELETE CASCADE,
    FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE compartilhamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    publicacao_id INT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (publicacao_id) REFERENCES publicacoes(id) ON DELETE CASCADE
) ENGINE=InnoDB;

INSERT INTO categorias (nome) VALUES
('Música'), ('Poesia'), ('Fotografia'), ('Desenho'), ('Pintura'),
('Ilustração'), ('Arte Digital'), ('Escultura'), ('Cinema'),
('Dança'), ('Literatura'), ('Design');

INSERT INTO objetivos_usuario (nome) VALUES
('Publicar minhas criações'),
('Descobrir novos artistas'),
('Acompanhar artistas'),
('Montar meu portfólio'),
('Compartilhar referências');
