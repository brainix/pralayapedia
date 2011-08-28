#-----------------------------------------------------------------------------#
#   config.py                                                                 #
#                                                                             #
#   Copyright (c) 2011, Robert Boustany, original author.                     #
#                                                                             #
#       This file is part of Pralayapedia.                                    #
#                                                                             #
#       Pralayapedia is free software; you can redistribute it and/or modify  #
#       it under the terms of the GNU General Public License as published by  #
#       the Free Software Foundation, either version 3 of the License, or (at #
#       your option) any later version.                                       #
#                                                                             #
#       Pralayapedia is distributed in the hope that it will be useful, but   #
#       WITHOUT ANY WARRANTY; without even the implied warranty of            #
#       or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public      #
#       License for more details.                                             #
#                                                                             #
#       You should have received a copy of the GNU General Public License     #
#       along with Pralayapedia.  If not, see:                                #
#           <http://www.gnu.org/licenses/>.                                   #
#-----------------------------------------------------------------------------#


import os

from setuptools import setup, find_packages


def read_file(*path_components):
    path = os.path.join(os.path.dirname(__file__), *path_components)
    f = open(path)
    contents = f.read()
    contents = contents.strip()
    f.close()
    return contents


version = read_file('pralaya', 'plone', 'version.txt')


setup(
    name='pralaya.plone',
    version=version,
    description='Custom Pralaya yoga Plone product.',
    long_description=open('README.txt').read() + '\n' +
                     open(os.path.join('docs', 'HISTORY.txt')).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        'Programming Language :: Python',
    ],
    keywords='',
    author='',
    author_email='',
    url='http://svn.plone.org/svn/collective/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['pralaya'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
        # -*- Entry points: -*-
    """,
)
