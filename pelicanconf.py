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

ARTICLE_URL = 'recipies/{slug}/'
ARTICLE_SAVE_AS = 'recipies/{slug}/index.html'

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'

CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
CATEGORYS_URL = 'categories/'
CATEGORYS_SAVE_AS = 'categories/index.html'

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'CNAME',
    'images'
]

DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'archives']

SUMMARY_MAX_LENGTH = 15

DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 3

PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
    (-1, '{base_name}/last/', '{base_name}/last/index.html'),
)
