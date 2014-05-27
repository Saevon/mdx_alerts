#!/usr/bin/python
# -*- coding: UTF-8 -*-

from setuptools import setup

setup(
    name = "mdx_alerts",
    version = "0.1.0",
    py_modules = ["mdx_alerts"],
    install_requires = ['Markdown>=2.2.0'],
    author = "Saevon",
    author_email = "dot.saevon@gmail.com",
    description = "Markdown alerts extension",
    license = "MIT",
    url = "https://github.com/saevon/markdown-alerts",
    keywords = "markdown twitter bootstrap alerts",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
)
