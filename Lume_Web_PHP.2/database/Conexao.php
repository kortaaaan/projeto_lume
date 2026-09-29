<?php
require_once __DIR__ . '/../config.php';

class Conexao
{
    public static function conectar(): PDO
    {
        $dsn = 'mysql:host=' . DB_HOST
             . ';port=' . DB_PORT
             . ';dbname=' . DB_NAME
             . ';charset=utf8mb4';

        try {
            return new PDO($dsn, DB_USER, DB_PASS, [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            ]);
        } catch (PDOException $e) {
            die('Não foi possível conectar ao MySQL: ' . htmlspecialchars($e->getMessage()));
        }
    }
}
