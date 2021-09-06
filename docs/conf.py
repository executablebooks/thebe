#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax',
              'sphinx_copybutton',
              'sphinx_js',
              'myst_parser']

# sphinx-js config
primary_domain = 'js'
js_source_path = '../src'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# Set the default role so we can use `foo` instead of ``foo``
default_role = 'literal'

# General information about the project.
project = u'Thebe'
copyright = u'%i, Executable Books Project' % date.today().year
author = u'Executable Books Project'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "node_modules"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "repository_url": "https://github.com/executablebooks/thebe",
    "use_issues_button": True,
    "use_repository_button": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "../examples"]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ThebeDoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ThebeDoc.tex', 'Thebe',
     'Chris Holdgraf', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Thebe', 'Thebe',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ThebeDoc', 'Thebe',
     author, 'ThebeDoc', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- Linkcheck options ------------------
linkcheck_anchors_ignore = ["/#!"]

# -- Build the latest JS for local preview -----------------------------
from subprocess import run, call
from pathlib import Path
import shutil as sh
import os

# -- Check for the yarn package manager ------------------------
path_root = Path(__file__).parent.parent
print(path_root)
local_yarn = Path("../node_modules/yarn/bin/yarn")
if not local_yarn.is_file():
    print("Local yarn not found, installing...")
    run(["npm","install","yarn"])
    run(["node_modules/yarn/bin/yarn", "--version"], cwd=path_root)
    print("yarn available!")

if not Path("_static/lib").exists():
    print("Couldn't find local `thebe` build for docs, building now...")
    run(["yarn", "install", "--frozen-lockfile"], cwd=path_root)
    run(["yarn", "build",], cwd=path_root)
    sh.copytree("../lib", "_static/lib")
    print("Finished building local `thebe` bundle.")
else:
    print("Found local `thebe` build, to update it, delete `_static/lib` and build docs")