<?php
require_once __DIR__ . '/includes/auth.php';
require_once __DIR__ . '/includes/header.php';
?>
<section class="page">
    <div class="page-heading">
        <p class="eyebrow">INÍCIO</p>
        <h1>Olá, <?= htmlspecialchars($_SESSION['usuario_nome']) ?>.</h1>
        <p>Seu espaço no Lume está funcionando. Em seguida vamos transformar esta área no feed da rede social.</p>
    </div>
    <div class="empty-state">
        <h2>Seu feed de arte</h2>
        <p>A próxima etapa será criar publicações, categorias, curtidas, comentários e salvamentos.</p>
    </div>
</section>
<?php require_once __DIR__ . '/includes/footer.php'; ?>
