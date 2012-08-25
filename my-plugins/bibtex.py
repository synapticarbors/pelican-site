from pelican import signals

from collections import namedtuple
import itertools

class BibtexParser():
    def __init__(self, generator):
        print('Initializing BibtexParser')
        try:
            from pybtex.database.input import bibtex

            self.parser = bibtex.Parser()
            self.bibtex_file = generator.settings['BIBTEX_FILE']

        except ImportError:
            raise Exception("Unable to load pybtex module")

    def fetch(self):
        """
            returns a list of namedtuples containing publication data
        """
        data = self.parser.parse_file(self.bibtex_file)
        
        bibdata = []

        # Coerce data into a more reasonable data structure
        fields = ['title', 'journal', 'doi', 'volume', 'year', 'pages', 'abstract', 'number','authors','shared','pmid']  
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
                else:
                    middle = ''

                pieces = [author.first(), middle, author.prelast(), author.last(), author.lineage()] 
                name = ' '.join(list(itertools.chain.from_iterable(pieces)))
                if '&#xFE61' in name:
                    pfields['shared'] = True

                auth_list.append(name)

            pfields['authors'] = auth_list

            bibdata.append(pub(**pfields))

        return bibdata


def bibtex_parser_initialization(generator):
    """
        Initialization of parser
    """
    generator.plugin_instance = BibtexParser(generator)

def bibtex_fetch_publications(generator, metadata):
    if 'BIBTEX_FILE' in generator.settings.keys():
        generator.context['bibtex_entries'] = generator.plugin_instance.fetch()

def register():
    """
        Plugin registration
    """
    signals.pages_generator_init.connect(bibtex_parser_initialization)
    signals.pages_generate_context.connect(bibtex_fetch_publications)
