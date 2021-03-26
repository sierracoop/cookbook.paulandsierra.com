#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = "Cookbook"
SITEURL = ''

# THEME = 'cookbook.paulandsierra.com-theme'
THEME = "themes/cookbook"

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'CNAME',
    'images'
]
