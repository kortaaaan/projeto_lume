<?php
session_start();

require_once __DIR__ . '/dao/UsuarioDAO.php';

$erro = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = trim($_POST['email'] ?? '');
    $senha = $_POST['senha'] ?? '';

    if ($email === '' || $senha === '') {
        $erro = 'Preencha todos os campos.';
    } else {
        $usuarioDAO = new UsuarioDAO();
        $usuario = $usuarioDAO->buscarPorEmail($email);

        if ($usuario && password_verify($senha, $usuario['senha'])) {
            $_SESSION['usuario_id'] = $usuario['id'];
            $_SESSION['usuario_nome'] = $usuario['nome'];
            $_SESSION['usuario_username'] = $usuario['username'];

            header('Location: home.php');
            exit;
        }

        $erro = 'E-mail ou senha incorretos.';
    }
}

require_once __DIR__ . '/includes/header.php';
?>

<section class="auth-card">
    <p class="eyebrow">BEM-VINDO DE VOLTA</p>
    <h1>Entrar no Lume</h1>

    <?php if ($erro !== ''): ?>
        <div class="alert"><?= htmlspecialchars($erro) ?></div>
    <?php endif; ?>

    <form method="post">
        <label>
            E-mail
            <input type="email" name="email" required>
        </label>

        <label>
            Senha
            <input type="password" name="senha" required>
        </label>

        <button class="button" type="submit">Entrar</button>
    </form>

    <p>Não possui uma conta? <a href="cadastro.php">Criar conta</a></p>
</section>

<?php require_once __DIR__ . '/includes/footer.php'; ?>
