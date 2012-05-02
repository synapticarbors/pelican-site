#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Joshua L. Adelman"
SITENAME = u"Joshua Adelman"
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG='en'

ARTICLE_DIR = 'notes'
ARTICLE_URL = 'notes/{slug}/'
ARTICLE_SAVE_AS = 'notes/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DEFAULT_PAGINATION = False

TYPOGRIFY = True

from tools.bibtex import bibtex_parser
PUBLICATIONS = bibtex_parser('publications/publications.bib')
