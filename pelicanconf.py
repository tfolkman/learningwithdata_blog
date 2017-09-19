#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tyler Folkman'
SITENAME = u'Learning With Data'
SITEURL = 'http://learningwithdata.com'
SITETITLE = AUTHOR
SITESUBTITLE = 'Data Scientist @Ancestry'
SITELOGO = '/images/profile.jpg'
FAVICON = '/images/favicon.ico'
THEME = '/media/tyler/slowdata/git_projects/pelican-themes'
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

ROBOTS = 'index, follow'

PATH = 'content'

TIMEZONE = 'MST'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

MENUITEMS =  (('Categories', '/categories.html'),
	     ('Tags', '/tags.html'),)

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/')

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/tylerfolkman'),
          ('github', 'https://github.com/tfolkman'),
          ('envelope-o', 'mailto:learningwithdata@gmail.com'),
          ('twitter', 'https://twitter.com/tyler_folkman'),
          ('rss', 'feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
