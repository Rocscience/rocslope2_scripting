# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime

directory_path = os.path.abspath(os.path.join("..", "src"))
sys.path.insert(0, directory_path)

# -- Project information -----------------------------------------------------

project = "RocSlope2 Scripting Reference Manual"
copyright = f"{datetime.now().year}, Rocscience Inc."
author = "Rocscience Inc."

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
    "sphinx.ext.napoleon",
]

autodoc_default_options = {
    "member-order": "bysource",
}

napoleon_google_docstring = True
napoleon_use_param = True
napoleon_use_ivar = True

exclude_patterns = [
    "_build",
    "generatedAPIDocFiles/modules.rst",
]

autodoc_mock_imports = [
    "grpc",
    "google",
    "google.protobuf",
    "pandas",
    "rocslope2.generatedPythonFiles",
]

# -- Options for LaTeX output -------------------------------------------------

latex_elements = {
    "papersize": "letterpaper",
    "pointsize": "10pt",
    "preamble": "",
    "figure_align": "htbp",
}

html_logo = "_static/rocscience-logo-primary.png"
html_favicon = "_static/rocscience_favicon.png"
html_theme = "pydata_sphinx_theme"
add_module_names = False
