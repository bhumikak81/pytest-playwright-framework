## Pytest Playwright Automation Framework

This project is an automation testing framework built using Python, Pytest, and Playwright.
It demonstrates end-to-end (E2E) UI testing capabilities with a modular and scalable test framework that can be extended for real-world applications.

## Features

1. Playwright for fast and reliable browser automation
2. Pytest for test execution and reporting
2. Fixtures for reusable setup/teardown logic
Configurable Base URL (pytest.ini or CLI options)
HTML Test Reports for execution results
Page Object Model (POM) structure for scalability
Support for headed/headless mode execution
Debugging support with page.pause() and --headed

## Tech Stack
Language: Python 3.12
Frameworks: Pytest, Playwright
Reporting: pytest-html, pytest-metadata
IDE: Visual Studio Code

## Project Structure
pytest_playwright_vscode/
│── tests/
│   └── test_login.py         # Sample login test
│
│── pages/                    # Page Object Model (POM)
│   └── login_page.py
│
│── config/
│   └── config.yaml           # Test data & environment configs
│
│── reports/                  # Test reports (HTML, screenshots)
│
│── pytest.ini                # Pytest configuration
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation
