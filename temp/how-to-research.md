# Research How-To 
*Step-by-step guides for each type of research quest*

Never done research before? No problem. These guides assume you're starting from zero and walk you through each type of investigation step by step.

---

##  Knowledge Gathering (Literature Reviews)
*"What does the research actually say about this topic?"*

### Step 1: Define Your Question (Week 1, Day 1-2)
**Pick something specific:**
-  Too broad: "accessibility and colors"
-  Just right: "do high contrast color schemes trigger vestibular symptoms?"

**Write it down:**
- What exactly do you want to know?
- Why would this help developers/designers?
- What would a good answer look like?

### Step 2: Find Your Sources (Week 1, Day 3-7)
**Start with free sources:**
- Google Scholar (scholar.google.com)
- PubMed for health-related topics
- Government accessibility sites (.gov)
- Major university research repositories

**Search tips:**
- Use simple terms first: "high contrast headaches"
- Try different combinations: "color contrast vestibular"
- Look at what recent papers cite for older studies

**Keep track:**
- Title, authors, year, where you found it
- One sentence about what it says
- Whether it's actually relevant

### Step 3: Read and Take Notes (Week 2)
**For each source:**
- Read the abstract first - does it actually answer your question?
- Skip if it's not relevant (seriously, it's okay)
- For relevant ones: what's the main finding?
- How many people did they study?
- Does their conclusion make sense from their data?

**Red flags to note:**
- Tiny sample sizes (like 12 people)
- Studies from decades ago that might be outdated
- Research funded by companies selling related products

### Step 4: Synthesize What You Found (Week 2-3)
**Look for patterns:**
- Do most studies agree?
- Where do they disagree?
- What questions are still unanswered?

**Write your findings using our template:**
```markdown
## TL;DR
[2-3 sentences: what's the main finding?]

## What Studies Found
- [Finding 1] - based on [X] studies with [Y] total participants
- [Finding 2] - but only [Z] studies looked at this
- [Conflicting finding] - some studies say X, others say Y

## So What Does This Mean?
[What should developers/designers actually do with this info?]

## What We Still Don't Know
[What questions still need research?]
```

### Step 5: Fact-Check Yourself (Week 3)
- Can someone else find your sources?
- Did you represent the findings fairly?
- Are you making claims bigger than the evidence supports?

---

##  Field Studies (Community Explorations)
*"What are people actually experiencing in real life?"*

### Step 1: Pick Your Community (Day 1-2)
**Choose based on:**
- A specific accessibility challenge you want to understand
- A community you can access respectfully (public forums, etc.)
- A group size that's manageable (start small!)

**Examples:**
- Reddit communities around specific conditions
- Developer forums discussing accessibility tools
- Social media hashtags about user experiences

### Step 2: Set Your Boundaries (Day 2-3)
**Decide:**
- Which platforms will you look at?
- What time period? (suggest 3-6 months max)
- What topics are you focusing on?
- What topics are off-limits? (crisis posts, very personal medical details)

**Write this down before you start** - it'll keep you focused.

### Step 3: Lurk and Learn (Week 1)
**Before collecting anything:**
- Read community rules and culture
- Understand what kinds of discussions happen
- Notice how people talk about their experiences
- Get a feel for community norms

**Don't collect yet** - just observe and understand.

### Step 4: Ethical Collection (Week 1-2)
**Read our [Social Media Ethics Guide](social-media-ethics.md) first.**

**As you collect:**
- Screenshot or copy relevant discussions privately
- Note general themes, don't focus on individual posts
- Remove usernames/identifying info immediately
- If something seems sensitive, skip it

**Keep track of:**
- Total posts you looked at
- How many were relevant
- General themes you're seeing
- Questions that come up

### Step 5: Find Patterns (Week 2)
**Look for:**
- What problems come up repeatedly?
- What solutions do people share?
- What frustrations are common?
- What works well for people?

