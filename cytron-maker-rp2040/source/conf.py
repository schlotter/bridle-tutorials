# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import git
import semver
import sphinx
from datetime import date


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# sys.path.insert(0, os.path.abspath('.'))

logcfg = sphinx.util.logging.getLogger(__name__)
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
on_windows = sys.platform.startswith('win')

if 'DOCSRC' not in os.environ:
    DOCSRC = os.path.abspath(os.getcwd())
else:
    DOCSRC = os.path.abspath(os.environ['DOCSRC'])

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

docstat = 'preliminary'
docnumb = 'MPNX-TST-240119'
doctype = 'Tutorial'
category = 'Learning'
project = 'Cytron Maker RP2040 Tutorials'
publisher = 'UL Method Park GmbH and Navimatix GmbH'
author = 'TiaC Systems Team'
contactaddr = 'Jena / Erlangen, Germany'
contactemail = 'info@tiac-systems.net'
contactweb = 'https://tiac-systems.net/'
copyright = f'2019‒{date.today().year}, ' + publisher + ' and individual contributors'
about = category + ' – ' + project + '.'
keywords: str = docnumb
keywords += ',' + doctype
keywords += ',' + category
keywords += ',' + project
keywords += ',Zephyr'
keywords += ',Bridle'
keywords += ',Cytron'

# Define basic strings that will be used in the dictionary of external sites.
# gxp/GXP stands for GitX (Hub/Lab) Pages
gxp_base = 'https://github.com/tiacsys/bridle-tutorials'
gxp_slug = 'bridle-tutorials'
gxp_name = publisher + ', ' + doctype + ', ' + project

if on_rtd:
    git_describe = ('--dirty=+RTDS', '--broken=+broken')
else:
    git_describe = ('--dirty=+dirty', '--broken=+broken')

try:
    repo = git.Repo(search_parent_directories=True)
    semv = semver.VersionInfo.parse(repo.git.describe(git_describe))
    sha1 = repo.head.object.hexsha.lower()
except:
    # fallback to unknown version / release
    semv = semver.VersionInfo.parse('0.0.0-invalid+unknown')
    sha1 = '0000000000000000000000000000000000000000'

# The short SHA1 for identification
identify = repo.git.rev_parse(sha1, short=8)

# The short X.Y.Z version
version = str(semv.finalize_version())
genvers = str(semv.major)

# The full version, including alpha/beta/rc tags
release = str(semv)

# Combined document title and subtitle
# title = project + ' ' + version
title = project
subtitle = doctype

# Single target file names
basename: str = 'bridle-tutorial'
namespace: str = 'net.tiac-systems.doc.learning.tutorial.cytron-maker-rp2040.'
namespace += version + '.'

logcfg.info(project + ' ' + release, color='yellow')

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

build_sphinx = sphinx.__version__

needs_sphinx = '7.1.2'
needs_extensions = {
    'sphinx.ext.extlinks':          needs_sphinx,
    'sphinx.ext.ifconfig':          needs_sphinx,
    'sphinx.ext.intersphinx':       needs_sphinx,
    'sphinx.ext.todo':              needs_sphinx,
#   'sphinx_immaterial':            '0.11.10',
}

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_immaterial',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'de'

rst_prolog = '''
.. |docsrc| replace:: {docsrc}
.. |docstat| replace:: {docstat}
.. |docnumb| replace:: {docnumb}
.. |genvers| replace:: {genvers}
.. |identify| replace:: {identify}
.. |title| replace:: {title}
.. |subtitle| replace:: {subtitle}
.. |publisher| replace:: {publisher}
.. |copyright| replace:: {copyright}
.. |project| replace:: {project}
.. |author| replace:: {author}
.. |about| replace:: {about}
.. |contactaddr| replace:: {contactaddr}
.. |contactemail| replace:: {contactemail}
.. |contactweb| replace:: {contactweb}
.. |gxp_name| replace:: {gxp_name}
.. |gxp_name_e| replace:: :emphasis:`{gxp_name}`
.. |gxp_name_s| replace:: :strong:`{gxp_name}`
.. meta::
   :keywords: {keywords}
'''.format(
    docsrc = DOCSRC,
    docstat = docstat,
    docnumb = docnumb,
    genvers = genvers,
    version = version,
    identify = identify,
    release = release,
    title = title,
    subtitle = subtitle,
    copyright = copyright,
    project = project,
    author = author,
    about = about,
    contactaddr = contactaddr,
    contactemail = contactemail,
    contactweb = contactweb,
    publisher = publisher,
    subject = about,
    keywords = keywords,
    gxp_name = gxp_name,
)

# -- Options for PDF output --------------------------------------------------
# https://www.mos6581.org/rinohtype/master/quickstart.html#sphinx-quickstart

rinoh_documents = [
    dict(doc = 'index', target = basename,
         title = project, author = author,
         template = '_styles/rinohtype/bridle.rtt',
         logo = '_static/images/bridle_text.pdf',
    ),
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = project
html_favicon = '_static/images/bridle.ico'
html_logo = '_static/images/bridle.svg'

html_theme = 'sphinx_immaterial'
html_static_path = ['_static']
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "repo_url": "https://github.com/tiacsys/bridle-tutorials/",
    "repo_name": "TiaCSys/Bridle-Tutorials",
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "indigo",
            "accent": "amber",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "In den dunklen Modus wechseln",
                # "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "indigo",
            "accent": "amber",
            "toggle": {
                "icon": "material/weather-night",
                "name": "In den hellen Modus wechseln",
                # "name": "Switch to light mode",
            },
        },
    ],
}

# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True