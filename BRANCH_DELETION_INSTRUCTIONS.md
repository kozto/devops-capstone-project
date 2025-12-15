# Branch Deletion Instructions

## Branch to Delete

The following branch needs to be deleted from the repository:
- **Branch name**: `copilot/create-kanban-board`

## How to Delete the Branch

### Option 1: Using GitHub Web Interface (Recommended)

1. Go to the repository: https://github.com/kozto/devops-capstone-project
2. Click on "Branches" (usually under the Code tab)
3. Find the branch `copilot/create-kanban-board`
4. Click the trash/delete icon next to the branch name
5. Confirm the deletion

### Option 2: Using Git Command Line

If you have write access to the repository, you can delete the remote branch using:

```bash
git push origin --delete copilot/create-kanban-board
```

## Verification

After deletion, you can verify the branch is removed by checking:

```bash
git ls-remote --heads origin | grep copilot/create-kanban-board
```

This command should return no results if the branch was successfully deleted.

## Why This Manual Step is Needed

The automated agent environment has security restrictions that prevent it from:
- Deleting remote branches
- Pushing to branches other than the current working branch
- Modifying repository settings or branches outside the PR workflow

This is a security feature to ensure automated agents cannot accidentally delete important branches or make unauthorized changes to the repository.
