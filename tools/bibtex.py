from pybtex.database.input import bibtex
from collections import namedtuple
import itertools

def bibtex_parser(bibfile):

    bibdata = []
    
    parser = bibtex.Parser()
    data = parser.parse_file(bibfile)

    # Coerce data into a more reasonable data structure
    fields = ['title', 'authors', 'journal', 'doi', 'volume', 'year', 'pages', 'abstract', 'number']  
    pub = namedtuple('Publications',fields)

    for pkey in data.entries:
        p = data.entries[pkey]

        pfields = {f:p.fields[f] for f in fields if f is not 'authors'}

        # Reformat author list
        authors = p.persons['author']
        auth_list = []
        for author in authors:
            if len(author.middle()) > 0:
                middle = [author.middle()[0] + '.'] 

            pieces = [author.first(), middle, author.prelast(), author.last(), author.lineage()] 
            name = list(itertools.chain.from_iterable(pieces))
            auth_list.append(' '.join(name))

        pfields['authors'] = auth_list

        bibdata.append(pub(**pfields))

    return bibdata
        
