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
    'sphinx_autodoc_typehints',  # optional, if you want type hints rendered nicely
]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']






# Optionally, set autodoc options:
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'show-inheritance': True,
}

# Use a theme (like the Read the Docs theme)
html_theme = 'sphinx_rtd_theme'
