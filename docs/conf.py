
import sys
import os

extensions = [
    'sphinx.ext.todo',
]

source_suffix = '.txt'

master_doc = 'index'

### part to update ###################################
project = u'domogik-plugin-mirror'
copyright = u'2016, Tikismoke'
version = '0.2'
release = version
######################################################

pygments_style = 'sphinx'

html_theme = 'default'
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'domogik-plugin-mirror'