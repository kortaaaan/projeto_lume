from models.usuario import cadastrar_usuario, fazer_login


print("=== LUME ===")
print("1 - Cadastrar")
print("2 - Login")

opcao = input("Escolha: ")


if opcao == "1":

    nome = input("Nome: ")
    username = input("Username: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    resultado = cadastrar_usuario(
        nome,
        username,
        email,
        senha
    )

    if resultado:
        print("Usuário cadastrado com sucesso!")
    else:
        print("Não foi possível cadastrar o usuário.")


elif opcao == "2":

    email = input("E-mail: ")
    senha = input("Senha: ")

    usuario = fazer_login(email, senha)

    if usuario:
        print()
        print("Login realizado com sucesso!")
        print(f"Bem-vindo, {usuario[1]}!")
        print(f"Username: @{usuario[2]}")
    else:
        print("E-mail ou senha incorretos.")


else:
    print("Opção inválida.")