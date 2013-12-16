from setuptools import setup, find_packages
import os

version = '0.1' 

setup(name='medialog.aktivitetshuset',
      version=version,
      description="For aktivitetshuset 5.",
      long_description=open("README").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone zope aktivitetshuset',
      author='Grieg Medialog [Espen Moe-Nilssen]',
      author_email='espen@medialog.no',
      url='http://products.medialog.no',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'archetypes.schemaextender',
          'plone.directives.form',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
