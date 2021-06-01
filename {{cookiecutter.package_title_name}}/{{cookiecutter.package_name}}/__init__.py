"""Top-level package for {{cookiecutter.package_title_name}}."""

from {{cookiecutter.package_name}}.fancy_logger import ColorizedLogger
from {{cookiecutter.package_name}}.timing_tools import timeit
from {{cookiecutter.package_name}}.profiling_funcs import profileit
from {{cookiecutter.package_name}}.configuration import Configuration, validate_json_schema
from {{cookiecutter.package_name}}.cloudstore import DropboxCloudstore
from {{cookiecutter.package_name}}.datastore import MySqlDatastore

__author__ = "{{cookiecutter.author}}"
__email__ = "{{cookiecutter.author_email}}"
__version__ = "{{cookiecutter.package_version}}"
