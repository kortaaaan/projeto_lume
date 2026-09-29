<?php
require_once __DIR__ . '/../database/Conexao.php';
require_once __DIR__ . '/../models/Usuario.php';

class UsuarioDAO
{
    private PDO $conexao;

    public function __construct()
    {
        $this->conexao = Conexao::conectar();
    }

    public function buscarPorEmail(string $email): ?array
    {
        $sql = 'SELECT id, nome, username, email, senha
                FROM usuarios
                WHERE email = ?
                LIMIT 1';

        $stmt = $this->conexao->prepare($sql);
        $stmt->execute([$email]);

        $usuario = $stmt->fetch();
        return $usuario ?: null;
    }

    public function buscarPorEmailOuUsername(string $email, string $username): ?array
    {
        $sql = 'SELECT id
                FROM usuarios
                WHERE email = ? OR username = ?
                LIMIT 1';

        $stmt = $this->conexao->prepare($sql);
        $stmt->execute([$email, $username]);

        $usuario = $stmt->fetch();
        return $usuario ?: null;
    }

    public function cadastrar(Usuario $usuario): int
    {
        $sql = 'INSERT INTO usuarios (nome, username, email, senha)
                VALUES (?, ?, ?, ?)';

        $stmt = $this->conexao->prepare($sql);
        $stmt->execute([
            $usuario->nome,
            $usuario->username,
            $usuario->email,
            $usuario->senha
        ]);

        return (int) $this->conexao->lastInsertId();
    }
}
