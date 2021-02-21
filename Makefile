# Makefile for the starter module

SHELL=/bin/bash
PYTHON_VERSION=3.8
BASE=~/anaconda3/envs/starter_cookiecutter
BIN=$(BASE)/bin
CLEAN_COMMAND="conda env remove -p $(BASE)"
CREATE_COMMAND="conda create --prefix $(BASE) python=$(PYTHON_VERSION) -y"

all:
	$(MAKE) help
help:
	@echo
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo "                                              DISPLAYING HELP                                              "
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo
	@echo "make help"
	@echo "       Display this message"
	@echo "make install"
	@echo "       Call delete_conda_env, create_conda_env, cookiecutter, requirements, and clean"
	@echo "make delete_env"
	@echo "       Delete the current conda env or virtualenv"
	@echo "make create_env"
	@echo "       Create a new conda env or virtualenv for the specified python version"
	@echo "make requirements"
	@echo "       Install python requirements for cookiecutter"
	@echo "make cookiecutter"
	@echo "       Run cookiecutter and generate a project from the template"
	@echo "make clean"
	@echo "       Not Yet Supported"
	@echo "-----------------------------------------------------------------------------------------------------------"
install:
	$(MAKE) delete_env
	$(MAKE) create_env
	$(MAKE) requirements
	$(MAKE) cookiecutter
	$(MAKE) clean
	@echo "Installation Successful!"
delete_env:
	@echo "Deleting virtual environment.."
	eval $(DELETE_COMMAND)
create_env:
	@echo "Creating virtual environment.."
	eval $(CREATE_COMMAND)
requirements:
	@echo "Installing requirements.."
	$(PYTHON_BIN)pip install -r requirements.txt
cookiecutter:
	@echo "Running cookiecutter.."
	$(PYTHON_BIN)cookiecutter . -f
clean:
	@echo "Clean command not yet supported"
	#$(PYTHON_BIN)python setup.py clean


.PHONY: help install delete_env create_env requirements cookiecutter clean