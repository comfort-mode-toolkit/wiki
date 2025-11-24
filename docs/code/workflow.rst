=======================
Development Workflow
=======================

*How to ship code without losing your mind*

----

This guide explains our process for making changes, getting them reviewed, and merging them.

The Cycle
=========

1. **Pick an Issue**
   Find something to work on. Assign it to yourself or comment that you're looking into it.

2. **Create a Branch**
   Name it descriptively::

       git checkout -b fix/contrast-calculation-bug

   Use prefixes like ``fix/``, ``feat/``, ``docs/``, or ``refactor/``.

3. **Make Changes**
   Write your code. Keep changes focused on the issue at hand.

4. **Test Locally**
   Run the test suite::

       pytest

   Add new tests if you added new functionality.

5. **Commit and Push**
   Write clear commit messages::

       git commit -m "Fix contrast calculation for dark mode"
       git push origin fix/contrast-calculation-bug

6. **Open a Pull Request (PR)**
   Go to GitHub and open a PR against the ``main`` branch. Fill out the template.

Code Review
===========

* **Be patient:** We're volunteers. It might take a few days.
* **Be open:** Feedback is about the code, not you.
* **Ask questions:** If a comment isn't clear, ask for clarification.

Merging
=======

Once your PR is approved and tests pass, a maintainer will merge it. You can then delete your branch.

----

*Small, focused PRs are easier to review and faster to merge.*
