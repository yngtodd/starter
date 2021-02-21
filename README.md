# Starter<img src='https://github.com/drkostas/starter/blob/master/img/snek.png' align='right' width='180' height='104'>

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/drkostas/starter/master/LICENSE)

## Table of Contents

+ [About](#about)
+ [Getting Started](#getting_started)
    + [Prerequisites](#prerequisites)
+ [Installing](#installing)
+ [Todo](#todo)
+ [Built With](#built_with)
+ [License](#license)
+ [Acknowledgments](#acknowledgments)

## About <a name = "about"></a>

A cookiecutter template for Python packages.

## Getting Started <a name = "getting_started"></a>

These instructions will help you generate a new python project/package from the cookiecutter template.

There are 2 ways to use this template:

1. Just open a command line and run:

```ShellSession
cookiecutter git@github.com:drkostas/starter.git --checkout cookiecutter
```

<i>You have to have cookiecutter installed first of course. If you don't,
run: `pip install cookiecutter~=1.7.2` first

2. Clone this repository and follow the next steps

### Prerequisites <a name = "prerequisites"></a>

You need to have a machine with Python > 3.6 and any Bash based shell (e.g. zsh) installed.

```ShellSession

$ python3.8 -V
Python 3.8.5

$ echo $SHELL
/usr/bin/zsh

```

## Installing <a name = "installing"></a>

All the installation steps are being handled by the [Makefile](Makefile).

Just execute the following command and fill in the project variables that will be requested:

```ShellSession
$ make install
```

## TODO <a name = "todo"></a>

Read the [TODO](TODO.md) to see the current task list.

## Built With <a name = "built_with"></a>

* [Cookie](https://cookiecutter.readthedocs.io/en/latest/README.html) - A command-line utility that
  creates projects from cookiecutters (project templates)

## License <a name = "license"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments <a name = "acknowledgments"></a>

* Thanks to PurpleBooth for
  the [README template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)

