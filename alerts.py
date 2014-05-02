#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from markdown import Extension
from markdown.preprocessors import Preprocessor
import re


class AlertBlockExtension(Extension):

    def extendMarkdown(self, markdown, markdown_globals):
        '''
        Adds the AlertBlockExtension to Markdown
        '''
        markdown.registerExtension(self)
        markdown.preprocessors.add(
            'alerts',
            AlertBlockPreprocessor(markdown),
            "_begin"
        )

class AlertBlockPreprocessor(Preprocessor):
    pass
    # def run(self, lines):
    #     pass


def makeExtension(configs=None):
    return AlertBlockExtension(configs=configs)
