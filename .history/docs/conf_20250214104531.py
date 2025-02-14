import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'GeoJax'
copyright = '2025, Nik Drummond'
author = 'Nik Drummond'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',  
]



templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'show-inheritance': True,
}
