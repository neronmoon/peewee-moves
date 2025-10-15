from setuptools import setup
from codecs import open
from os import path


from setuptools import setup
import pathlib, re

def read_version():
    text = pathlib.Path("peewee_moves.py").read_text(encoding="utf-8")
    m = re.search(r'^__version__\s*=\s*[\'"]([^\'"]+)[\'"]', text, re.M)
    if not m:
        raise RuntimeError("Cannot find __version__ in peewee_moves.py")
    return m.group(1)


root_dir = path.abspath(path.dirname(__file__))

with open(path.join(root_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(root_dir, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = list(map(str.strip, f.readlines()))


setup(
    name='peewee-moves',
    version=read_version(),

    description='Simple and flexible migration manager for Peewee ORM.',
    long_description=long_description,

    url='https://github.com/timster/peewee-moves',

    author='Tim Shaffer',
    author_email='timshaffer@me.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Database :: Front-Ends',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='peewee orm database migration development',

    py_modules=['peewee_moves'],

    entry_points={
        'flask.commands': [
            'db = peewee_moves:flask_command',
        ],
        'console_scripts': [
            'peewee-db = peewee_moves:cli_command'
        ],
    },

    install_requires=install_requires,
)
