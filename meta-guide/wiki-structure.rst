====================
Wiki Structure
====================

*How this documentation is organized and why*

----

Overview
========

This document explains how the Comfort Commons wiki is structured, following best practices from the `Google Developer Documentation Style Guide <https://developers.google.com/style/documentation-structure>`_. Our goal is to help everyone—from first-time contributors to experienced developers—find what they need quickly.

**Core principles:**

- Information organized by user task, not by internal project structure
- No redundancy—each concept explained once, linked elsewhere
- Clear pathways for different contributor types
- Progressive disclosure—basic info first, details available when needed

----

Documentation Architecture
===========================

Information Types
-----------------

Following the `Diátaxis framework <https://diataxis.fr/>`_ (also recommended by Google), we organize content into four types:

**Tutorials (Learning-Oriented)**
   Guide newcomers through their first complete experience. Example: "Your First Contribution"
   
   - Goal: Help someone succeed at doing something for the first time
   - Structure: Step-by-step, encouraging, assumes no prior knowledge
   - Location: Top-level, discoverable from home page

**How-To Guides (Task-Oriented)**
   Solve specific problems for people with some context. Example: "How to Set Up SSH Keys"
   
   - Goal: Help someone accomplish a specific task
   - Structure: Direct steps, assume some familiarity
   - Location: Grouped by topic area (code, research, design, etc.)

**Explanations (Understanding-Oriented)**
   Provide background and deepen understanding. Example: "Why We Use Person-First Language"
   
   - Goal: Help someone understand concepts and choices
   - Structure: Thoughtful discussion with examples
   - Location: Integrated with relevant how-to docs, ethics section

**Reference (Information-Oriented)**
   Provide complete, accurate technical details. Example: "Glossary," "API Documentation"
   
   - Goal: Help someone look up specific information
   - Structure: Comprehensive, well-organized, searchable
   - Location: Separate reference section

User Journey Pathways
----------------------

Rather than organizing by project components, we organize by **what people want to do**:

**First-Time Visitors**
   Path: Home → Getting Started → Pick pathway (research/code/design/docs)
   
**Researchers**
   Path: Research Hub → Ethics Guidelines → Social Media Ethics → How-To Research

**Developers**
   Path: Technical Setup → Code How-To → Contributing Guidelines → Repository

**Designers**
   Path: Getting Started → Try CM-Colors → Design Discussions → Feedback

**Documentation Writers**
   Path: Style Guide → Wiki Structure → How to Contribute Docs

----

Current Structure
=================

Top Level
---------

.. code-block:: text

    docs/
    ├── index.rst                  # Home page (warm welcome, overview)
    ├── getting-started.rst        # Universal starting point
    ├── accessibility-basics.rst   # For people new to accessibility
    ├── style-guide.rst            # For contributors (you are here)
    ├── wiki-structure.rst         # How docs are organized (this file)
    ├── glossary.rst               # Terminology reference
    └── tech-setup.rst             # Development environment setup

**Purpose of Top Level:**

- Welcoming entry point (index)
- Universal orientation (getting-started)
- Foundation concepts everyone needs (accessibility-basics)
- Contributor guides (style-guide, wiki-structure)
- Reference materials (glossary)

Research Documentation
----------------------

.. code-block:: text

    docs/research/
    ├── intro.rst                  # Research hub overview
    ├── research-ethics.rst        # Core ethics guidelines
    ├── social-media-ethics.rst    # Specific to social media research
    └── how-to-research.rst        # Practical research guide

**Organization principle:** Start with the hub (intro), understand ethics, then do the work.

Community Documentation
-----------------------

.. code-block:: text

    docs/who-we-are/
    ├── index.rst                  # About the community
    ├── our-values.rst             # What drives us
    ├── our-culture.rst            # How we work together
    └── the-team.rst               # Who's building this

**Organization principle:** Personal connection—who we are before what we've done.

Code Documentation
------------------

