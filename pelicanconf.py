#!/usr/bin/env python
# -*- coding: utf-8 -*- #
PATH = 'content'
AUTHOR = u"Joshua L. Adelman"
SITENAME = u"Joshua Adelman"
SITEURL = ''

MODE = 'testing'

TIMEZONE = 'America/New_York'

DEFAULT_LANG='en'

ARTICLE_DIR = 'notes'
ARTICLE_URL = 'notes/{slug}/'
ARTICLE_SAVE_AS = 'notes/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DEFAULT_PAGINATION = False

TYPOGRIFY = True

THEME = 'site-theme'
DEFAULT_DATE_FORMAT = ('%d %b %Y')


BIBTEX_FILE = 'bibtex/publications.bib'
PROTIMGS = "['s-1.png','s-2.png','s-3.png']"
PLUGIN_PATH = 'my-plugins'
PLUGINS = ['my-plugins.bibtex']

STATIC_PATHS = ['pdfs']

GOOGLE_SCHOLAR = 'http://scholar.google.com/citations?user=Th4qmVMAAAAJ'
MENUITEMS = (
    ('About','/about'),
    ('Publications','/publications'),
    ('Research','/research'),
    ('Notes','/notes'),
)
