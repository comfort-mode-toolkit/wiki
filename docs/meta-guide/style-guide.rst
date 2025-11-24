================
Style Guide
================

*How we write, what we say, and why it matters*

----

Overview
========

This style guide helps maintain consistency, clarity, and kindness across all Comfort Commons documentation. It's based on the `Google Developer Documentation Style Guide <https://developers.google.com/style>`_ with additional guidelines specific to our community values.

**Key principles:**

- Write for real people, not just developers
- Use clear, jargon-free language
- Respect everyone's humanity and dignity
- Make accessibility accessible

----

General Writing Guidelines
===========================

Voice and Tone
--------------

**Conversational but Clear**
   Write like you're talking to a friend who's smart but new to the topic. Use "we" and "you" freely. Contractions are fine. Be warm without being unprofessional.

   - **Good:** "We're researching how color affects people with vestibular challenges."
   - **Avoid:** "The research team is investigating the effects of chromatic stimuli on individuals presenting with vestibular symptomatology."

**Direct and Active**
   Use active voice. Start instructions with verbs. Tell people what to do, not what can be done.

   - **Good:** "Create a new file called custom.css"
   - **Avoid:** "A new file called custom.css should be created"

**Honest About Complexity**
   If something is hard, say so. If we don't know something yet, admit it. If something is easy, don't make it sound complicated.

   - **Good:** "This is tricky to get right. Take your time."
   - **Avoid:** "This straightforward procedure should pose no difficulties."

Structure and Organization
---------------------------

Follow these patterns from the Google style guide:

**Use Headings Hierarchically**
   H1 for page title, H2 for main sections, H3 for subsections. Don't skip levels.

**Start with the Goal**
   Tell people what they'll accomplish before explaining how. Put the most important information first.

**Use Lists for Multiple Items**
   - Use bulleted lists for unordered items
   - Use numbered lists for sequential steps
   - Use definition lists for terms and explanations

**Keep Paragraphs Focused**
   One main idea per paragraph. 3-5 sentences usually works. If it's longer, consider breaking it up or using a list.

----

Language and Word Choice
========================

Person-First Language
---------------------

**The Core Rule: People Are Not Their Conditions**

Never reduce someone to a medical condition, disability, or characteristic. Always use "people who..." or "people experiencing..." phrasing.

**Correct Examples:**

- "people who use screen readers"
- "people who experience vestibular challenges"
- "people who navigate by keyboard"
- "people with ADHD" (when the community prefers this phrasing)
- "people in the deaf community" (respecting community preference)

**Never Use:**