.. code-block:: text

    docs/code/
    ├── code-how-to.rst            # Contribution guide
    ├── architecture.rst           # System design (future)
    └── api-reference.rst          # Technical reference (future)

**Organization principle:** How-to first, technical details for those who need them.

----

Key Structural Principles
=========================

No Redundancy
-------------

**Each concept gets one canonical location:**

- **Good:** Define "person-first language" fully in style-guide.rst, link to it from elsewhere
- **Bad:** Copy the definition into multiple documents

**When to repeat information:**

- Critical safety information (ethics)
- Different user contexts need different framing (beginner vs. advanced)
- Summary/overview vs. detailed explanation

**How to handle it:**

- Use internal links: ``:doc:`style guide <style-guide>```
- Use term references: ``:term:`WCAG```
- Extract to reference docs if used in many places

Progressive Disclosure
----------------------

**Start simple, add complexity as needed:**

**Level 1: Overview**
   What it is, why it matters, who needs it
   
   Example: "CM-Colors makes your color palettes accessible"

**Level 2: Getting Started**
   Basic usage, common scenarios
   
   Example: "Install CM-Colors with pip install cm-colors"

**Level 3: How-To**
   Specific tasks and solutions
   
   Example: "How to configure CM-Colors for your CSS framework"

**Level 4: Deep Dive**
   Technical details, edge cases, theory
   
   Example: "How CM-Colors calculates perceptual contrast"

**Level 5: Reference**
   Complete API, all parameters, all options
   
   Example: "CM-Colors API Reference"

Put each level in appropriate documents. Link forward ("learn more about...") and backward ("if you haven't yet...").

Task-Oriented Organization
---------------------------

**Organize by what users want to do, not by system components:**

**Instead of:**

.. code-block:: text

    /colors/
    /contrast/
    /wcag/
    /testing/

**Do:**

.. code-block:: text

    /making-colors-accessible/
    /testing-your-color-scheme/
    /understanding-wcag-requirements/

**Benefits:**

- Users search by task ("how do I make colors accessible?")
- Reduces need for users to understand internal structure
- Easier to find information without knowing jargon

Scannable Content
-----------------

**Make information easy to find without reading everything:**

- Use descriptive headings that answer questions
- Put most important information first
- Use lists for multiple items
- Use tables for comparative information
- Add "TL;DR" or "Quick start" sections where helpful
- Include a table of contents for longer pages

**Good heading progression:**

.. code-block:: rst

    How to Contribute Documentation
    ================================
    
    Quick Start
    -----------
    
    Before You Start
    ----------------
    
    Writing Your First Doc
    ----------------------
    
    Getting Feedback
    ----------------

----

Best Practices
==============

Home Page
---------

**Purpose:** Welcome, orient, and route people to what they need.

**What to include:**

- Brief, warm welcome establishing tone
- Clear value proposition (what we do and why)
- Multiple entry points for different user types
- Current projects/status to show activity
- How to get help

**What not to include:**

- Detailed how-to instructions (link to them)
- Complete project history (link to about page)
- Every possible thing someone might need (prioritize)

Getting Started Pages
---------------------

**Purpose:** Give newcomers their first successful experience.

**What to include:**

- One clear goal they'll accomplish
- Prerequisites explicitly stated
- Step-by-step instructions
- Expected outcome/how to verify success
- Troubleshooting common issues
- Next steps/where to go from here

**What not to include:**

- Multiple paths (create separate guides instead)
- Advanced options (progressive disclosure)
- Tangential information (link to it)

How-To Guides
-------------

**Purpose:** Help someone solve a specific problem.

**Structure:**

1. Problem statement (what this solves)
2. Prerequisites (what you need first)
3. Solution (numbered steps)
4. Explanation (why this works)
5. Alternatives (other approaches, optional)
6. Related guides (links)

**Characteristics:**

- Task-focused title ("How to X")
- Assumes some familiarity
- Direct, imperative voice
- Code examples with context
- Links to deeper explanations

Reference Documentation
-----------------------

**Purpose:** Provide complete, accurate information for lookup.

