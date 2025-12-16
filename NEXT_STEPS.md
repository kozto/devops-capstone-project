# ✅ User Stories Preparation Complete - Next Steps

## What Has Been Done

All the content and automation scripts for creating seven user stories have been prepared and are ready to use. The user stories follow the project's existing template format and cover all required milestones.

## ⚠️ Important: What You Need to Do

**I cannot directly create GitHub Issues** due to security and permission constraints. You need to complete one of the following steps to create the actual issues in your GitHub repository.

## Three Options to Create the Issues

### ✨ Option 1: Automated with GitHub CLI (Recommended - Takes ~10 seconds)

**Prerequisites:** GitHub CLI must be installed and authenticated

```bash
# 1. Install GitHub CLI if not already installed
# macOS: brew install gh
# Linux: See https://cli.github.com/
# Windows: See https://cli.github.com/

# 2. Authenticate (if not already done)
gh auth login

# 3. Navigate to repository and run script
cd path/to/devops-capstone-project
./.github/create_user_stories.sh

# Done! All seven issues will be created automatically
```

### 🐍 Option 2: Automated with Python API (Alternative automation)

**Prerequisites:** Python 3 and GitHub Personal Access Token

```bash
# 1. Install requests library
pip install requests

# 2. Create a GitHub Personal Access Token
# Go to: https://github.com/settings/tokens
# Create token with 'repo' scope

# 3. Set token and run script
export GITHUB_TOKEN=your_token_here
cd path/to/devops-capstone-project
python3 ./.github/create_user_stories.py

# Done! All seven issues will be created automatically
```

### 📝 Option 3: Manual Creation (Most control)

1. Go to https://github.com/kozto/devops-capstone-project/issues
2. Click "New Issue"
3. Open `.github/user_stories.md` in this repository
4. Copy User Story 1 content
5. Paste into issue form
6. Add label "user story"
7. Click "Submit new issue"
8. Repeat steps 2-7 for User Stories 2-7

**Estimated time:** ~10-15 minutes for all seven stories

## After Creating the Issues

### Set Up Your Kanban Board

1. Go to the **Projects** tab in your repository
2. Create a new Project (Board layout)
3. Add columns:
   - **New Issues** ← This is where your stories should go initially
   - **In Progress**
   - **Review**
   - **Done**
4. Add all seven issues to the project
5. Ensure they appear in the **"New Issues"** column

### Verify Success

Check that:
- ✓ Seven issues exist with titles matching the user stories
- ✓ All issues are labeled "user story"
- ✓ All issues follow the template format (As a... I need... So that...)
- ✓ All issues are added to your kanban board
- ✓ All issues are in the "New Issues" pipeline

## The Seven User Stories You'll Create

1. **Setup the Development Environment** - Configure dev tools and environment
2. **Read an Account from the Service** - Implement GET /accounts/{id}
3. **Update an Account in the Service** - Implement PUT /accounts/{id}
4. **Delete an Account from the Service** - Implement DELETE /accounts/{id}
5. **List All Accounts in the Service** - Implement GET /accounts
6. **Containerize the Microservice Using Docker** - Create and build Dockerfile
7. **Deploy Docker Image to Kubernetes** - Deploy to K8s cluster

## Documentation Reference

- **Quick Start Guide:** `CREATING_ISSUES_GUIDE.md` (in repository root)
- **Detailed Instructions:** `.github/USER_STORIES_README.md`
- **Full Story Content:** `.github/user_stories.md`
- **Bash Script:** `.github/create_user_stories.sh`
- **Python Script:** `.github/create_user_stories.py`

## Troubleshooting

### "gh: command not found"
Install GitHub CLI: https://cli.github.com/

### "Error: GITHUB_TOKEN environment variable is not set"
For Python script: `export GITHUB_TOKEN=your_token_here`

### "Permission denied"
Ensure you have write access to the repository

### "Module 'requests' not found"
For Python script: `pip install requests`

## Project Context

This DevOps Capstone Project involves:
- Building a Customer Account Microservice with Flask
- Implementing CRUD operations (Create, Read, Update, Delete, List)
- Using PostgreSQL for data persistence
- Containerizing with Docker
- Deploying to Kubernetes
- Following Test-Driven Development (TDD) practices

The user stories guide you through implementing these features step by step.

## Questions or Issues?

- Review the detailed documentation in `.github/USER_STORIES_README.md`
- Check the repository's main `README.md` for project overview
- Consult your course materials for additional context

---

**Ready to proceed?** Choose one of the three options above and create your issues! The fastest way is Option 1 with GitHub CLI.
