#!/usr/bin/env python3
"""
Script to create user stories as GitHub Issues using GitHub REST API
Prerequisites: 
  - Python 3.x
  - requests library (pip install requests)
  - GitHub Personal Access Token with 'repo' scope
  - Export token as environment variable: export GITHUB_TOKEN=your_token_here
"""

import os
import sys
import json
import requests

# Configuration
REPO_OWNER = "kozto"
REPO_NAME = "devops-capstone-project"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable is not set")
    print("Please set it with: export GITHUB_TOKEN=your_token_here")
    sys.exit(1)

# GitHub API configuration
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# User Stories
user_stories = [
    {
        "title": "Setup the Development Environment",
        "body": """**As a** developer  
**I need** to set up the development environment  
**So that** I can start developing and testing the account microservice  
      
### Details and Assumptions
* Python 3.9 virtual environment needs to be configured
* PostgreSQL database should be available via Docker
* All dependencies from requirements.txt must be installed
* Development tools (linting, testing) should be configured

### Acceptance Criteria     
```gherkin 
Given the development environment is not configured
When I run the setup script
Then Python 3.9 virtual environment should be activated
And all dependencies should be installed
And PostgreSQL database should be running
And I can run tests successfully
```""",
        "labels": ["user story"]
    },
    {
        "title": "Read an Account from the Service",
        "body": """**As a** service consumer  
**I need** the ability to read an account from the service  
**So that** I can retrieve account details by account ID  
      
### Details and Assumptions
* Account must exist in the database to be retrieved
* Should return HTTP 404 if account is not found
* Should return HTTP 200 with account data if found
* Endpoint should be GET /accounts/{id}

### Acceptance Criteria     
```gherkin 
Given an account exists in the database
When I send a GET request to /accounts/{id}
Then I should receive a 200 OK status
And the response should contain the account details

Given an account does not exist
When I send a GET request to /accounts/{id}
Then I should receive a 404 NOT FOUND status
```""",
        "labels": ["user story"]
    },
    {
        "title": "Update an Account in the Service",
        "body": """**As a** service consumer  
**I need** the ability to update an account in the service  
**So that** I can modify existing account information  
      
### Details and Assumptions
* Account must exist in the database to be updated
* Should return HTTP 404 if account is not found
* Should return HTTP 200 with updated account data if successful
* Endpoint should be PUT /accounts/{id}
* Request body should contain the updated account data in JSON format

### Acceptance Criteria     
```gherkin 
Given an account exists in the database
When I send a PUT request to /accounts/{id} with valid account data
Then I should receive a 200 OK status
And the response should contain the updated account details
And the account should be updated in the database

Given an account does not exist
When I send a PUT request to /accounts/{id}
Then I should receive a 404 NOT FOUND status
```""",
        "labels": ["user story"]
    },
    {
        "title": "Delete an Account from the Service",
        "body": """**As a** service consumer  
**I need** the ability to delete an account from the service  
**So that** I can remove accounts that are no longer needed  
      
### Details and Assumptions
* Account must exist in the database to be deleted
* Should return HTTP 204 NO CONTENT on successful deletion
* Should return HTTP 404 if account is not found
* Endpoint should be DELETE /accounts/{id}

### Acceptance Criteria     
```gherkin 
Given an account exists in the database
When I send a DELETE request to /accounts/{id}
Then I should receive a 204 NO CONTENT status
And the account should be removed from the database

Given an account does not exist
When I send a DELETE request to /accounts/{id}
Then I should receive a 404 NOT FOUND status
```""",
        "labels": ["user story"]
    },
    {
        "title": "List All Accounts in the Service",
        "body": """**As a** service consumer  
**I need** the ability to list all accounts in the service  
**So that** I can see all available accounts  
      
### Details and Assumptions
* Should return an empty list if no accounts exist
* Should return HTTP 200 with a list of all accounts
* Endpoint should be GET /accounts
* Response should be a JSON array of account objects

### Acceptance Criteria     
```gherkin 
Given multiple accounts exist in the database
When I send a GET request to /accounts
Then I should receive a 200 OK status
And the response should contain a list of all accounts

Given no accounts exist in the database
When I send a GET request to /accounts
Then I should receive a 200 OK status
And the response should contain an empty list
```""",
        "labels": ["user story"]
    },
    {
        "title": "Containerize the Microservice Using Docker",
        "body": """**As a** developer  
**I need** to containerize the microservice using Docker  
**So that** I can ensure consistent deployment across different environments  
      
### Details and Assumptions
* Dockerfile should be created in the root directory
* Image should include Python 3.9 and all dependencies
* Image should expose the appropriate port for the Flask application
* PostgreSQL should be configured as a separate container
* Should be able to build and run the container locally

### Acceptance Criteria     
```gherkin 
Given a Dockerfile exists
When I build the Docker image
Then the image should be created successfully
And the image should contain all necessary dependencies

Given the Docker image is built
When I run the container
Then the service should start successfully
And I should be able to access the service endpoints
```""",
        "labels": ["user story"]
    },
    {
        "title": "Deploy Docker Image to Kubernetes",
        "body": """**As a** DevOps engineer  
**I need** to deploy the Docker image to Kubernetes  
**So that** the microservice can run in a scalable, production-ready environment  
      
### Details and Assumptions
* Kubernetes deployment manifests should be created
* Should include deployment, service, and any necessary configuration
* Deployment should reference the Docker image
* Service should expose the application to external traffic
* Should consider environment variables for database connection

### Acceptance Criteria     
```gherkin 
Given Kubernetes deployment manifests exist
When I apply the manifests to a Kubernetes cluster
Then the deployment should be created successfully
And pods should be running
And the service should be accessible

Given the service is deployed to Kubernetes
When I send a request to the service endpoint
Then I should receive a successful response
And the service should be operational
```""",
        "labels": ["user story"]
    }
]

def create_issue(story):
    """Create a GitHub issue for a user story"""
    response = requests.post(API_URL, headers=HEADERS, json=story)
    
    if response.status_code == 201:
        issue = response.json()
        print(f"✓ Created issue #{issue['number']}: {story['title']}")
        return True
    else:
        print(f"✗ Failed to create issue: {story['title']}")
        print(f"  Status: {response.status_code}")
        print(f"  Response: {response.text}")
        return False

def main():
    """Main function to create all user stories"""
    print(f"Creating user stories in repository: {REPO_OWNER}/{REPO_NAME}")
    print("=" * 60)
    
    success_count = 0
    for story in user_stories:
        if create_issue(story):
            success_count += 1
    
    print("=" * 60)
    print(f"Successfully created {success_count} out of {len(user_stories)} user stories")
    print(f"View them at: https://github.com/{REPO_OWNER}/{REPO_NAME}/issues")

if __name__ == "__main__":
    main()