**Group similar experiences:**
- Technical barriers (tools don't work)
- Social barriers (people don't understand)
- Design barriers (interfaces are confusing)
- etc.

### Step 6: Write It Up (Week 2-3)
**Use our template:**
```markdown
## The Community
- [General description - no identifying details]
- [Size/activity level]
- [Where you gathered info]

## What We Learned
- [Theme 1]: [Anonymous examples]
- [Theme 2]: [Anonymous examples]
- [Theme 3]: [Anonymous examples]

## Takeaways for Builders
[What should developers/designers do differently?]
```

**Never include:**
- Usernames or identifying details
- Direct quotes without permission
- Specific platform names if they could identify people

---

##  Tool Discovery (Ecosystem Mapping)
*"What tools already exist and how well do they work?"*

### Step 1: Define Your Territory (Day 1-2)
**Pick a specific domain:**
-  Too broad: "accessibility tools"
-  Just right: "color contrast checking tools"
-  Also good: "React accessibility testing libraries"

### Step 2: Find All the Tools (Week 1)
**Search everywhere:**
- Google with different terms
- GitHub topic searches
- Package managers (npm, pip, etc.)
- Tool directories and "awesome" lists
- Ask on relevant forums/communities

**Cast a wide net first** - you'll narrow down later.

### Step 3: Create Your Inventory (Week 1-2)
**For each tool, collect:**
- Name and website/repository
- What it does (one sentence)
- Who it's for (developers? designers? end users?)
- Cost (free, paid, freemium?)
- Last updated (is it maintained?)
- How popular it is (GitHub stars, downloads, etc.)

**Use a spreadsheet or simple table** - makes comparison easier later.

### Step 4: Test Key Tools (Week 2-3)
**Don't test everything** - pick 5-10 most promising ones.

**For each tool:**
- How easy is it to get started?
- Does it actually work as advertised?
- How's the documentation?
- What are the limitations?
- Any integration issues?

**Keep notes on:**
- Setup time
- Learning curve
- Actual usefulness
- Major pros/cons

### Step 5: Analyze the Landscape (Week 3)
**Look for:**
- What types of tools exist?
- What's missing?
- Which tools work well together?
- What are the common pain points?
- Are there clear leaders vs. niche tools?

### Step 6: Document Your Findings
**Use our template:**
```markdown
## The Full Landscape
### Established Tools
[The ones everyone knows about]

### Hidden Gems
[Good tools that aren't well-known]

### Gaps We Found
[What's missing that should exist]

## Recommendations
[Who should use what and when]
```

---

##  Research Proposals
*"Here's a question we should investigate"*

### Step 1: Identify the Mystery (Any time)
**Good questions come from:**
- Gaps you found in other research
- Problems you keep hearing about
- Assumptions everyone makes but no one has tested
- Tools that should exist but don't

### Step 2: Check If It's Already Been Done
**Quick search for:**
- Similar research questions
- Existing tools that solve this
- Recent discussions about this topic

**If someone else is already doing it:** Consider joining them or picking a different angle.

### Step 3: Write Your Proposal
**Use our template - keep it simple:**
```markdown
## The Question
[What exactly do we want to find out?]

## Why This Matters
[Who would benefit? What decisions could this inform?]

## How We Could Investigate
[Research methods, who we'd need to talk to]

## What We Hope to Learn
[Expected outcomes]
```

### Step 4: Share and Refine
- Post as a GitHub issue
- Get feedback from the community
- Revise based on suggestions
- See if others want to collaborate

---

##  Tech Proposals
*"Here's how we could build a solution"*

### Step 1: Start With a Problem
**Base your proposal on:**
- Research findings that point to a solution
- Community needs you've identified
- Gaps in existing tool landscape
- Your own experience with accessibility challenges

### Step 2: Sketch the Solution
**Think through:**
- What would this tool actually do?
- Who would use it and when?
- How would it fit into existing workflows?
- What would success look like?

### Step 3: Research Feasibility
**Check:**
- Are there existing libraries you could build on?
- What's the technical complexity?
- How much work would this be?
- What skills would contributors need?

### Step 4: Write Your Proposal
```markdown
## The Problem
[What research/experience led to this idea?]

## Proposed Solution
[High-level description, maybe some code examples]

## Technical Approach
[How you'd build it, what technologies]

## Success Criteria
[How would we know this actually helps people?]
```

### Step 5: Get Community Input
- Share as GitHub issue
- Ask for technical feedback
- See if others want to collaborate
- Refine based on discussion

---

##  Getting Help

**Stuck on any step?**
- Comment on research issues
- Ask in community discussions
- Tag maintainers for guidance

**Not sure if your research is good enough?**
- Share early drafts for feedback
- Remember: helpful insights matter more than perfect methodology
- Community will help you improve

**Worried about ethics?**
- Read our [Ethics Guide](research-ethics.md)
- When in doubt, ask
- Protecting people is always the priority

---

**Remember:** Research is about curiosity and helping people, not impressing academics. Start simple, ask questions, and improve as you go.

*Every expert was once a beginner who asked good questions* 