"""swissbias demo"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("swissbias-gw")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Guillaume Witz"
__email__ = "guillaume.witz@unibe.ch"
