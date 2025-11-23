# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Comfort Commons'
copyright = '2025, Lalitha A R, & Contributors of Comfort Mode Toolkit'
author = 'Lalitha A R, & Contributors of Comfort Mode Toolkit'
# release = 'v0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'

extensions = [
    # 'myst_parser',  # For Markdown support
    'sphinx_design',
]



html_static_path = ['_static']
html_css_files = ['custom.css']
html_favicon = "_static/logo.png"



html_theme_options = {
    "repository_url": "https://github.com/comfort-mode-toolkit/wiki",
    "use_repository_button": True,
    "use_sidenotes": True,
}