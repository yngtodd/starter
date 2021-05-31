"""Top-level package for Starter."""

from starter.fancy_logger import ColorizedLogger
from starter.timing_tools import timeit
from starter.profiling_funcs import profileit
from starter.configuration import Configuration, validate_json_schema
from starter.cloudstore import DropboxCloudstore

__author__ = "drkostas"
__email__ = "georgiou.kostas94@gmail.com"
__version__ = "0.1.0"
