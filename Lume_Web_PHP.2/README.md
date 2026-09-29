# Lume Web — PHP + MySQL + HTML5 + CSS3 + DAO

Primeira fase do Lume usando PHP, MySQL, HTML5 semântico, CSS3 e padrão DAO.

## Estrutura principal

- `config.php` — configurações do MySQL.
- `database/Conexao.php` — cria a conexão PDO.
- `models/Usuario.php` — representa os dados de um usuário.
- `dao/UsuarioDAO.php` — concentra as operações SQL de usuários.
- `includes/` — arquivos reutilizáveis de sessão e estrutura HTML.
- arquivos `.php` da raiz — páginas da aplicação.
- `assets/css/style.css` — estilos.
- `database/lume.sql` — banco e tabelas.

## Instalação

1. Coloque a pasta em `C:\xampp\htdocs\Lume_Web_PHP_DAO`.
2. Ligue Apache e MySQL no XAMPP.
3. Importe `database/lume.sql` pelo phpMyAdmin.
4. Acesse `http://localhost/Lume_Web_PHP_DAO/`.

## Banco padrão

Host: 127.0.0.1
Porta: 3306
Usuário: root
Senha: vazia
Banco: lume
