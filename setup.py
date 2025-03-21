from setuptools import setup
from os         import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name             = 'neovim-remote',
    author           = 'Marco Hinz',
    author_email     = 'mh.codebro@gmail.com',
    url              = 'https://github.com/mhinz/neovim-remote',
    description      = 'Control nvim processes using "nvr" commandline tool',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    python_requires  = '>=3.7',
    install_requires = ['pynvim', 'psutil', 'setuptools'],
    entry_points     = {
        'console_scripts': ['nvr = nvr.nvr:main']
    },
    packages         = ['nvr'],
    version          = '2.5.0',
    license          = 'MIT',
    keywords         = 'neovim nvim nvr remote helper',
    classifiers      = [
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
)

