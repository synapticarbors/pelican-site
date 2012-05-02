# -*- coding: utf-8 -*-

from bibtex import bibtex_parser

data = bibtex_parser('../bibtex/publications.bib')

for d in data:
    x = d._asdict()
    print '\n'
    for key in x:
        print u'{}: {}'.format(key,x[key]).encode('utf-8')
