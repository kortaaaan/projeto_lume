from database.banco import conectar


def cadastrar_usuario(nome, username, email, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO usuarios (nome, username, email, senha)
            VALUES (?, ?, ?, ?)
        """, (nome, username, email, senha))

        conexao.commit()
        return True

    except Exception as erro:
        print("Erro ao cadastrar:", erro)
        return False

    finally:
        conexao.close()


def fazer_login(email, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, username, email
        FROM usuarios
        WHERE email = ? AND senha = ?
    """, (email, senha))

    usuario = cursor.fetchone()

    conexao.close()

    return usuario