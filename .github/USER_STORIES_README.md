# Creating User Stories for DevOps Capstone Project

This directory contains resources to create seven user stories as GitHub Issues for the DevOps Capstone Project.

## Overview

Seven user stories have been prepared covering the following project milestones:

1. **Setup the Development Environment** - Configure Python, PostgreSQL, and development tools
2. **Read an Account from the Service** - Implement GET /accounts/{id} endpoint
3. **Update an Account in the Service** - Implement PUT /accounts/{id} endpoint
4. **Delete an Account from the Service** - Implement DELETE /accounts/{id} endpoint
5. **List All Accounts in the Service** - Implement GET /accounts endpoint
6. **Containerize the Microservice Using Docker** - Create Dockerfile and containerize the application
7. **Deploy Docker Image to Kubernetes** - Create Kubernetes manifests and deploy the service

## Files Provided

- **user_stories.md** - Full content of all seven user stories in Markdown format
- **create_user_stories.sh** - Bash script to create issues using GitHub CLI
- **create_user_stories.py** - Python script to create issues using GitHub REST API
- **USER_STORIES_README.md** - This file (instructions)

## Methods to Create the Issues

### Method 1: Using the Web Interface (Manual)

1. Navigate to: https://github.com/kozto/devops-capstone-project/issues
2. Click **"New Issue"**
3. Select the **"User Story"** template if available
4. Open `user_stories.md` in this directory
5. Copy the content of each user story (one at a time)
6. Paste into the issue form
7. Add the label **"user story"**
8. Click **"Submit new issue"**
9. Repeat for all seven stories

### Method 2: Using GitHub CLI (Automated with Bash)

**Prerequisites:**
- GitHub CLI (`gh`) must be installed
- You must be authenticated: `gh auth login`
- You must have write access to the repository

**Steps:**
```bash
# Navigate to the repository root
cd /home/runner/work/devops-capstone-project/devops-capstone-project

# Run the script
./.github/create_user_stories.sh
```

The script will create all seven issues automatically and provide links to view them.

### Method 3: Using Python Script (Automated with API)

**Prerequisites:**
- Python 3.x installed
- `requests` library: `pip install requests`
- GitHub Personal Access Token with `repo` scope
  - Create one at: https://github.com/settings/tokens

**Steps:**
```bash
# Set your GitHub token as an environment variable
export GITHUB_TOKEN=your_personal_access_token_here

# Navigate to the repository root
cd /home/runner/work/devops-capstone-project/devops-capstone-project

# Run the script
python3 ./.github/create_user_stories.py
```

The script will create all seven issues and show the results.

## After Creating the Issues

Once the issues are created, they will appear in the repository's Issues tab:
- URL: https://github.com/kozto/devops-capstone-project/issues

### Setting Up the Kanban Board

1. Navigate to the **Projects** tab in your repository
2. Create a new Project (if one doesn't exist)
3. Choose the **"Board"** layout
4. Add columns such as:
   - **New Issues** (or "To Do")
   - **In Progress**
   - **Done**
5. Add the newly created issues to the project
6. They will initially appear in the **"New Issues"** column

### Organizing Your Issues

- All issues are labeled with **"user story"** for easy filtering
- You can add additional labels like:
  - `enhancement`
  - `documentation`
  - `infrastructure`
  - `priority: high/medium/low`
- Assign issues to team members as work progresses
- Move issues between columns as work progresses

## User Story Format

Each user story follows the standard format:

```
**As a** [role]  
**I need** [function]  
**So that** [benefit]  
      
### Details and Assumptions
* [documented assumptions]

### Acceptance Criteria     
```gherkin 
Given [some context]
When [certain action is taken]
Then [the outcome of action is observed]
```
```

This format ensures clarity and testability for each story.

## Troubleshooting

### GitHub CLI Issues
- **Not authenticated?** Run: `gh auth login`
- **Permission denied?** Ensure you have write access to the repository
- **Command not found?** Install GitHub CLI: https://cli.github.com/

### Python Script Issues
- **Module not found?** Install requests: `pip install requests`
- **Authentication failed?** Check your GitHub token and permissions
- **Token not set?** Run: `export GITHUB_TOKEN=your_token`

### General Issues
- Verify you're in the correct repository
- Check your internet connection
- Ensure the repository exists and you have access

## Next Steps

After creating the user stories:

1. Review all issues in the GitHub Issues tab
2. Set up or add issues to your GitHub Project board
3. Prioritize the issues (suggest working in the order listed)
4. Assign team members to specific stories
5. Begin implementation following Test-Driven Development practices

## Support

If you encounter issues with these scripts or need assistance:
- Check the repository's main README.md for project documentation
- Review GitHub's documentation on Issues and Projects
- Consult the Coursera Capstone project instructions

---

**Note:** These user stories are designed to guide the implementation of the DevOps Capstone Project. Follow TDD practices: write tests first, then implement the code to make them pass.
