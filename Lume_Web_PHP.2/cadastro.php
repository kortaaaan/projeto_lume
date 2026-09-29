<?php
session_start();

require_once __DIR__ . '/dao/UsuarioDAO.php';

$erro = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nome = trim($_POST['nome'] ?? '');
    $username = trim($_POST['username'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $senha = $_POST['senha'] ?? '';
    $confirmar = $_POST['confirmar_senha'] ?? '';

    if ($nome === '' || $username === '' || $email === '' || $senha === '') {
        $erro = 'Preencha todos os campos.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $erro = 'Digite um e-mail válido.';
    } elseif (strlen($senha) < 6) {
        $erro = 'A senha deve ter pelo menos 6 caracteres.';
    } elseif ($senha !== $confirmar) {
        $erro = 'As senhas não coincidem.';
    } else {
        try {
            $usuarioDAO = new UsuarioDAO();

            if ($usuarioDAO->buscarPorEmailOuUsername($email, $username)) {
                $erro = 'Esse e-mail ou nome de usuário já está cadastrado.';
            } else {
                $senhaHash = password_hash($senha, PASSWORD_DEFAULT);

                $usuario = new Usuario(
                    $nome,
                    $username,
                    $email,
                    $senhaHash
                );

                $id = $usuarioDAO->cadastrar($usuario);

                $_SESSION['usuario_id'] = $id;
                $_SESSION['usuario_nome'] = $nome;
                $_SESSION['usuario_username'] = $username;

                header('Location: home.php');
                exit;
            }
        } catch (PDOException $e) {
            $erro = 'Erro ao cadastrar: ' . $e->getMessage();
        }
    }
}

require_once __DIR__ . '/includes/header.php';
?>

<section class="auth-card">
    <p class="eyebrow">FAÇA PARTE DO LUME</p>
    <h1>Criar conta</h1>

    <?php if ($erro !== ''): ?>
        <div class="alert"><?= htmlspecialchars($erro) ?></div>
    <?php endif; ?>

    <form method="post">
        <label>
            Nome
            <input type="text" name="nome" required>
        </label>

        <label>
            Nome de usuário
            <input type="text" name="username" required>
        </label>

        <label>
            E-mail
            <input type="email" name="email" required>
        </label>

        <label>
            Senha
            <input type="password" name="senha" required>
        </label>

        <label>
            Confirmar senha
            <input type="password" name="confirmar_senha" required>
        </label>

        <button class="button" type="submit">Criar conta</button>
    </form>

    <p>Já possui uma conta? <a href="login.php">Entrar</a></p>
</section>

<?php require_once __DIR__ . '/includes/footer.php'; ?>
