<!-- # Tech Setup
( Don't worry, it's not as scary as it may sound - we got you! )

If you want to edit docs / non tech stuff
You just need a github account  -->
<!-- Steps to add docs / create pr / evth from web itself  -->

<!-- For code / tech stuff -->

<!-- One time setup
1. Install / check git version
2. Sign up for github if not already
3. Set up ssh for local commit and push

For specific repo
1. Copy the url
2. fork the repo
3. `git clone forked-repo-url`
4. creatign an env
5. pip install requirements.txt
6. open the folder
7. make changes
8. commit
9. go to github to click contribute
10. open a pr -->

# Tech Setup Guide 🛠️
*Don't worry, it's not as scary as it sounds - we got you!*

Whether you want to fix a typo or build the next amazing accessibility tool, here's how to get set up. Pick your adventure level!

---

## 🌱 Level 1: Just Want to Edit Docs or Add Ideas?
*No scary terminal commands needed!*

**You just need:** A GitHub account (it's free!)

### Quick Start:
1. **Sign up for GitHub** at [github.com](https://github.com) if you don't have an account
2. **Find what you want to change** - browse our repositories and find a file you want to edit
3. **Click the pencil icon** (✏️) on any file to edit it directly in your browser
4. **Make your changes** using the built-in editor
5. **Scroll down and describe your changes** in the text boxes
6. **Click "Propose changes"** - this creates what we call a "pull request"
7. **Wait for review** - someone will look at your changes and merge them!

**That's it!** No software to install, no commands to remember. GitHub handles everything in your browser.

---

## ⚔️ Level 2: Want to Code or Make Bigger Changes?
*Time to set up your development sandbox!*

### One-Time Setup (Do This Once)

#### Step 1: Install Git
**What it is:** Git tracks changes to code so teams can work together without chaos.

**Mac users:**
- Git might already be installed! Open Terminal and type: `git --version`
- If not installed, it'll prompt you to install it, or download from [git-scm.com](https://git-scm.com)

**Windows users:**
- Download Git from [git-scm.com](https://git-scm.com) 
- Install with default settings (just keep clicking "Next")

**Linux users:**
- You probably already know: `sudo apt install git` or `sudo yum install git`

#### Step 2: GitHub Account Setup
1. **Sign up at [github.com](https://github.com)** if you haven't already
2. **Set up SSH keys** (this lets you push code without typing your password every time)
   
   In your terminal/command prompt:
   
   ```bash
   # Generate a new SSH key (replace email with yours)
   ssh-keygen -t ed25519 -C "your_email@example.com"
   
   # When prompted, just press Enter for default location
   # Set a passphrase or press Enter to skip
   ```
   

4. **Add the SSH key to GitHub:**
   ```bash
   # Copy your public key (this command works on Mac/Linux)
   cat ~/.ssh/id_ed25519.pub
   
   # On Windows, use:
   type %USERPROFILE%\.ssh\id_ed25519.pub
   ```
   - Copy the output
   - Go to GitHub → Settings → SSH and GPG keys → New SSH key
   - Paste your key and save

5. **Tell Git who you are:**
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your_email@example.com"
   ```

**Test it works:** `ssh -T git@github.com` should say "Hi [username]!"

#### Step 3: Install Python (for our current tools)
**What it is:** The programming language most of our tools use.

- **Download Python 3.8 or newer** from [python.org](https://python.org)
- **During installation:** Check "Add Python to PATH" (very important!)
- **Test it works:** Open terminal and type `python --version`

---

### For Each Project You Want to Work On

Let's say you want to work on CM-Colors. Here's the dance:

#### Step 1: Fork the Repository
1. **Go to the project page** (like [github.com/comfort-mode-toolkit/cm-colors](https://github.com/comfort-mode-toolkit/cm-colors))
2. **Click "Fork"** in the top-right corner
3. **This creates your own copy** you can mess with safely

#### Step 2: Clone Your Fork
**What this means:** Download the code to your computer so you can edit it.

```bash
# Get the URL from your fork (green "Code" button)
git clone git@github.com:YOUR-USERNAME/cm-colors.git

# Go into the folder
cd cm-colors
```

#### Step 3: Set Up Your Environment
**Why:** Keeps this project's requirements separate from other Python projects.

```bash
# Create a virtual environment (like a clean room for this project)
python -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install what the project needs
pip install -r requirements.txt

# If there's also a requirements-dev.txt (for development tools):
pip install -r requirements-dev.txt
```

**You'll know it worked when** your terminal prompt shows `(venv)` at the beginning.

#### Step 4: Make Your Changes
1. **Open the folder** in your favorite code editor (VS Code, PyCharm, whatever you like)
2. **Make your changes** - fix bugs, add features, update docs
3. **Test your changes** - run any tests, try the tool yourself

#### Step 5: Save and Share Your Work
```bash
# See what you changed
git status

# Add your changes to be saved
git add .

# Save them with a message describing what you did
git commit -m "Fix color contrast calculation for edge case"

# Send your changes to your GitHub fork
git push origin main
```

#### Step 6: Create a Pull Request
1. **Go to your fork on GitHub** - there should be a banner saying "Compare & pull request"
2. **Click it** (or go to the original repo and click "New pull request")
3. **Fill out the template** we provide
4. **Submit and wait for review!**

---

## 🆘 When Things Go Wrong

### "Command not found" errors
- **On Windows:** Make sure you checked "Add to PATH" during installation
- **Restart your terminal** after installing new software
- **Try the full path:** Instead of `python`, try `/usr/bin/python3` or `C:\Python39\python.exe`

### SSH/Git authentication issues
- **Check your SSH key:** `ssh -T git@github.com` should work
- **Use HTTPS instead:** Replace `git@github.com:` with `https://github.com/` in clone URLs
- **GitHub has good docs:** Search "GitHub SSH setup" for detailed help

### Python/pip issues
- **Use python3:** On some systems, `python` is Python 2, use `python3` instead
- **Virtual environment not working:** Make sure you activated it (`source venv/bin/activate`)
- **Permission errors:** Don't use `sudo` with pip, fix your virtual environment instead

### Git confusing you
- **Start over:** Delete the folder and clone again (your GitHub fork is safe)
- **Undo last commit:** `git reset --soft HEAD~1`
- **When all else fails:** Ask in the GitHub discussions, we've all been there!

---

## 🧙‍♂️ Glossary

**Clone:** Download a copy of code from GitHub to your computer

**Commit:** Save a set of changes with a message describing what you did

**Fork:** Make your own copy of someone else's project on GitHub

**Git:** Tool that tracks changes to code so teams can work together

**Pull Request (PR):** Way to submit your changes back to the original project

**Repository (repo):** A project's folder containing all its code and history

**SSH Key:** A secure way to prove your identity to GitHub without passwords

**Terminal/Command Line:** Text-based way to talk to your computer (scary looking, actually friendly)

**Virtual Environment:** Isolated space for a project's requirements so they don't conflict with other projects

---

## 🤝 Need Help?

**Stuck on setup?** Create an issue tagged `setup-help` and we'll walk you through it.

**Something not working?** Don't suffer in silence! The community is here to help.

**Never coded before?** That's totally fine! We all started somewhere. Ask questions, make mistakes, learn together.

**Imposter syndrome kicking in?** You belong here. Your perspective and contributions matter, regardless of experience level.

---

*Remember: Every expert was once a beginner. Every contribution makes the web a little more comfortable for someone. You've got this!* 🌟

---

## Quick Reference Card

```bash
# Daily workflow after initial setup:
cd your-project-folder
source venv/bin/activate  # (or venv\Scripts\activate on Windows)
# Make your changes
git add .
git commit -m "Describe what you did"
git push origin main
# Go to GitHub to create pull request
```

Save this page - you'll probably need to reference it until the commands become muscle memory!