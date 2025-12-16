# Guide: Creating GitHub Issues for User Stories

## Summary

This pull request provides everything needed to create seven user stories as GitHub Issues for the DevOps Capstone Project. The user stories cover the complete project lifecycle from development setup to Kubernetes deployment.

## What's Included

All necessary files have been created in the `.github/` directory:

1. **user_stories.md** - Complete content for all seven user stories
2. **create_user_stories.sh** - Automated bash script (requires GitHub CLI)
3. **create_user_stories.py** - Automated Python script (requires GitHub API token)
4. **USER_STORIES_README.md** - Detailed instructions for all methods

## The Seven User Stories

1. **Setup the Development Environment** - Configure Python, PostgreSQL, and dev tools
2. **Read an Account from the Service** - Implement GET /accounts/{id}
3. **Update an Account in the Service** - Implement PUT /accounts/{id}
4. **Delete an Account from the Service** - Implement DELETE /accounts/{id}
5. **List All Accounts in the Service** - Implement GET /accounts
6. **Containerize the Microservice Using Docker** - Create Dockerfile
7. **Deploy Docker Image to Kubernetes** - Create K8s manifests and deploy

## How to Create the Issues

### Quick Start (Recommended): Using GitHub CLI

If you have GitHub CLI installed and authenticated:

```bash
# Navigate to your repository root directory
cd path/to/devops-capstone-project
./.github/create_user_stories.sh
```

This will automatically create all seven issues in about 10 seconds.

### Alternative: Using Python Script

If you prefer Python and have a GitHub token:

```bash
export GITHUB_TOKEN=your_token_here
# Navigate to your repository root directory
cd path/to/devops-capstone-project
python3 ./.github/create_user_stories.py
```

### Manual Method: Using GitHub Web Interface

1. Go to: https://github.com/kozto/devops-capstone-project/issues
2. Click "New Issue"
3. Copy content from `.github/user_stories.md` (one story at a time)
4. Paste into the issue form
5. Add label "user story"
6. Submit
7. Repeat for all seven stories

## Setting Up Your Kanban Board

After creating the issues:

1. Navigate to the **Projects** tab in your GitHub repository
2. Create a new Project or open an existing one
3. Choose **Board** layout
4. Create columns:
   - **New Issues** (or "To Do")
   - **In Progress**  
   - **Review**
   - **Done**
5. Add the seven issues to your project
6. They will initially appear in the "New Issues" pipeline

## Verifying Success

After running one of the automation scripts or manually creating issues, verify:

- ✓ Seven new issues appear at: https://github.com/kozto/devops-capstone-project/issues
- ✓ All issues are labeled with "user story"
- ✓ All issues follow the proper user story format (As a... I need... So that...)
- ✓ Each issue has Details/Assumptions and Acceptance Criteria sections
- ✓ All issues are added to your GitHub Project board
- ✓ All issues appear in the "New Issues" pipeline

## Next Steps

Once the issues are created:

1. **Review** - Ensure all issues are properly formatted
2. **Prioritize** - Order them (suggested order: 1→2→3→4→5→6→7)
3. **Assign** - Assign team members or yourself to each story
4. **Start Working** - Begin with "Setup the Development Environment"
5. **Follow TDD** - Write tests first, then implement functionality
6. **Track Progress** - Move issues across board columns as you work

## Troubleshooting

### GitHub CLI Not Working?
- Install: https://cli.github.com/
- Authenticate: `gh auth login`
- Verify: `gh auth status`

### Python Script Failing?
- Install requests: `pip install requests`
- Get token: https://github.com/settings/tokens (needs 'repo' scope)
- Set token: `export GITHUB_TOKEN=your_token`

### Permission Issues?
- Ensure you have write access to the repository
- Verify you're authenticated correctly
- Check that the repository exists and is accessible

## Additional Resources

- Full instructions: `.github/USER_STORIES_README.md`
- User story content: `.github/user_stories.md`
- Project README: `README.md`

## Why These Stories?

Each user story addresses a specific requirement from the DevOps Capstone Project:

- **Story 1** ensures your development environment is properly configured
- **Stories 2-5** implement the core CRUD operations for the Account microservice
- **Story 6** containerizes the application for consistent deployment
- **Story 7** deploys to Kubernetes for production-ready orchestration

These stories guide you through the complete DevOps lifecycle: development → testing → containerization → deployment.

---

**Ready to create the issues?** Choose one of the methods above and get started! The automated scripts make this a 10-second task.
