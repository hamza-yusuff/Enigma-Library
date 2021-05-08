
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '0.0.3'
PACKAGE_NAME = 'PyEnigmatic'
AUTHOR = 'Hamza Bin Yusuff'
AUTHOR_EMAIL = 'hbyusuff@uwaterloo.ca'
URL = 'https://github.com/hamza-yusuff'

LICENSE = 'MIT LICENSE'
DESCRIPTION = 'An enigmatic cryptographic library'
LONG_DESCRIPTION = long_description
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'cryptography',
      'pynacl',
      'pycryptodome'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      keywords=['python', 'enigma', 'cryptography', 'aes', 'rsa', 'caesar', 'vigenere', 'symmetric', 'assymetric', 'key', 'prime'],
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )