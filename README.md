# Gestão de Ginásio em Python

Sistema de gestão de clientes de um ginásio, desenhado com programação orientada a objetos, com interface de linha de comandos e interface gráfica.

## Funcionalidades

- Registar, listar, pesquisar (por nome ou id), editar e remover clientes
- Clientes regulares e VIP, cada um com o seu desconto
- Uma classe abstrata `Gym` e uma implementação concreta, `FitnessGym`
- Persistência em SQLite
- Duas interfaces sobre o mesmo domínio: linha de comandos e desktop (Tkinter)

## Como correr

Requer Python 3.9 ou mais recente e [Poetry](https://python-poetry.org/). As versões estão em `.tool-versions`, para quem usa `asdf`.

```sh
poetry install
poetry run python cli.py       # linha de comandos
poetry run python desktop.py   # interface gráfica
poetry run pytest              # testes do domínio
```

O `web.py` é um esboço de uma interface web com FastAPI, ainda por fazer.

## Estrutura

| Ficheiro | O que faz |
| --- | --- |
| `gym.py` | Classe abstrata com as operações do ginásio |
| `fitnessGym.py` | Implementação concreta |
| `customer.py` | Clientes regulares e VIP |
| `banco.py`, `users.py` | Acesso à base de dados SQLite |
| `cli.py`, `desktop.py` | As duas interfaces |
| `tests/` | Testes do domínio com pytest |
| `oldGym/` | A primeira versão, antes da reorganização |

## Contexto

Projeto da unidade curricular de Programação por Objetos, Universidade Aberta, fevereiro de 2025.

Desenvolvido em programação a pares com um mentor.
