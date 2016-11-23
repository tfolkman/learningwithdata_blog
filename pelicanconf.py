#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tyler Folkman'
SITENAME = u'Learning With Data'
SITEURL = ''
SITETITLE = AUTHOR
SITESUBTITLE = 'Data Scientist @Ancestry'
SITELOGO = '/images/profile.jpg'
FAVICON = '/images/favicon.ico'
THEME = 'Flex'
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

PATH = 'content'

TIMEZONE = 'MST'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/')

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/tylerfolkman'),
          ('github', 'https://github.com/tfolkman'),
          ('envelope-o', 'mailto:learningwithdata@gmail.com'),
          ('twitter', 'https://twitter.com/tyler_folkman'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
