# Gestão de Ginásio em Python

Sistema de gestão de clientes de um ginásio, desenhado com programação orientada a objetos, com interface de linha de comandos e interface gráfica.

## Funcionalidades

- Registar, listar, pesquisar (por nome ou id), editar e remover clientes
- Clientes regulares e VIP, cada um com o seu desconto
- Uma classe abstrata `Gym` e uma implementação concreta, `FitnessGym`
- Duas interfaces: linha de comandos (clientes em memória) e desktop em Tkinter (clientes em SQLite)

## Como correr

Requer Python 3.9 ou mais recente e [Poetry](https://python-poetry.org/). As versões estão em `.tool-versions`, para quem usa `asdf`.

Para instalar o Python e o Poetry com [asdf](https://asdf-vm.com/) (só é preciso uma vez por máquina):

```sh
asdf plugin add python
asdf plugin add poetry
asdf install   # instala as versões do .tool-versions; compilar o Python demora alguns minutos
```

No macOS, o Python tem de ser compilado com o Tk 8.6 do Homebrew. Com o Tk 8.5 do sistema, a interface desktop aparece incompleta no modo escuro:

```sh
brew install tcl-tk@8
TK=$(brew --prefix tcl-tk@8)
PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$TK/include/tcl-tk' --with-tcltk-libs='-L$TK/lib -ltcl8.6 -ltk8.6'" asdf install python 3.9.16
```

Depois, para instalar as dependências e correr:

```sh
poetry install
poetry run gym-cli        # linha de comandos
poetry run gym-desktop    # interface gráfica
poetry run pytest         # testes do domínio
```

O `interfaces/web.py` é um esboço de uma interface web com FastAPI, ainda por fazer.

## Estrutura

```
src/gym/
├── domain/       # regras de negócio, sem I/O
│   ├── gym.py            classe abstrata com as operações do ginásio
│   ├── fitness_gym.py    implementação concreta
│   └── customer.py       clientes regulares e VIP
├── storage/      # acesso à base de dados SQLite
│   ├── database.py
│   └── users.py
└── interfaces/   # formas de usar a aplicação
    ├── cli.py
    ├── desktop.py
    └── web.py
tests/            # testes do domínio com pytest
```

## Contexto

Projeto da unidade curricular de Programação por Objetos, Universidade Aberta, fevereiro de 2025.

Desenvolvido em programação a pares com um mentor.
