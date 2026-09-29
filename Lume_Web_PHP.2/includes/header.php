<?php
if (session_status() !== PHP_SESSION_ACTIVE) {
    session_start();
}
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lume</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header class="site-header">
    <nav class="navbar" aria-label="Navegação principal">
        <a class="logo" href="index.php">LUME</a>

        <div class="nav-links">
            <?php if (!empty($_SESSION['usuario_id'])): ?>
                <a href="home.php">Início</a>
                <a href="perfil.php">Meu perfil</a>
                <a href="logout.php">Sair</a>
            <?php else: ?>
                <a href="login.php">Entrar</a>
                <a href="cadastro.php">Criar conta</a>
            <?php endif; ?>
        </div>
    </nav>
</header>

<main class="container">
