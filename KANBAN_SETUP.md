# Kanban Board Setup Guide

This guide explains how to set up a GitHub Project Kanban board for the DevOps Capstone project.

## Overview

The Kanban board will help you manage your development workflow with the following columns:

1. **New issues** - Newly created issues that haven't been triaged yet
2. **Icebox** - Ideas and features that might be implemented in the future
3. **Product backlog** - Features and work items planned for future sprints
4. **Sprint backlog** - Work items selected for the current sprint
5. **In progress** - Work currently being developed
6. **Review/QA** - Work that is complete and awaiting review or testing
7. **Done** - Completed work

## Prerequisites

Before setting up the Kanban board, ensure you have:

- GitHub CLI (`gh`) installed on your system
  - Download from: https://cli.github.com/
- Authenticated with GitHub CLI
  - Run: `gh auth login`
- Project scope enabled for your GitHub token
  - Run: `gh auth refresh -s project`

## Automated Setup (Recommended)

We provide a script to automate most of the setup process:

```bash
./bin/setup-kanban.sh
```

This script will:
1. ✓ Create a new GitHub Project
2. ✓ Link the project to your repository
3. ⚠ Provide instructions for manual column configuration

### After Running the Script

GitHub Projects v2 requires manual configuration of the Status field. Follow these steps:

1. Visit the project URL provided by the script
2. Click on the `...` (three dots) menu in the top right corner
3. Select `Settings`
4. Find the `Status` field configuration
5. Add the following options (in order):
   - New issues
   - Icebox
   - Product backlog
   - Sprint backlog
   - In progress
   - Review/QA
   - Done

## Manual Setup

If you prefer to set up the Kanban board manually or the script doesn't work:

### Step 1: Create a New Project

1. Navigate to your repository on GitHub
2. Click on the `Projects` tab
3. Click `Link a project` → `New project`
4. Choose `Board` template or start from scratch
5. Name it: "DevOps Capstone - Kanban Board"

### Step 2: Configure Columns

1. Click on the project settings (three dots menu)
2. Select `Settings`
3. Configure the `Status` field with the following options:
   - New issues
   - Icebox
   - Product backlog
   - Sprint backlog
   - In progress
   - Review/QA
   - Done

### Step 3: Link to Repository

1. In project settings, go to `Manage access`
2. Link the project to your repository

### Step 4: Set Up Automation (Optional)

Configure automation rules to automatically move items:

1. When an issue is created → Move to "New issues"
2. When a PR is opened → Move to "In progress"
3. When a PR is merged → Move to "Done"

## Using the Kanban Board

### Adding Items

- **Create a new issue**: Issues can be created directly in the project or from the repository
- **Add existing issues**: Drag and drop or use the `+` button in any column

### Moving Items

- **Drag and drop**: Simply drag items between columns
- **Context menu**: Right-click on an item to move it

### Best Practices

1. **New issues**: Triage new issues regularly to move them to appropriate columns
2. **Icebox**: Use for ideas that aren't currently planned but shouldn't be forgotten
3. **Product backlog**: Prioritize items here before each sprint
4. **Sprint backlog**: Limit work in progress - only add what can be completed in the sprint
5. **In progress**: Limit concurrent work items to maintain focus
6. **Review/QA**: Ensure timely reviews to prevent bottlenecks
7. **Done**: Archive completed items periodically to keep the board clean

## Troubleshooting

### "gh: command not found"

Install GitHub CLI:
- **macOS**: `brew install gh`
- **Ubuntu/Debian**: `sudo apt install gh`
- **Windows**: Download from https://cli.github.com/

### "Not authenticated with GitHub CLI"

Run the authentication command:
```bash
gh auth login
```

Follow the prompts to authenticate.

### "Insufficient privileges"

Ensure you have:
- Admin access to the repository
- Project scope enabled: `gh auth refresh -s project`

### Script fails to create project

Try the manual setup process described above.

## Additional Resources

- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GitHub CLI Project Commands](https://cli.github.com/manual/gh_project)
- [Agile Planning with GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects)

## Support

If you encounter issues not covered in this guide, please:
1. Check the GitHub Projects documentation
2. Review GitHub CLI documentation
3. Open an issue in this repository with details of the problem
