# -*- coding: utf-8 -*-
"""Installer for the collective.examples.hud package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst')  # + \
#    read('docs', 'CHANGELOG.rst')

setup(
    name='collective.examples.hud',
    version='0.1',
    description="Plone Heads Up Display Panel Example",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
    ],
    keywords='Plone HUD Panel Example',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/collective/collective.examples.hud',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.examples'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Pillow',
        'Plone',
        'plone.api',
        #'plone.hud',
        'setuptools',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
        'develop': [
            'coverage',
            'flake8',
            'jarn.mkrelease',
            'niteoweb.loginas',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'Sphinx',
            'zest.releaser',
            'zptlint',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
