# !/usr/bin/env python
import setuptools

setuptools.setup(
    name="molecule-glesys",
    author='Magnus Johansson',
    author_email='magnus@glesys.se',
    description='Molecule GleSYS Plugin :: run molecule tests in GleSYS Cloud',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/glesys/molecule-driver',
    package_dir={'': '.'},
    include_package_data=True,
    entry_points={
        'molecule.driver': [
            'glesys = molecule_glesys.driver:GleSYS',
        ],
    },

    packages=[
        'molecule_glesys',
        'molecule_glesys.cookiecutter',
    ],
    install_requires=[
        # molecule plugins are not allowed to mention Ansible as a direct dependency
        'PyYAML',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
