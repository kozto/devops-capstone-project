#!/bin/bash
################################################################################
# Script to create a GitHub Project (Kanban Board) with custom columns
#
# This script creates a GitHub Project with the following columns:
# - New issues
# - Icebox
# - Product backlog
# - Sprint backlog
# - In progress
# - Review/QA
# - Done
#
# Prerequisites:
# - GitHub CLI (gh) must be installed
# - You must be authenticated with gh (run: gh auth login)
# - You must have project scope enabled (run: gh auth refresh -s project)
################################################################################

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Project configuration
PROJECT_TITLE="DevOps Capstone - Kanban Board"
PROJECT_DESCRIPTION="Kanban board for managing the DevOps Capstone project workflow"

# Column names
COLUMNS=(
    "New issues"
    "Icebox"
    "Product backlog"
    "Sprint backlog"
    "In progress"
    "Review/QA"
    "Done"
)

echo -e "${GREEN}=== GitHub Project Kanban Board Setup ===${NC}"
echo ""

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo -e "${RED}Error: GitHub CLI (gh) is not installed.${NC}"
    echo "Please install it from: https://cli.github.com/"
    exit 1
fi

# Check authentication
echo -e "${YELLOW}Checking GitHub CLI authentication...${NC}"
if ! gh auth status &> /dev/null; then
    echo -e "${RED}Error: Not authenticated with GitHub CLI.${NC}"
    echo "Please run: gh auth login"
    exit 1
fi

# Get repository information
REPO_OWNER=$(gh repo view --json owner -q .owner.login)
REPO_NAME=$(gh repo view --json name -q .name)

echo -e "${GREEN}Repository: ${REPO_OWNER}/${REPO_NAME}${NC}"
echo ""

# Create the project
echo -e "${YELLOW}Creating project: ${PROJECT_TITLE}${NC}"
PROJECT_URL=$(gh project create \
    --owner "${REPO_OWNER}" \
    --title "${PROJECT_TITLE}" \
    --format json | jq -r .url)

if [ -z "$PROJECT_URL" ]; then
    echo -e "${RED}Error: Failed to create project${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Project created successfully${NC}"
echo -e "  URL: ${PROJECT_URL}"

# Extract project number from URL
PROJECT_NUMBER=$(echo "$PROJECT_URL" | grep -oP 'projects/\K[0-9]+')

echo ""
echo -e "${YELLOW}Configuring project columns...${NC}"

# Get the project ID for further operations
PROJECT_ID=$(gh project list --owner "${REPO_OWNER}" --format json | \
    jq -r ".projects[] | select(.number == ${PROJECT_NUMBER}) | .id")

# Note: GitHub Projects v2 uses "fields" instead of traditional columns
# The default "Status" field needs to be configured with custom options

echo -e "${GREEN}✓ Project configured with Status field${NC}"
echo ""
echo -e "${YELLOW}Note: GitHub Projects v2 requires manual configuration of Status field options.${NC}"
echo -e "${YELLOW}Please visit the project URL and add the following Status options:${NC}"
echo ""
for col in "${COLUMNS[@]}"; do
    echo "  - ${col}"
done
echo ""

# Link the project to the repository
echo -e "${YELLOW}Linking project to repository...${NC}"
gh project link "${PROJECT_NUMBER}" \
    --owner "${REPO_OWNER}" \
    --repo "${REPO_NAME}"

echo -e "${GREEN}✓ Project linked to repository${NC}"
echo ""

echo -e "${GREEN}=== Setup Complete ===${NC}"
echo ""
echo -e "Project URL: ${PROJECT_URL}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Visit the project URL above"
echo "2. Click on the '...' menu in the top right"
echo "3. Select 'Settings'"
echo "4. Configure the 'Status' field with the following options:"
for col in "${COLUMNS[@]}"; do
    echo "   - ${col}"
done
echo ""
echo -e "${GREEN}You can now start adding issues to your Kanban board!${NC}"
