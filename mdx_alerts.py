#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import re
from markdown import Extension
from markdown.preprocessors import Preprocessor


class AlertBlockExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        '''
        Adds the AlertBlockExtension to Markdown
        '''
        md.registerExtension(self)
        md.preprocessors.add(
            'alerts',
            AlertBlockPreprocessor(md),
            "_end"
        )


class AlertBlockPreprocessor(Preprocessor):
    OPEN_RE = re.compile(
        r'^\s*'
            # REQUIRED: opening tag
            r'!alert!'
        r'\s*'
            # REQUIRED: the alert level
            r'(?P<level>[a-zA-Z]+)'
        r'\s*'
            # OPTIONAL: whether the alert is dismissable
            r'(?P<dismissable>dismissable)?'
        r'\s*'
            # OPTIONAL: the font-awesome icon to use
            r'(?P<icon>[_a-zA-Z0-9-]+|(noicon))?'
        r'\s*$',
        re.DOTALL,
    )
    CLOSE_RE = re.compile(
        r'^\s*!endalert!\s*$',
    )

    OPEN_HTML = '<div class="alert alert-{level} {dismissable}">'
    ICON_HTML = '<i class="fa fa-{icon}"></i>'
    CLOSE_BUTTON_HTML = '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>'
    CLOSE_HTML = '</div>'

    NO_ICON_FLAG = 'noicon'
    ICON_MAP = {
        'warning': 'warning',
        'info': 'info-circle',
        'success': 'check-circle',
        'danger': 'warning',
        'thoughts': 'commenting',
    }

    LEVEL_MAP = {
        # Note: alert-danger is used instead of alert-error
        #   Thus error is now an alias for the danger level
        'error': 'danger',
        'thoughts': 'info',
    }

    def __init__(self, md):
        super(AlertBlockPreprocessor, self).__init__(md)

        self.alert = False
        self.is_dismissable = False
        self.name = None
        self.has_icon = None
        self.icon = None
        self.level = None

    def run(self, lines):
        for index, line in enumerate(lines):
            # First we need to find and parse any opening tag
            # (but not if we already found an open tag)
            if not self.alert:
                match = AlertBlockPreprocessor.OPEN_RE.search(line)
                if match is not None:
                    # Mark that we found an alert
                    self.new_alert(match)

                    # replace the opening with the appropriate formatting
                    lines[index] = self.format_open()

            # We also look for any closing tags
            # (but only if we already found an open tag)
            elif self.alert:
                match = AlertBlockPreprocessor.CLOSE_RE.search(line)
                if match is not None:
                    # Mark that we've finished with the alert
                    self.end_alert(match)

                    # replace the closing with the appropriate formatting
                    lines[index] = self.format_closed()
                else:
                    # Allow alerts to have indented content.
                    if line.startswith(" " * 4):
                        lines[index] = lines[index][4:]

        return lines

    def new_alert(self, match):
        '''
        Marks that we've found an open tag, parsing data from it
        '''
        self.alert = True
        self.is_dismissable = match.group('dismissable') is not None

        self.name = match.group('level')

        # Now we figure out if the user wants an icon
        icon = match.group('icon')
        self.has_icon = True
        if icon is None:
            self.icon = AlertBlockPreprocessor.ICON_MAP[self.name]
        elif icon != AlertBlockPreprocessor.NO_ICON_FLAG:
            self.has_icon = False
        else:
            self.icon = icon

        # Map the level to the bootstrap class for the level
        self.level = match.group('level')
        self.level = AlertBlockPreprocessor.LEVEL_MAP.get(self.name, self.name)

    def end_alert(self, match):
        '''
        Marks that we've found a close tag, parsing data from it
        '''
        self.alert = None

    def format_open(self):
        '''
        Formats the replacement open tag html
        '''
        data = AlertBlockPreprocessor.OPEN_HTML.format(
            level=self.level,
            dismissable=('alert-dismissable' if self.is_dismissable else ''),
        )

        # Add the icon if asked
        if self.has_icon:
            data += AlertBlockPreprocessor.ICON_HTML.format(
                icon=self.icon,
            )

        # Add the closing button if the alert is dismissable
        if self.is_dismissable:
            data += AlertBlockPreprocessor.CLOSE_BUTTON_HTML

        return data

    def format_closed(self):
        '''
        Formats the replacement open tag html
        '''
        data = AlertBlockPreprocessor.CLOSE_HTML

        return data


def makeExtension(*args, **kwargs):
    return AlertBlockExtension(*args, **kwargs)
