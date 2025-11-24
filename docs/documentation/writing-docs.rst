======================
Writing Documentation
======================

*How to write docs that people actually read*

----

This guide covers the mechanics of writing documentation for Comfort Commons projects.

The Process
===========

1. **Identify the Audience**
   Who are you writing for? A beginner? An expert? A designer?

2. **Choose the Type**
   Is it a tutorial, a how-to, an explanation, or a reference? (See :doc:`/meta-guide/wiki-structure`)

3. **Drafting**
   * Use plain language.
   * Keep sentences short.
   * Use active voice.

4. **Review**
   * Check against the :doc:`/meta-guide/style-guide`.
   * Build the docs locally to check formatting.

Building Docs Locally
=====================

To see your changes before you push::

    # Activate your venv
    source venv/bin/activate

    # Install docs dependencies
    pip install -r docs/requirements.txt

    # Build HTML
    sphinx-build -b html . _build/html

    # Open _build/html/index.html in your browser

Common RST Patterns
===================

**Links**
   ``:doc:`Page Title <filename>``` for internal docs.
   ```Link Text <URL>`_`` for external links.

**Code Blocks**
   Use double colons ``::`` or ``.. code-block:: language``.

**Notes**
   ``.. note::`` for helpful tips.

----

*Clear writing is clear thinking.*
