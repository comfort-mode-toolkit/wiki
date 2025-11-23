=======================
Technical Setup Guide
=======================

*Getting your machine ready for adventure*

----

This guide will help you set up your development environment for contributing to Comfort Commons projects.

Prerequisites
=============

You'll need the following installed on your machine:

* **Python 3.10 or higher**
* **Git**
* **A code editor** (VS Code is popular, but use what you love)

Step 1: Fork and Clone
======================

1. **Fork the repository** you want to work on (e.g., `cm-colors`) on GitHub.
2. **Clone your fork** to your local machine::

    git clone https://github.com/YOUR-USERNAME/cm-colors.git
    cd cm-colors

Step 2: Virtual Environment
===========================

Always work in a virtual environment to keep dependencies isolated.

1. **Create the environment**::

    python3 -m venv venv

2. **Activate it**::

    # On Windows
    venv\Scripts\activate

    # On macOS/Linux
    source venv/bin/activate

Step 3: Install Dependencies
============================

Install the project dependencies::

    pip install -r requirements.txt

If you're working on documentation (this repo), you'll also need::

    pip install -r docs/requirements.txt

Step 4: Verify Setup
====================

Run the tests to make sure everything is working::

    pytest

If the tests pass, you're ready to go!

----

Troubleshooting
===============

**"Command not found: python"**
   Try using ``python3`` instead.

**"Permission denied"**
   You might need to use ``sudo`` (on Linux/Mac) or run as Administrator (on Windows), but usually, this means permissions on your folder are wrong. Avoid using sudo for pip installs if possible.

**Still stuck?**
   Open an issue or ask in our discussions. We'll help you debug.
