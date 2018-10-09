"""

This module abstracts templates for invoice providers.

Templates are initially read from .yml files and then kept as a class.

"""

import os
import yaml
import pkg_resources
from collections import OrderedDict
import logging as logger
from invtemplate import InvoiceTemplate 
import codecs
import chardet


logger.getLogger('chardet').setLevel(logger.WARNING)

"""
In terminal - 
import loader
stream = open('flip.yml', 'r')
from loader import ordered_load

z = ordered_load(stream)
"""


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
	"""
	Load mappings and ordered mappings.

	Loader to load mappings and ordered mappings intp python 2.7+ dict type.
	instead of the vanilla dict and the list of pair it currently uses.

	"""
	class OrderedLoader(Loader):
		pass

	def contruct_mapping(loader,node):
		loader.flatten_mapping(node)
		return object_pairs_hook(loader.construct_pairs(node))

	OrderedLoader.add_constructor(
		yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
		contruct_mapping)

	return yaml.load(stream, OrderedLoader)



def read_templates(folder=None):
	"""
	Load yaml templates from templates folder. Retunrs list of dics.

	use built in folder if no folder set.

	paramters:
	folder - str - user definder folder where they store their files, if none use builtin templates.

	Returns:
	Output: instance of "Invoice Templates". Template with match based on key words.

	After reading the template you can use the result as an instance of `InvoiceTemplate` to extract fields from
    `extract_data()`
    >>> my_template = InvoiceTemplate([('issuer', 'OYO'), ('fields', OrderedDict([('amount', 'GrandTotalRs(\\d+)'),
    ('date', 'Date:(\\d{1,2}\\/\\d{1,2}\\/\\d{1,4})'), ('invoice_number', '([A-Z0-9]+)CashatHotel')])),
    ('keywords', ['OYO', 'Oravel', 'Stays']), ('options', OrderedDict([('currency', 'INR'), ('decimal_separator', '.'),
    ('remove_whitespace', True)])), ('template_name', 'com.oyo.invoice.yml')])
    >>> extract_data("invoice2data/test/pdfs/oyo.pdf", my_template, pdftotext)
    {'issuer': 'OYO', 'amount': 1939.0, 'date': datetime.datetime(2017, 12, 31, 0, 0), 'invoice_number': 'IBZY2087',
     'currency': 'INR', 'desc': 'Invoice IBZY2087 from OYO'}

	"""

	output = []

	if folder is None:
		folder = pkg_resources.resource_filename(__name__, 'templates')

#pkg_resource.resource_filename - since the named resource is a directory
# all the files in the directory are extracted. Here pkg_res will be invoice2data

	for path, subdirs, files in os.walk(folder):
		for name in sorted(files):
			if name.endswith('.yml'):
				with codecs.open(os.path.join(path, name), encoding=chardet.detect(open(os.path.join(path, name), 'rb').read())['encoding']) as template_file:
					tpl = ordered_load(template_file.read())
				tpl['template_name'] = name

				#Test if all the required feilds are there in the template
				assert 'keywords' in tpl.keys(), 'Missing keywords field'

				#keywords as list
				if type(tpl['keywords']) is not list:
					tpl['keywords'] = [tpl['keywords']]
				output.append(InvoiceTemplate(tpl))
	return output
