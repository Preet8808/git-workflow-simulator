# Git Workflow Simulator

This project simulates a real-world Git team workflow with feature branches, pull requests, code reviews, merge conflicts, and release tagging.

## Features
- Login System Module
- Dashboard UI Module
- API Integration Module
- Git branching simulation
- PR-based workflow
- Release tagging

## Branch Strategy
- main → production
- develop → integration
- feature/* → new features

## Workflow
1. Create feature branch from develop
2. Commit changes
3. Push branch
4. Open Pull Request
5. Code review
6. Merge into develop
7. Release from main

## Version
v1.0
def load_dashboard():
    print("Dashboard Loaded")
    print("Showing user stats...")

if __name__ == "__main__": 
    load_dashboard()

def get_data():
    return {
        "status": "success",
        "data": [1, 2, 3, 4]
    }

if __name__ == "__main__":
    print(get_data())
