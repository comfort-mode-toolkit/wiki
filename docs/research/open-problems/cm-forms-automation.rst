.. contents::
   :depth: 3
..

CM-Forms: Automation Safety in Form Accessibility
=================================================

| **Status:** Active Research \| **Started:** November 2025
| **Research Question:** What can we automate safely, and what requires
  human judgment?

--------------

The Context
-----------

Forms are where the web asks people to do things: sign up, log in, buy
something, share information, get help. When forms aren't accessible,
people get locked out of essential services—banking, healthcare,
education, employment.

Missing form labels are consistently among the top six accessibility
errors on the web, affecting roughly 39% of form inputs. That's millions
of forms where people using screen readers don't know what information
to enter.

But here's the tension: **form accessibility is both mechanical and
deeply human**.

Some things are purely mechanical: 
- A ``<label>`` element must be connected to its ``<input>`` via matching ``for`` and ``id`` attributes
- Required fields need ``required`` or ``aria-required="true"`` 
- Submit buttons need accessible names

Other things require context only a human has: 
- What should the label
*say*? (“Email” vs “Work Email” vs “Email for Receipt”) 
- What does this
error *mean*? (“Invalid format” vs “Please use the format: name@example.com”) 
- Is this form even asking the right questions for
its purpose?

The Problem We're Trying to Solve
---------------------------------

**For developers:** You're building a login form at 2am. You know it
needs labels, but WCAG is 78 pages and you're not sure if your
implementation is correct. You want to do better, but “learn all of
WCAG” isn't feasible right now.

**For people using assistive technology:** Another unlabeled form.
Another mystery about what goes in which field. Another time you have to
guess or give up.

**The gap:** There's a huge distance between “I want to build an
accessible form” and “I deeply understand WCAG 2.2, ARIA 1.3, and how
screen readers interpret form markup across different browsers.”

What We're *Not* Trying to Do
-----------------------------

We are **not** trying to: 
- Replace accessibility expertise 
- Promise “instant WCAG compliance” 
- Generate meaningful label text from field names 
- Determine if your form makes sense for its purpose 
- Test with real screen reader users 
- Understand the context of your application

Those things matter enormously. They're just not things a tool can do
reliably.

What We *Are* Trying to Do
--------------------------

We're trying to build a tool that catches the **mechanical errors** so
developers can focus on the **meaningful content**.

Think of it like a spell checker: it catches “teh” but it can't tell you
if your sentence makes sense. That's still valuable—it's just not the
whole job.

Our Safety Framework
~~~~~~~~~~~~~~~~~~~~

We're categorizing form accessibility tasks into three buckets:

Safe to Automate
^^^^^^^^^^^^^^^^^^^

Things we can fix with 100% confidence, zero risk of making things
worse.

**Example:** Linking ``<label for="username">`` to
``<input id="username">`` when they're in the same form and nothing else
conflicts.

**Why it's safe:** The WCAG requirement is purely mechanical. There's no
ambiguity, no context needed.

Can Suggest, Cannot Fix
^^^^^^^^^^^^^^^^^^^^^^^^^^

Things we can detect and guess at, but must let the developer decide.

**Example:** An input named ``name="email"`` probably wants
``autocomplete="email"``, but maybe it's asking for someone else's
email, or it's a different kind of email field.

**Why it's not safe:** We'd be making assumptions about meaning and
purpose without context.

Must Not Automate
^^^^^^^^^^^^^^^^^^^^

Things that require human understanding of context, purpose, and
meaning.

**Example:** Writing the actual text for error messages. We can detect
that an error message exists, but we can't know what it should *say* in
a way that helps your specific users understand the specific problem in
your specific form.

**Why it's not safe:** Language, tone, helpfulness, and clarity depend
entirely on your application's context and your users' needs.

The Research Questions
----------------------

This document tracks our investigation into:

1. | **What are the most common form accessibility errors?**
   | *Why this matters:* We should focus on errors that actually affect
     people, not edge cases.

2. | **Which errors can be detected by reading code (static analysis)?**
   | *Why this matters:* If we can't reliably detect it, we can't fix it
     or warn about it.

3. | **Which detectable errors can be fixed with zero risk?**
   | *Why this matters:* This defines the boundary of safe automation.

4. | **What are the failure modes of form accessibility automation?**
   | *Why this matters:* We need to know how automation goes wrong so we
     don't repeat those mistakes.

5. | **How do we communicate uncertainty to developers?**
   | *Why this matters:* A warning that says “this might be wrong” needs
     to be clear about *what* might be wrong and *why* it matters.

What Success Looks Like
-----------------------

**For developers:** - Catch mechanical errors they didn't know about
(missing labels, broken ARIA references) - Get warnings about things
that need their attention (ambiguous button text, missing error
messages) - Learn *why* something needs fixing, not just *that* it does
- Spend their time on meaningful content, not hunting for missing ``id``
attributes

**For users:** - Fewer forms that are completely unlabeled - More forms
where the mechanical structure works (even if content needs improvement)
- Incremental progress toward a more accessible web

**For accessibility advocates:** - A tool that doesn't promise what it
can't deliver - Developers who understand the difference between
“mechanically connected” and “meaningfully labeled” - A bridge that
actually helps people learn, not a shortcut that lets them ignore the
real work

What We're Learning So Far
--------------------------

*(This section will be updated as research progresses)*

Current Status (v0.0.1)
~~~~~~~~~~~~~~~~~~~~~~~

Our initial implementation: 
- Detects unlabeled inputs 
- Adds basic ``<label>`` elements for inputs with ``id`` but no label 
- Adds ``aria-required="true"`` to inputs with the ``required`` attribute 
- Warns when button text is generic/ambiguous (“Submit”, “Click Here”) 
- Does NOT generate label text from ``name`` attributes 
- Does NOT modify existing labels

**Example output:**

::

   Processed: signup.html -> signup_cm.html
   - Added label to <input id="username">
   - Added label to <input id="email">
   - Added aria-required="true" to <input id="email">
   - Added aria-required="true" to <input id="password">
   - WARNING: <button> label "Submit" is ambiguous, developer review needed

Experiments & Research
----------------------

Below is an index of research experiments investigating specific
questions about form automation safety. Each experiment follows a
consistent format: hypothesis, methodology, findings, and
recommendations.

**Want to add your own research?** See our `Contributing
Guide <./CONTRIBUTING.md>`__ for experiment templates and submission
process.

--------------

Experiment Index
~~~~~~~~~~~~~~~~

*Research experiments will be listed here as they're added, in the
format:*

.. `EXP-001: Label Detection Accuracy <./experiments/001-label-detection/>`__
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. | **Question:** Can we reliably detect when a label is missing vs. when
..   it's intentionally not visible?
.. | **Status:** In Progress
.. | **Owner:** [@contributor-name]

.. `EXP-002: Autocomplete Inference Safety <./experiments/002-autocomplete-inference/>`__
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. | **Question:** How accurate are ``name`` attribute patterns for
..   inferring ``autocomplete`` values?
.. | **Status:** Planning
.. | **Owner:** Available

.. `EXP-003: Error Message Detection <./experiments/003-error-message-detection/>`__
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. | **Question:** Can we detect missing error messages without generating
..   bad ones?
.. | **Status:** Planning
.. | **Owner:** Available

.. --------------

How to Contribute
-----------------

We need people with different perspectives and expertise:

**If you're a developer:** Test our tools on real forms. Tell us what
breaks, what helps, what's confusing.

**If you use assistive technology:** Tell us what actually matters. What
errors make forms unusable vs. just annoying?

**If you're an accessibility professional:** Tell us where we're wrong.
What are we missing? What's dangerous?

**If you're a researcher:** Help us understand the data. What do form
accessibility studies tell us? What's speculation vs. evidence?

**If you're a student/beginner:** Ask questions. If our documentation
doesn't make sense to you, it needs to be better.

**No PhD required. No experience required. Just honesty about what you
know and what you don't.**

--------------

Principles Guiding This Work
----------------------------

1. **Transparency over promises:** We document what we can't do as
   prominently as what we can.

2. **Safety over completeness:** We'd rather catch 20% of errors safely
   than attempt 80% and cause harm.

3. **Teaching over automation:** If a developer learns *why* something
   needs fixing, that's better than silently fixing it.

4. **Progressive improvement:** 70% accessible is better than 0%, even
   if it's not 100%.

5. **Honest about limitations:** We're building a bridge, not a
   teleporter. Bridges are useful even if they don't solve everything.

What We Need Help With
----------------------

-   **Research:** Finding studies on common form errors, testing
    real-world forms, analyzing failure patterns
-   **Code:** Building detection algorithms, writing tests, improving
    the parser
-   **Documentation:** Explaining why things matter, writing clear
    warnings, creating examples
-   **Testing:** Running cm-forms on real projects, finding edge
    cases, reporting what breaks
-   **Debate:** Challenging our assumptions, finding holes in our
    logic, pushing back on what's “safe”

--------------

Questions or Concerns?
----------------------

Open an issue. Challenge our approach. Tell us where we're being naive
or where we're not thinking about something.

This is hard work at the intersection of code, humans, and
accessibility. We're going to get things wrong. **Help us get them less
wrong.**

--------------

*Building bridges across the accessibility gap—because the stakes are
deeply human.*