- "disabled users"
- "normal users" (implies others are abnormal)
- "the blind" (people are not their vision status)
- "vestibular patients" (we're not a medical practice)
- "wheelchair-bound" (wheelchairs provide freedom, not confinement)
- "suffering from" (unless someone specifically describes it that way)

**Important Notes:**

- Some disability communities prefer identity-first language (e.g., "autistic person" rather than "person with autism"). When you know the community preference, follow it.
- When in doubt, use person-first language and keep the person as the subject.
- Never use disability as a metaphor for something bad ("that's blind to the issue," "tone-deaf response").

Inclusive and Neutral Language
-------------------------------

**Avoid Assumptions**
   Don't assume everyone codes, reads English as a first language, uses a mouse, or sees color the same way.

   - **Good:** "Select the Submit button"
   - **Avoid:** "Click Submit" (assumes mouse usage)

**Use "They" as Singular**
   Instead of "he or she" or awkward constructions, use singular "they."

   - **Good:** "When a user encounters an error, they should..."
   - **Avoid:** "When a user encounters an error, he/she should..."

**Be Specific About Users**
   Instead of generic "users," be specific about who you're talking about when possible.

   - **Good:** "people using screen readers," "developers integrating this tool"
   - **Okay:** "users" (when you truly mean everyone)

Jargon and Technical Terms
---------------------------

**Default to Plain Language**
   If a simpler word works, use it. Save technical terms for when they're actually needed.

   - **Good:** "color combination"
   - **Avoid:** "chromatic juxtaposition"

**Define Technical Terms on First Use**
   When you must use jargon, define it the first time it appears on a page.

   Example: "We test for WCAG (Web Content Accessibility Guidelines) compliance."

**Add Complex Terms to the Glossary**
   If a term needs explanation and you'll use it repeatedly, add it to the :doc:`glossary </reference/glossary>` and link to it.

**Acronyms**
   * Spell out on first use with acronym in parentheses
   * Don't capitalize the spelled-out version unless it's a proper noun
   * Add to glossary if used frequently

   Example: "Web Content Accessibility Guidelines (WCAG)"

Words to Avoid
--------------

**Ableist Language:**

* "sanity check" → use "coherence check" or "soundness check"
* "crazy" or "insane" → use "unexpected" or "surprising"
* "crippled" → use "broken" or "not functioning"
* "dummy" content → use "placeholder" or "sample"

**Assumptions:**

* "obviously," "clearly," "simply," "just" → If it were obvious, they wouldn't be reading the docs
* "easy" or "difficult" → Subjective; what's easy for you may be hard for others

**Vague Language:**

* "soon," "later," "recently" → Be specific with timeframes when possible
* "various," "some," "several" → Use specific numbers or examples

----

Documentation Types
===================

We have different documentation types, each with specific purposes:

Tutorials
---------

**Purpose:** Teach someone how to accomplish a specific task from start to finish.

**Structure:**

1. **Title:** Start with a verb (e.g., "Set Up Your Development Environment")
2. **Introduction:** What they'll accomplish and why it matters
3. **Prerequisites:** What they need before starting
4. **Step-by-step instructions:** Numbered list with clear actions
5. **Verification:** How to know it worked
6. **Next steps:** What to do after

**Tone:** Encouraging and supportive. Assume they're new.

How-To Guides
-------------

**Purpose:** Show how to solve a specific problem for someone with some context.

**Structure:**

1. **Problem statement:** What this guide solves
2. **Solution:** Clear, ordered steps
3. **Explanation:** Why this approach works
4. **Alternatives:** Other ways to accomplish the same thing (optional)

**Tone:** Practical and direct. Assume some familiarity.

Explanations
------------

**Purpose:** Provide background, context, or deeper understanding.

**Structure:**

1. **Overview:** What you're explaining and why it matters
2. **Details:** Go deep, but stay organized
3. **Examples:** Real-world applications
4. **Related concepts:** Links to what they should explore next

**Tone:** Thoughtful and thorough. Don't talk down.

Reference Documentation
-----------------------

**Purpose:** Provide complete, accurate information about commands, APIs, or features.

**Structure:**

* Alphabetical or logical ordering
* Consistent format for each item
* All parameters or options documented
* Examples of actual usage

**Tone:** Precise and complete. No personality needed.

----

Formatting Guidelines
=====================

Following RST Conventions
-------------------------

**Headings**

Use consistent underline characters::

    ================
    Page Title (H1)
    ================

    Section Heading (H2)
    ====================

    Subsection Heading (H3)
    -----------------------

    Subsubsection Heading (H4)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

**Code**

Inline code uses single backticks::

    Use the `custom.css` file.

Code blocks use double colons and indentation::

    Here's how to install::

        pip install sphinx

**Links**

External links::

    Visit `GitHub <https://github.com>`_ for more info.

Internal cross-references::

    See the :doc:`Getting Started guide </getting-started>`.

**Lists**

Bulleted lists need blank lines around them::

    Here are the options:

    * Option one
    * Option two
    * Option three

    Next paragraph.

Numbered lists use automatic numbering::

    Follow these steps:

    1. First step
    2. Second step
    3. Third step

**Notes and Warnings**

Use admonitions for important information::

    .. note::
       This is helpful context.

    .. warning::
       This could cause problems if ignored.

    .. important::
       Pay special attention to this.

----

Content Guidelines
==================

Screenshots and Images
----------------------

**When to Include:**

* Complex UI that's hard to describe
* Visual design concepts
* Workflow diagrams

**How to Include:**

* Use descriptive alt text: ``.. image:: path.png   :alt: Screenshot showing the Submit button in green``
* Annotate to draw attention to relevant parts
* Keep file sizes reasonable
* Use PNG for UI screenshots, SVG for diagrams when possible

**Accessibility:**

* Never rely on an image alone to convey information
* Describe what the image shows in the surrounding text
* Use meaningful alt text, not "image of..." or "screenshot of..."

Examples
--------

**Use Real Examples**
   Show actual code, real scenarios, and concrete examples. Not "foo," "bar," or "example.com" unless absolutely necessary.

**Show Context**
   Don't just show the one line that changed. Show enough surrounding code that people understand where it fits.

**Explain the Example**
   Don't just drop in code. Explain what it does and why this approach works.

Links
-----

**Descriptive Link Text**
   Never use "click here" or "read more." The link text should describe where it goes.

   * **Good:** "Read our :doc:`research ethics guidelines </research/ethics>`"
   * **Avoid:** "Click here for research ethics"

**External Links**
   Link to authoritative, stable sources. Avoid linking to content that might disappear or change significantly.

**Internal Links**
   Link generously to related documentation, but don't overdo it. One link per concept per page is usually enough.

----

Glossary Guidelines
===================

**When to Add a Term:**

* It's technical or specialized
* You use it more than once across documentation
* It might be unfamiliar to newcomers
* It has a specific meaning in our context

**How to Write Definitions:**

1. Start with a simple, one-sentence definition
2. Add context or examples if helpful
3. Link to longer explanations if they exist
4. Avoid circular definitions (don't define a term using itself)

**Example Entry:**

**WCAG**
   Web Content Accessibility Guidelines. International standards for making web content accessible to everyone, including people with disabilities. Maintained by the W3C.

Add terms to :doc:`glossary </reference/glossary>` and link to them from documentation using::

    :term:`WCAG`

----

Review Checklist
================

Before publishing documentation, check:

**Content:**

- ☐ Is the goal clear from the start?
- ☐ Is information organized logically?
- ☐ Are all claims accurate and current?
- ☐ Are examples realistic and working?

**Language:**

- ☐ Person-first language throughout?
- ☐ No ableist or exclusionary terms?
- ☐ Jargon defined or removed?
- ☐ Active voice used?

**Structure:**

- ☐ Headings are hierarchical and descriptive?
- ☐ Lists used appropriately?
- ☐ Paragraphs are focused and scannable?
- ☐ Code examples are formatted correctly?

**Accessibility:**

- ☐ Images have meaningful alt text?
- ☐ Links have descriptive text?
- ☐ Information isn't conveyed by color alone?
- ☐ Tables have proper headers?

**Consistency:**

- ☐ Matches our tone and voice?
- ☐ Follows RST formatting conventions?
- ☐ Technical terms used consistently?
- ☐ Links work and go to current content?

----

Getting Help
============

**Questions about style?**
   Create an issue tagged "documentation" and ask. We'll clarify and update this guide.

**Found an inconsistency?**
   Point it out! Our docs should practice what they preach.

**Disagree with a guideline?**
   Let's discuss it. This guide evolves based on what actually works for our community.

**Need a style decision we haven't covered?**
   Check the `Google Developer Documentation Style Guide <https://developers.google.com/style>`_ first, then ask the community.

----

*Good documentation respects the reader's time, meets them where they are, and helps them succeed. That's what we're building together.*
