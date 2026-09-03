# Lume

Protótipo inicial de uma rede social/portfólio para arte, poesia, música, fotografia e outras formas de criação.

## Tecnologias atuais

- Python
- Tkinter
- SQLite

## Estrutura

- `main.py`: ponto de entrada do programa.
- `app/database`: conexão e criação do banco.
- `app/models`: regras relacionadas aos dados.
- `app/views`: interface gráfica.
- `app/utils`: configurações reutilizáveis.
- `data`: banco SQLite.
- `assets`: imagens, ícones e outros recursos.

## Executar

Na pasta raiz:

```bash
python main.py
```

O banco será criado automaticamente em `data/lume.db`.

## Futuro

A ideia é separar também as telas em arquivos próprios conforme o aplicativo crescer, por exemplo:

```text
app/views/
├── app.py
├── login.py
├── cadastro.py
├── home.py
├── perfil.py
└── publicacao.py
```

Por enquanto algumas telas estão no `app.py` para manter o primeiro protótipo pequeno e compreensível.
