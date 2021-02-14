# Makefile for the starter module

SHELL=/bin/bash
PYTHON_VERSION=3.8
# You can use either venv (virtualenv) or conda env
CONDA_BASE=~/anaconda3/envs/starter
CONDA_BIN=$(CONDA_BASE)/bin
VENV_BASE=venv
VENV_BIN=$(VENV_BASE)/bin
# TESTS_FOLDER=tests
#--------------------------------------------
ifeq ($(server),prod)
	AN_ENVIRONMENT_SPECIFIC_VARIABLE='production'
	SETUP_FLAG=''
	DEBUG=False
else ifeq ($(server),dev)
	AN_ENVIRONMENT_SPECIFIC_VARIABLE='development'
	SETUP_FLAG=''
	DEBUG=True
else ifeq ($(server),local)
	AN_ENVIRONMENT_SPECIFIC_VARIABLE='local'
	SETUP_FLAG='--local'
	DEBUG=True
else
	AN_ENVIRONMENT_SPECIFIC_VARIABLE='production'
	SETUP_FLAG=
	DEBUG=True
endif
#--------------------------------------------


all:
	$(MAKE) help
help:
	@echo
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo "                                              DISPLAYING HELP                                              "
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo "make help"
	@echo "       Display this message"
	@echo "make install"
	@echo "       Call clean delete_conda_env create_conda_env setup run_tests"
	@echo "make clean"
	@echo "       Delete all './build ./dist ./*.pyc ./*.tgz ./*.egg-info' files"
	@echo "make delete_venv"
	@echo "       Delete the current venv"
	@echo "make delete_conda_env"
	@echo "       Delete the current conda env"
	@echo "make create_venv"
	@echo "       Create a new venv for the specified python version"
	@echo "make create_conda_env"
	@echo "       Create a new conda env for the specified python version"
	# @echo "make requirements"
	# @echo "       Upgrade pip and install the requirements"
	@echo "make setup"
	@echo "       Call setup.py install"
	@echo "make run_tests"
	@echo "       Run all the tests from the specified folder"
	# @echo "make clean_pyc"
	# @echo "       Clean all the pyc files"
	# @echo "make clean_build"
	# @echo "       Clean all the build folders"
	@echo "-----------------------------------------------------------------------------------------------------------"
install:
	$(MAKE) clean
	# $(MAKE) delete_venv  # Pick virtualenv or conda
	$(MAKE) delete_conda_env
	# $(MAKE) create_venv  # Pick virtualenv or conda
	$(MAKE) create_conda_env
	# $(MAKE) requirements  # Step is done by setup.py install
	$(MAKE) setup
	$(MAKE) run_tests
	@echo "Installation Successful!"
clean:
	# $(MAKE) clean_pyc
	# $(MAKE) clean_build
	$(PYTHON_BIN)python setup.py clean
delete_venv:
	@echo "Deleting venv.."
	rm -rf $(VENV_BASE)
delete_conda_env:
	@echo "Deleting conda env.."
	conda env remove -p $(CONDA_BASE)
create_venv:
	@echo "Creating venv.."
	python$(PYTHON_VERSION) -m venv $(VENV_BASE)
create_conda_env:
	@echo "Creating conda env.."
	conda create --prefix $(CONDA_BASE) python=$(PYTHON_VERSION)
#requirements:
#	@echo "Upgrading pip.."
#	$(PYTHON_BIN)pip install --upgrade pip wheel setuptools
#	@echo "Installing requirements.."
#	$(PYTHON_BIN)pip install -r requirements.txt
run_tests:
	# source $(PYTHON_BIN)activate && \
	# export PYTHONPATH=$(PWD) && \
	# cd tests && python -m unittest
	$(PYTHON_BIN)python setup.py test
setup:
	$(PYTHON_BIN)python setup.py install $(SETUP_FLAG)
#clean_pyc:
#	@echo "Cleaning pyc files.."
#	find . -name '*.pyc' -delete
#	find . -name '*.pyo' -delete
#	find . -name '*~' -delete
#clean_build:
#	@echo "Cleaning build directories.."
#	rm --force --recursive build/
#	rm --force --recursive dist/
#	rm --force --recursive *.egg-info

.PHONY: help install clean delete_venv delete_conda_env create_venv create_conda_env setup run_tests