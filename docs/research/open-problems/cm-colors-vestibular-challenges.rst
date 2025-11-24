.. contents::
   :depth: 3
..

CM-Colors: Vestibular Safety in Color Contrast Optimization
===========================================================

| **Status:** Active Research \| **Started:** October 2025
| **Research Question:** How do we balance contrast requirements with
  vestibular safety?

--------------

The Context
-----------

Color contrast isn’t just about passing WCAG thresholds. It’s about
making text readable without causing physical harm.

When contrast is too low, people can’t read your content. When contrast
is too high—or when certain color combinations are used—some people
experience dizziness, nausea, migraines, or even seizures.

This puts us in a difficult position: accessibility standards require
sufficient contrast, but cranking contrast to maximum can create new
barriers for people with vestibular disorders, photosensitivity, or
seizure conditions.

The Problem We’re Trying to Solve
---------------------------------

**For designers:** You want your brand colors. You also want everyone to
be able to read your content. But “just make it higher contrast” can
trigger vestibular symptoms in some users.

**For people with vestibular conditions:** High-contrast interfaces,
especially with certain color combinations or saturation levels, can
cause dizziness, nausea, disorientation, or migraines. “Accessible” by
WCAG standards can be inaccessible in practice.

**For people who need high contrast:** Low contrast makes text
unreadable. You need the contrast to be there—just not in ways that
trigger other issues.

**The gap:** WCAG gives us a minimum contrast ratio (4.5:1 for normal
text), but it doesn’t tell us when we’ve gone too far. There’s no
standard for “this combination is too harsh” or “this saturation level
triggers symptoms.”

What We’re *Not* Trying to Do
-----------------------------

We are **not** trying to: - Replace WCAG contrast requirements with
something weaker - Promise “universally safe” colors (individual
triggers vary) - Make aesthetic judgments about your design - Override
your brand colors without reason - Claim we can prevent all vestibular
triggers - Reduce contrast below accessibility minimums

Those things either aren’t possible or would undermine actual
accessibility.

What We *Are* Trying to Do
--------------------------

We’re trying to understand where the boundary is between “high enough
contrast to read” and “harsh enough to trigger symptoms.”

Currently, cm-colors takes your color palette and adjusts it to meet
WCAG contrast minimums. But we don’t have guidelines for: - When
saturation becomes problematic - Which color combinations are more
likely to trigger issues - How bright is “too bright” for photosensitive
users - Whether certain color spaces (OKLCH, LAB) handle this better
than others

We want to find the sweet spot: readable for everyone, comfortable for
as many people as possible.

Our Safety Framework
~~~~~~~~~~~~~~~~~~~~

We’re investigating color properties across three dimensions:

Mechanical Requirements (Must Meet)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Things we cannot compromise on because they make content unreadable.

**Example:** WCAG 4.5:1 contrast ratio for normal text.

**Why it’s non-negotiable:** Below this threshold, text becomes
unreadable for people with low vision, color blindness, or viewing in
bright light.

Trigger Thresholds (Need to Identify)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Properties where going beyond certain values can cause physical
symptoms.

**Example:** Saturation levels above X% combined with contrast ratios
above Y:1 may trigger vestibular symptoms.

**What we don’t know yet:** What those thresholds actually are, whether
they’re universal or individual, and how to detect them algorithmically.

