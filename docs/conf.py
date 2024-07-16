#
# Python Soft IOC documentation build configuration file, created by
# sphinx-quickstart on Fri May 14 13:06:33 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import softioc

# General information about the project.
project = u'pythonSoftIOC'
copyright = u'2008, Diamond Light Source'
author = 'Michael Abbott'

# The full version, including alpha/beta/rc tags.
release = softioc.__version__

# The short X.Y version.
if '+' in release:
    # Not on a tag
    version = 'master'
else:
    version = release

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    # Use this for generating API docs
    'sphinx.ext.autodoc',
    # This can parse google style docstrings
    'sphinx.ext.napoleon',
    # For linking to external sphinx documentation
    'sphinx.ext.intersphinx',
    # Add links to source code in API docs
    'sphinx.ext.viewcode',
]

# If true, Sphinx will warn about all references where the target cannot
# be found.
nitpicky = True

# A list of (type, target) tuples (by default empty) that should be ignored when
# generating warnings in "nitpicky mode". Note that type should include the
# domain name if present. Example entries would be ('py:func', 'int') or
# ('envvar', 'LD_LIBRARY_PATH').
nitpick_ignore = [('py:func', 'int')]

# Both the class’ and the __init__ method’s docstring are concatenated and
# inserted into the main body of the autoclass directive
autoclass_content = 'both'

# Order the members by the order they appear in the source code
autodoc_member_order = 'bysource'

# Don't inherit docstrings from baseclasses
autodoc_inherit_docstrings = False

# The name of a reST role (builtin or Sphinx extension) to use as the default
# role, that is, for text marked up `like this`
default_role = 'any'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# This means you can link things like `str` and `asyncio` to the relevant
# docs in the python documentation.
intersphinx_mapping = dict(
    python=('https://docs.python.org/3/', None),
    cothread=(
        "https://diamondlightsource.github.io/cothread/master/", None
    ),
    aioca=("https://DiamondLightSource.github.io/aioca/master/", None),
    epicsdbbuilder=(
        "https://DiamondLightSource.github.io/epicsdbbuilder/master/", None)
)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
try:
    import sphinx_rtd_theme_github_versions
    html_theme = 'sphinx_rtd_theme_github_versions'
except ImportError:
    html_theme = 'default'

# Options for the sphinx rtd theme, use DLS blue
html_theme_options = dict(style_nav_header_background='rgb(7, 43, 93)')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# Add some CSS classes for columns and other tweaks in a custom css file
html_css_files = ['theme_overrides.css']

# Logo
html_logo = 'images/softioc-logo.svg'
html_favicon = 'images/softioc-favicon.ico'

# Common links that should be available on every page
rst_epilog = """
.. _epicscorelibs: https://github.com/mdavidsaver/epicscorelibs
"""
