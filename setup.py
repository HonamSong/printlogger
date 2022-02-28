import setuptools
import os
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

about = {}

pkg_path = 'printlogger'

print(here)
print(os.path.join(here, pkg_path, '__version__.py'))

with open(os.path.join(here, pkg_path, '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    license=about['__license__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    keywords=['print', 'logging', 'color print'],
    long_description=readme,
    long_description_content_type='text/markdown',
    python_requires=">=3.7",
    url=about['__url__'],
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt').read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    #entry_points=dict(
    #    console_scripts=[
    #        'icon_getinfo=icon_getinfo.icon_getinfo_cli:main'
    #    ],
    #),
)

