# Gym Management in Python

A system for managing a gym's customers, designed with object-oriented programming, with a command-line interface and a graphical interface.

## Features

- Register, list, search (by name or id), edit and remove customers
- Regular and VIP customers, each with their own discount
- An abstract `Gym` class and a concrete implementation, `FitnessGym`
- Two interfaces: command line (customers in memory) and a Tkinter desktop app (customers in SQLite)

## Running

Requires Python 3.9 or later and [Poetry](https://python-poetry.org/). The versions are in `.tool-versions`, for those who use `asdf`.

To install Python and Poetry with [asdf](https://asdf-vm.com/) (only needed once per machine):

```sh
asdf plugin add python
asdf plugin add poetry
asdf install   # installs the versions in .tool-versions; compiling Python takes a few minutes
```

On macOS, Python has to be compiled against Homebrew's Tk 8.6. With the system's Tk 8.5, the desktop interface shows up incomplete in dark mode:

```sh
brew install tcl-tk@8
TK=$(brew --prefix tcl-tk@8)
PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$TK/include/tcl-tk' --with-tcltk-libs='-L$TK/lib -ltcl8.6 -ltk8.6'" asdf install python 3.9.16
```

Then, to install the dependencies and run:

```sh
poetry install
poetry run gym-cli        # command line
poetry run gym-desktop    # graphical interface
poetry run pytest         # tests
```

`interfaces/web.py` is a sketch of a web interface with FastAPI, not yet built.

## Structure

```
src/gym/
├── domain/       # business rules, no I/O
│   ├── gym.py            abstract class with the gym's operations
│   ├── fitness_gym.py    concrete implementation
│   └── customer.py       regular and VIP customers
├── storage/      # SQLite database access
│   ├── database.py
│   └── users.py
└── interfaces/   # ways to use the application
    ├── cli.py
    ├── desktop.py
    └── web.py
tests/            # pytest tests for the domain and the storage
```

## Context

Course project for Object-Oriented Programming (Programação por Objetos), Universidade Aberta, February 2025.

Built through pair programming with a mentor.
