# Makefile for the starter module

SHELL=/bin/bash
PYTHON_VERSION=3.8

# You can use either venv (virtualenv) or conda env by specifying the correct argument (server=<prod, circleci, local>)
ifeq ($(server),prod)
	# Use Conda
	BASE=~/anaconda3/envs/starter
	BIN=$(BASE)/bin
	CLEAN_COMMAND="conda env remove -p $(BASE)"
	CREATE_COMMAND="conda create --prefix $(BASE) python=$(PYTHON_VERSION) -y"
	SETUP_FLAG=
	DEBUG=False
else ifeq ($(server),circleci)
	# Use Venv
	BASE=venv
	BIN=$(BASE)/bin
	CLEAN_COMMAND="rm -rf $(BASE)"
	CREATE_COMMAND="python$(PYTHON_VERSION) -m venv $(BASE)"
	SETUP_FLAG=
	DEBUG=True
else ifeq ($(server),local)
	# Use Conda
	BASE=~/anaconda3/envs/starter
	BIN=$(BASE)/bin
	CLEAN_COMMAND="conda env remove -p $(BASE)"
	CREATE_COMMAND="conda create --prefix $(BASE) python=$(PYTHON_VERSION) -y"
#	SETUP_FLAG='--local' # If you want to use this, you change it in setup.py too
	DEBUG=True
else
	# Use Conda
	BASE=~/anaconda3/envs/starter
	BIN=$(BASE)/bin
	CLEAN_COMMAND="conda env remove -p $(BASE)"
	CREATE_COMMAND="conda create --prefix $(BASE) python=$(PYTHON_VERSION) -y"
#	SETUP_FLAG='--local' # If you want to use this, you change it in setup.py too
	DEBUG=True
endif


all:
	$(MAKE) help
help:
	@echo
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo "                                              DISPLAYING HELP                                              "
	@echo "-----------------------------------------------------------------------------------------------------------"
	@echo "Use make [server=<prod|circleci|local>] <make recipe> to specify the server"
	@echo "Prod, and local are using conda env, circleci uses virtualenv. Default: local"
	@echo
	@echo "make help"
	@echo "       Display this message"
	@echo "make [server=<prod|circleci|local>] install"
	@echo "       Call clean delete_conda_env create_conda_env setup run_tests"
	@echo "make [server=<prod|circleci|local>] clean"
	@echo "       Delete all './build ./dist ./*.pyc ./*.tgz ./*.egg-info' files"
	@echo "make [server=<prod|circleci|local>] delete_env"
	@echo "       Delete the current conda env or virtualenv"
	@echo "make [server=<prod|circleci|local>] create_env"
	@echo "       Create a new conda env or virtualenv for the specified python version"
	@echo "make [server=<prod|circleci|local>] setup"
	@echo "       Call setup.py install"
	@echo "make [server=<prod|circleci|local>] run_tests"
	@echo "       Run all the tests from the specified folder"
	@echo "-----------------------------------------------------------------------------------------------------------"
install:
	$(MAKE) clean
	$(MAKE) delete_env
	$(MAKE) create_env
	$(MAKE) setup
	$(MAKE) run_tests
	@echo "Installation Successful!"
clean:
	$(PYTHON_BIN)python setup.py clean
delete_env:
	@echo "Deleting virtual environment.."
	eval $(DELETE_COMMAND)
create_env:
	@echo "Creating virtual environment.."
	eval $(CREATE_COMMAND)
run_tests:
	$(BIN)/python setup.py test $(SETUP_FLAG)
setup:
	$(BIN)/python setup.py install $(SETUP_FLAG)


.PHONY: help install clean delete_env create_env setup run_tests