User Preferences (Should Enable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Individual variations that can’t be standardized but should be
controllable.

**Example:** Some people prefer lower saturation even if it meets
contrast minimums; others need maximum contrast.

**What we’re exploring:** How to build tools that let users adjust
within safe ranges rather than imposing one “correct” answer.

The Research Questions
----------------------

This document tracks our investigation into:

1. **What specific color properties trigger vestibular symptoms?**
   *Why this matters:* We can’t avoid triggers if we don’t know what
   they are.

   -  Saturation thresholds
   -  Brightness levels
   -  Specific color combinations
   -  Flicker or visual vibration effects from certain contrasts

2. **Where is the boundary between accessible contrast and triggering
   contrast?**
   *Why this matters:* This defines how much we can optimize without
   causing harm.

   -  How high can contrast go before becoming problematic?
   -  Are there color spaces that handle this better?
   -  Do some hue combinations handle high contrast better than others?

3. **What do people with vestibular conditions actually experience?**
   *Why this matters:* Academic papers don’t always capture lived
   experience.

   -  Which color combinations cause problems in practice?
   -  What strategies do people use to make interfaces more comfortable?
   -  Are there patterns in what works vs. what doesn’t?

4. **How do we measure this algorithmically?**
   *Why this matters:* If we can’t quantify it, we can’t build tools
   around it.

   -  Can we detect “harsh” combinations programmatically?
   -  Are there existing color spaces that model visual comfort?
   -  What metrics beyond contrast ratio matter?

5. **What are existing tools doing (or not doing)?**
   *Why this matters:* We don’t need to reinvent wheels, but we need to
   understand gaps.

   -  How do current accessibility tools handle vestibular
      considerations?
   -  What compromises are other tools making?
   -  Where are the gaps in available solutions?

What Success Looks Like
-----------------------

**For designers:** - Keep your brand colors (or something very close) -
Meet WCAG contrast requirements - Avoid color combinations known to
trigger symptoms - Understand *why* certain adjustments are being
suggested

**For people with vestibular conditions:** - Fewer interfaces that cause
dizziness, nausea, or migraines - Tools that acknowledge your needs
exist alongside contrast needs - Options to adjust colors within safe
ranges based on your preferences

**For people who need high contrast:** - Still get readable text - Not
have contrast reduced below usable levels in the name of “comfort” -
Have confidence that adjustments are based on evidence, not guesswork

**For accessibility advocates:** - Tools that don’t weaken contrast
requirements - Evidence-based approach rather than assumptions -
Acknowledgment that accessibility isn’t one-size-fits-all

What We’re Learning So Far
--------------------------

*(This section will be updated as research progresses)*

Current Status
~~~~~~~~~~~~~~

cm-colors currently: - Adjusts colors to meet WCAG contrast minimums -
Preserves hue and adjusts lightness to reach target contrast - Does NOT
consider saturation effects - Does NOT warn about potentially triggering
combinations - Does NOT offer user-configurable comfort preferences

Known Gaps
~~~~~~~~~~

What we don’t know yet: - Specific saturation thresholds that correlate
with vestibular symptoms - Whether certain hue pairs are more
problematic than others at high contrast - How individual variation
affects what’s “safe” vs. triggering - Whether perceptually uniform
color spaces (OKLCH, LAB) help with this problem - How
brightness/luminance thresholds relate to photosensitivity

Community Feedback
~~~~~~~~~~~~~~~~~~

This research was sparked by `community
discussion <https://www.reddit.com/r/accessibility/comments/1gvos7l/color_contrast_but_make_it_comfy_seeking_feedback/>`__
highlighting that: - Traditional contrast-focused tools don’t consider
vestibular needs - High-contrast interfaces can be inaccessible for
people with certain conditions - There’s a gap between WCAG compliance
and actual comfort - Users need more control over how contrast is
achieved

Experiments & Research
----------------------

Below is an index of research experiments investigating the relationship
between color properties and vestibular/neurological triggers. Each
experiment follows a consistent format: hypothesis, methodology,
findings, and recommendations.

**Want to add your own research?** See our `Contributing
Guide <./CONTRIBUTING.md>`__ for experiment templates and submission
process.

--------------

Experiment Index
~~~~~~~~~~~~~~~~

*Research experiments will be listed here as they’re added, in the
format:*

.. raw:: html

   <!-- #### [EXP-001: Saturation Threshold Literature Review](./experiments/001-saturation-thresholds/)
   **Question:** What does existing research tell us about saturation levels and vestibular symptoms?  
   **Status:** Planning  
   **Owner:** Available

   #### [EXP-002: Color Combination Case Studies](./experiments/002-color-combinations/)
   **Question:** What color combinations do people with vestibular conditions report as problematic?  
   **Status:** Planning  
   **Owner:** Available

   #### [EXP-003: Tools Analysis](./experiments/003-existing-tools/)
   **Question:** How do existing accessibility tools handle vestibular considerations?  
   **Status:** Planning  
   **Owner:** Available

   #### [EXP-004: Color Space Comparison](./experiments/004-color-spaces/)
   **Question:** Do perceptually uniform color spaces better predict visual comfort?  
   **Status:** Planning  
   **Owner:** Available -->

--------------

How to Contribute
-----------------

We need people with different perspectives and expertise:

**If you experience vestibular issues:** Tell us what color combinations
or properties cause problems for you. Your lived experience is data we
don’t have.

**If you’re a designer:** Test cm-colors on real palettes. Tell us what
works, what breaks, what feels wrong.

**If you’re a researcher:** Help us find and interpret academic papers
on photosensitivity, vestibular disorders, and color perception.

**If you’re a developer:** Help us figure out how to measure these
properties algorithmically and implement safe defaults.

**If you work in accessibility:** Tell us where we’re being naive about
WCAG requirements or where our approach conflicts with established
standards.

**No PhD required. No experience required. Just honesty about what you
know and what you’ve experienced.**

Research We Need
~~~~~~~~~~~~~~~~

We’re documenting evidence-based guidelines for balancing contrast and
comfort. This means:

**Literature reviews:** - Academic papers on vestibular disorders and
visual triggers - Studies on photosensitivity and color/brightness
thresholds - Research on perceptual color spaces and visual comfort

**Case studies:** - Real experiences from people with vestibular
conditions - Examples of interfaces that work well vs. poorly - Analysis
of successful and problematic color schemes

**Tool analysis:** - Survey of existing accessibility and color tools -
Documentation of how they handle (or don’t handle) vestibular
considerations - Gap analysis showing what’s missing

**Experimentation:** - Testing color combinations with users who have
vestibular conditions - Measuring properties of “comfortable”
vs. “harsh” palettes - Developing algorithms to detect potentially
problematic combinations

Principles Guiding This Work
----------------------------

1. **Evidence over assumptions:** We don’t implement restrictions
   without understanding why they matter.

2. **Both/and, not either/or:** We’re not choosing between contrast and
   comfort—we’re finding where they can coexist.

3. **Individual variation matters:** What triggers symptoms varies by
   person. Tools should enable preferences, not enforce one answer.

4. **WCAG is a floor, not a ceiling:** We meet minimums, but we’re
   exploring what else matters beyond the standard.

5. **Lived experience is data:** Academic papers are valuable, but so
   are people’s actual experiences using interfaces every day.

What We Need Help With
----------------------

-  **Research:** Finding studies, analyzing papers, synthesizing
   findings into actionable guidelines
-  **Experiences:** Sharing what color combinations or properties cause
   issues for you
-  **Code:** Building detection algorithms, testing color space
   transformations
-  **Design:** Testing real palettes, identifying patterns in what works
-  **Testing:** Trying cm-colors on real projects, finding edge cases
-  **Challenge:** Pushing back on assumptions, finding holes in logic

--------------

Questions or Concerns?
----------------------

Open an issue. Share your experience. Tell us where we’re missing the
mark.

This is hard work at the intersection of accessibility standards, color
science, and individual human neurology. We’re going to get things
wrong. **Help us get them less wrong.**

--------------

*Building bridges across the accessibility gap—because the stakes are
deeply human.*
