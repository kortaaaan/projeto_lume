import hashlib
import sqlite3

from app.database.database import conectar


def hash_senha(senha):
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def cadastrar_usuario(nome, username, email, senha):
    conexao = conectar()

    try:
        conexao.execute(
            """
            INSERT INTO usuarios (nome, username, email, senha)
            VALUES (?, ?, ?, ?)
            """,
            (nome, username, email, hash_senha(senha))
        )
        conexao.commit()
        return True, ""
    except sqlite3.IntegrityError:
        return False, "E-mail ou nome de usuário já cadastrado."
    finally:
        conexao.close()


def fazer_login(email, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT id, nome, username, email, bio
        FROM usuarios
        WHERE email = ? AND senha = ?
        """,
        (email, hash_senha(senha))
    )

    usuario = cursor.fetchone()
    conexao.close()
    return usuario


def atualizar_bio(usuario_id, bio):
    conexao = conectar()
    conexao.execute(
        "UPDATE usuarios SET bio = ? WHERE id = ?",
        (bio, usuario_id)
    )
    conexao.commit()
    conexao.close()
