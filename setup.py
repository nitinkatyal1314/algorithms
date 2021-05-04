import pathlib
from setuptools import setup, find_packages
import re

HERE = pathlib.Path(__file__).parent

# helper functions to make it easier to list dependencies not as a python list, but vertically w/
# optional built-in comments to why a certain version of the dependency is listed


def cleanup(x):
    return re.sub(r" *#.*", "", x.strip())  # comments


def to_list(buffer):
    return list(filter(None, map(cleanup, buffer.splitlines())))


DEPENDENCIES = {
    "core": to_list(
      """
        py-ds
      """
    )
}

VERSION = '0.1.0'
PACKAGE_NAME = 'pyalgo'
AUTHOR = 'Nitin Katyal'
AUTHOR_EMAIL = 'nitinkatyal1314@gmail.com'
URL = 'https://github.com/nitinkatyal1314/data-structures'

LICENSE = 'MIT License'
DESCRIPTION = 'Ready to use algorithms'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [y for x in DEPENDENCIES.values() for y in x]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      python_requires=">=3.6",
      include_package_data=True,
      zip_safe=False,
      packages=find_packages()
)