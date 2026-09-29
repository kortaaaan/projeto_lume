<?php
class Usuario
{
    public ?int $id;
    public string $nome;
    public string $username;
    public string $email;
    public string $senha;

    public function __construct(
        string $nome,
        string $username,
        string $email,
        string $senha,
        ?int $id = null
    ) {
        $this->id = $id;
        $this->nome = $nome;
        $this->username = $username;
        $this->email = $email;
        $this->senha = $senha;
    }
}
