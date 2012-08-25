from pybtex.database.input import bibtex
from collections import namedtuple
import itertools

def bibtex_parser(bibfile):

    bibdata = []
    
    parser = bibtex.Parser()
    data = parser.parse_file(bibfile)

    # Coerce data into a more reasonable data structure
    fields = ['title', 'journal', 'doi', 'volume', 'year', 'pages', 'abstract', 'number','authors','shared']  
    exclude_fields = ['authors','shared']
    pub = namedtuple('Publications',fields)

    for pkey in data.entries:
        p = data.entries[pkey]

        pfields = {f:p.fields[f] for f in fields if f not in exclude_fields} 
        pfields['shared'] = False

        # Reformat author list
        authors = p.persons['author']
        
        auth_list = []
        for author in authors:
            if len(author.middle()) > 0:
                middle = [author.middle()[0] + '.'] 

            pieces = [author.first(), middle, author.prelast(), author.last(), author.lineage()] 
            name = ' '.join(list(itertools.chain.from_iterable(pieces)))
            if '&#xFE61' in name:
                pfields['shared'] = True

            auth_list.append(name)

        pfields['authors'] = auth_list

        bibdata.append(pub(**pfields))

    return bibdata
        