**Characteristics:**

- Comprehensive (cover everything)
- Consistent structure for all items
- Alphabetical or logical ordering
- Minimal explanation (link to explanations)
- Searchable
- Examples of actual usage

**Examples:**

- Glossary of terms
- API reference
- Configuration options
- Command-line reference

----

Adding New Documentation
========================

Before Creating a New Page
---------------------------

Ask yourself:

1. **Does this already exist?**
   Search existing docs. Maybe it just needs updating.

2. **Where do users look for this?**
   What task or question leads them here?

3. **What type of documentation is this?**
   Tutorial, how-to, explanation, or reference?

4. **Who is the audience?**
   Complete beginners, intermediate, or advanced users?

5. **Can this be added to existing content?**
   Sometimes a section on an existing page is better than a new page.

Choosing a Location
-------------------

**Decision tree:**

Is it a tutorial for complete newcomers?
   → Top level (near getting-started.rst)

Is it task-oriented how-to content?
   → Grouped by topic (/research/, /code/, /design/)

Is it deep background or explanation?
   → With related how-to docs, or separate /explanations/ section

Is it reference material?
   → /reference/ directory or top-level if widely referenced (glossary)

Is it about the community itself?
   → /who-we-are/

Creating the Structure
----------------------

1. **Create an outline first**
   
   Use headings to structure before writing::

       ================
       Page Title
       ================
       
       Overview
       =========
       
       Section One
       ===========
       
       Subsection
       ----------

2. **Write the introduction**
   
   Answer: What is this? Why does it matter? Who needs it?

3. **Fill in the content**
   
   Follow appropriate structure for the doc type.

4. **Add navigation**
   
   Update the toctree in the parent index.rst::

       .. toctree::
          :maxdepth: 2
          
          existing-page
          your-new-page

5. **Link from related pages**
   
   Add contextual links from anywhere users might look for this.

6. **Test the flow**
   
   Build the docs, click through as a user would.

Naming Files and Pages
----------------------

**File names:**

- lowercase with hyphens: ``getting-started.rst``
- descriptive of content: ``research-ethics.rst`` not ``ethics.rst``
- not too long: ``code-how-to.rst`` not ``how-to-contribute-code-to-comfort-commons.rst``

**Page titles:**

- Clear and descriptive
- Often match navigation label
- Sometimes can be more creative on the page than in the URL

----

Maintaining the Wiki
====================

Regular Reviews
---------------

**Quarterly checks:**

- Are pathways still clear?
- Have we introduced redundancy?
- Do examples still work?
- Are external links still valid?
- Is anything outdated?

**When adding major features:**

- Update getting-started if it affects newcomers
- Update relevant how-to guides
- Add to glossary if new terms introduced
- Check if structure still serves users

**After contributor feedback:**

- If multiple people can't find something, restructure
- If something is confusing, rewrite or reorganize
- If links are broken, fix and prevent recurrence

Deprecating Content
-------------------

**When to remove:**

- Feature no longer exists
- Information is dangerously outdated
- Content has been consolidated elsewhere

**How to deprecate:**

1. Add a note at the top pointing to replacement
2. Update all incoming links
3. Keep the old page for a transition period
4. Eventually replace with a redirect or stub

**Never:**

- Silently delete without redirects
- Remove content others link to without notice

Quality Standards
-----------------

All documentation should:

- Follow the :doc:`style-guide`
- Use person-first language
- Include working examples
- Link to related content
- Be tested (run commands, click links)
- Be accessible (alt text, descriptive links)

----

Getting Help
============

**Not sure where something belongs?**
   Ask in a GitHub issue tagged "documentation." We'll figure it out together.

**Want to restructure something?**
   Propose it first. Major changes affect everyone.

**Found something in the wrong place?**
   Create an issue or fix it and explain why in the pull request.

**This structure doesn't solve your use case?**
   Help us improve it. What would work better?

----

*Good structure is invisible when it works. Users find what they need without thinking about organization. That's what we're building.*
