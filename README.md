# Playwright QA Lab

Personal QA Automation learning lab built on a local homelab environment.

## Stack

* Playwright
* TypeScript
* Python
* GitHub Actions
* Docker
* Proxmox LXC
* OrangeHRM

## Environment

The project is running inside a local homelab environment:

```txt
Proxmox
└── LXC Container
    ├── Docker
    ├── OrangeHRM
    ├── Playwright
    └── VS Code Remote SSH
```

## Project Structure

```txt
playwright-qa-lab/
├── python-playwright/
│   └── tests/
│       └── test_smoke.py
│
├── ts-playwright/
│   ├── .github/workflows/
│   ├── tests/
│   │   └── smoke.spec.ts
│   ├── playwright.config.ts
│   └── package.json
│
└── README.md
```

## Current Test Coverage

### Smoke Tests

* Verify application availability
* Verify homepage opens correctly
* Verify URL and page title

## Local Application

Tests are executed against a local OrangeHRM instance running in Docker.

## CI/CD

GitHub Actions pipeline is configured for automated Playwright test execution.

## Goals

* Learn Playwright automation
* Practice TypeScript and Python automation
* Understand CI/CD workflows
* Practice API and SQL testing
* Build a realistic QA Automation lab

## Learning Notes

This repository is primarily focused on:

* practical automation skills
* debugging and troubleshooting
* locator strategies
* stable test design
* understanding Playwright concepts
* QA engineering workflows

## Status

Work in progress 🚀
