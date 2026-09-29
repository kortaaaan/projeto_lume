<?php
require_once __DIR__ . '/includes/auth.php';
require_once __DIR__ . '/includes/header.php';
?>

<section class="page">
    <p class="eyebrow">PORTFÓLIO</p>
    <h1><?= htmlspecialchars($_SESSION['usuario_nome']) ?></h1>
    <p>@<?= htmlspecialchars($_SESSION['usuario_username']) ?></p>

    <article class="empty-state">
        <h2>Perfil artístico</h2>
        <p>
            Depois vamos adicionar bio, características do artista,
            técnicas, estilos e galerias.
        </p>
    </article>
</section>

<?php require_once __DIR__ . '/includes/footer.php'; ?>
