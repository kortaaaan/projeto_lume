import tkinter as tk
from tkinter import messagebox

from app.database.database import inicializar_banco
from app.models.usuario import cadastrar_usuario, fazer_login, atualizar_bio
from app.utils.cores import BG, CARD, CARD_2, PURPLE, LILAC, YELLOW, WHITE, GRAY


class LumeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lume")
        self.geometry("1050x680")
        self.minsize(900, 600)
        self.configure(bg=BG)
        self.user = None

        inicializar_banco()
        self.mostrar_login()

    def limpar(self):
        for widget in self.winfo_children():
            widget.destroy()

    def titulo(self, parent, texto, tamanho=28):
        return tk.Label(
            parent, text=texto, bg=parent.cget("bg"),
            fg=WHITE, font=("Segoe UI", tamanho, "bold")
        )

    def botao(self, parent, texto, comando, largura=18, destaque=True):
        return tk.Button(
            parent, text=texto, command=comando, width=largura,
            bg=PURPLE if destaque else CARD_2,
            fg=WHITE, activebackground=LILAC, activeforeground=BG,
            relief="flat", bd=0, cursor="hand2",
            font=("Segoe UI", 10, "bold"), padx=8, pady=10
        )

    def campo(self, parent, label, show=None):
        tk.Label(
            parent, text=label, bg=parent.cget("bg"),
            fg=GRAY, font=("Segoe UI", 10)
        ).pack(anchor="w", pady=(8, 4))

        entry = tk.Entry(
            parent, bg=CARD_2, fg=WHITE, insertbackground=WHITE,
            relief="flat", font=("Segoe UI", 11), show=show
        )
        entry.pack(fill="x", ipady=9)
        return entry

    def mostrar_login(self):
        self.limpar()

        outer = tk.Frame(self, bg=BG)
        outer.pack(fill="both", expand=True)

        left = tk.Frame(outer, bg=BG, width=430)
        left.pack(side="left", fill="both", expand=True)

        tk.Label(
            left, text="L", bg=BG, fg=YELLOW,
            font=("Segoe UI", 62, "bold")
        ).pack(pady=(120, 0))

        tk.Label(
            left, text="LUME", bg=BG, fg=WHITE,
            font=("Segoe UI", 32, "bold")
        ).pack()

        tk.Label(
            left, text="onde ideias encontram pessoas.",
            bg=BG, fg=LILAC, font=("Segoe UI", 13)
        ).pack(pady=8)

        tk.Label(
            left,
            text="Arte • Poesia • Música • Fotografia • Desenho",
            bg=BG, fg=GRAY, font=("Segoe UI", 10)
        ).pack(pady=4)

        card = tk.Frame(outer, bg=CARD, padx=42, pady=38)
        card.pack(side="right", fill="both", expand=True, padx=80, pady=75)

        self.titulo(card, "Entrar", 24).pack(anchor="w", pady=(0, 15))
        email = self.campo(card, "E-mail")
        senha = self.campo(card, "Senha", "•")

        def entrar():
            usuario = fazer_login(email.get().strip(), senha.get())

            if not usuario:
                messagebox.showerror(
                    "Lume", "E-mail ou senha incorretos."
                )
                return

            self.user = usuario
            self.mostrar_home()

        self.botao(card, "ENTRAR", entrar).pack(fill="x", pady=(22, 10))

        tk.Label(
            card, text="Ainda não tem uma conta?",
            bg=CARD, fg=GRAY, font=("Segoe UI", 10)
        ).pack(pady=(12, 3))

        self.botao(
            card, "CRIAR CONTA",
            self.mostrar_cadastro, destaque=False
        ).pack(fill="x")

    def mostrar_cadastro(self):
        self.limpar()

        container = tk.Frame(self, bg=BG)
        container.pack(fill="both", expand=True)

        card = tk.Frame(container, bg=CARD, padx=50, pady=35)
        card.place(
            relx=.5, rely=.5, anchor="center",
            relwidth=.48, relheight=.78
        )

        self.titulo(card, "Criar conta", 24).pack(anchor="w", pady=(0, 8))

        tk.Label(
            card, text="Comece a mostrar o que você cria.",
            bg=CARD, fg=GRAY, font=("Segoe UI", 10)
        ).pack(anchor="w", pady=(0, 8))

        nome = self.campo(card, "Nome")
        username = self.campo(card, "Nome de usuário")
        email = self.campo(card, "E-mail")
        senha = self.campo(card, "Senha", "•")

        def cadastrar_click():
            dados = [
                nome.get().strip(),
                username.get().strip(),
                email.get().strip(),
                senha.get()
            ]

            if not all(dados):
                messagebox.showwarning(
                    "Lume", "Preencha todos os campos."
                )
                return

            ok, erro = cadastrar_usuario(*dados)

            if not ok:
                messagebox.showerror("Lume", erro)
                return

            messagebox.showinfo("Lume", "Conta criada com sucesso!")
            self.mostrar_login()

        self.botao(
            card, "CRIAR CONTA", cadastrar_click
        ).pack(fill="x", pady=(20, 8))

        self.botao(
            card, "VOLTAR", self.mostrar_login,
            destaque=False
        ).pack(fill="x")

    def barra_lateral(self):
        side = tk.Frame(self, bg=CARD, width=190)
        side.pack(side="left", fill="y")
        side.pack_propagate(False)

        tk.Label(
            side, text="LUME", bg=CARD, fg=YELLOW,
            font=("Segoe UI", 22, "bold")
        ).pack(pady=(30, 45))

        self.botao(
            side, "⌂  Início",
            self.mostrar_home, destaque=False
        ).pack(fill="x", padx=18, pady=5)

        self.botao(
            side, "◉  Meu perfil",
            self.mostrar_perfil, destaque=False
        ).pack(fill="x", padx=18, pady=5)

        self.botao(
            side, "+  Publicar",
            self.publicar_teste, destaque=False
        ).pack(fill="x", padx=18, pady=5)

        tk.Label(
            side, text="EXPLORE", bg=CARD, fg=GRAY,
            font=("Segoe UI", 9, "bold")
        ).pack(anchor="w", padx=25, pady=(40, 10))

        for item in ["Arte", "Poesia", "Fotografia", "Música", "Desenho"]:
            tk.Label(
                side, text=f"  {item}", bg=CARD, fg=WHITE,
                font=("Segoe UI", 10)
            ).pack(anchor="w", padx=25, pady=6)

        self.botao(
            side, "Sair", self.mostrar_login,
            destaque=False
        ).pack(side="bottom", fill="x", padx=18, pady=20)

    def mostrar_home(self):
        self.limpar()
        self.barra_lateral()

        main = tk.Frame(self, bg=BG)
        main.pack(
            side="left", fill="both", expand=True,
            padx=35, pady=30
        )

        tk.Label(
            main, text=f"Olá, {self.user[1]} 👋",
            bg=BG, fg=WHITE,
            font=("Segoe UI", 25, "bold")
        ).pack(anchor="w")

        tk.Label(
            main, text="Descubra novas formas de criar.",
            bg=BG, fg=GRAY,
            font=("Segoe UI", 11)
        ).pack(anchor="w", pady=(3, 25))

        self.cartao_publicacao(
            main,
            "Começando no Lume",
            "Este é o primeiro teste visual da sua rede social artística.",
            "LUME • Projeto Integrador"
        )

        self.cartao_publicacao(
            main,
            "Seu espaço criativo",
            "Aqui entrarão fotografias, poesias, desenhos, músicas e outros trabalhos.",
            "Comunidade Lume"
        )

    def cartao_publicacao(self, parent, titulo, descricao, autor):
        card = tk.Frame(parent, bg=CARD, padx=25, pady=20)
        card.pack(fill="x", pady=10)

        tk.Label(
            card, text=autor, bg=CARD, fg=LILAC,
            font=("Segoe UI", 9, "bold")
        ).pack(anchor="w")

        tk.Label(
            card, text=titulo, bg=CARD, fg=WHITE,
            font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", pady=(7, 4))

        tk.Label(
            card, text=descricao, bg=CARD, fg=GRAY,
            font=("Segoe UI", 10),
            wraplength=700, justify="left"
        ).pack(anchor="w")

        actions = tk.Frame(card, bg=CARD)
        actions.pack(anchor="w", pady=(15, 0))

        tk.Label(
            actions, text="♡  Curtir", bg=CARD, fg=WHITE,
            font=("Segoe UI", 9)
        ).pack(side="left", padx=(0, 20))

        tk.Label(
            actions, text="○  Comentar", bg=CARD, fg=WHITE,
            font=("Segoe UI", 9)
        ).pack(side="left")

    def mostrar_perfil(self):
        self.limpar()
        self.barra_lateral()

        main = tk.Frame(self, bg=BG)
        main.pack(
            side="left", fill="both", expand=True,
            padx=45, pady=40
        )

        tk.Label(
            main, text="●", bg=BG, fg=LILAC,
            font=("Segoe UI", 65)
        ).pack()

        tk.Label(
            main, text=self.user[1], bg=BG, fg=WHITE,
            font=("Segoe UI", 25, "bold")
        ).pack()

        tk.Label(
            main, text=f"@{self.user[2]}",
            bg=BG, fg=LILAC,
            font=("Segoe UI", 11)
        ).pack(pady=4)

        bio = self.user[4] or "Sua bio aparecerá aqui."

        tk.Label(
            main, text=bio, bg=BG, fg=GRAY,
            font=("Segoe UI", 11),
            wraplength=650
        ).pack(pady=15)

        self.botao(
            main, "EDITAR BIO",
            self.editar_bio, largura=15
        ).pack(pady=8)

        stats = tk.Frame(main, bg=CARD, padx=25, pady=18)
        stats.pack(fill="x", pady=25)

        for texto in [
            "0 Publicações",
            "0 Seguidores",
            "0 Seguindo",
            "0 Amigos"
        ]:
            tk.Label(
                stats, text=texto, bg=CARD, fg=WHITE,
                font=("Segoe UI", 10, "bold")
            ).pack(side="left", expand=True)

    def editar_bio(self):
        janela = tk.Toplevel(self)
        janela.title("Editar bio")
        janela.geometry("430x220")
        janela.configure(bg=CARD)

        tk.Label(
            janela, text="Sua bio", bg=CARD, fg=WHITE,
            font=("Segoe UI", 15, "bold")
        ).pack(pady=(25, 10))

        texto = tk.Text(
            janela, height=5, bg=CARD_2, fg=WHITE,
            insertbackground=WHITE, relief="flat"
        )
        texto.pack(fill="x", padx=30)
        texto.insert("1.0", self.user[4] or "")

        def salvar():
            nova_bio = texto.get("1.0", "end").strip()
            atualizar_bio(self.user[0], nova_bio)

            self.user = (
                self.user[0],
                self.user[1],
                self.user[2],
                self.user[3],
                nova_bio
            )

            janela.destroy()
            self.mostrar_perfil()

        self.botao(
            janela, "SALVAR", salvar, largura=12
        ).pack(pady=15)

    def publicar_teste(self):
        messagebox.showinfo(
            "Em desenvolvimento",
            "A tela de publicação será a próxima etapa."
        )
