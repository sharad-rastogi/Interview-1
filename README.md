# Accelirate Playwright Automation Framework

## Project Overview

This project is a UI automation framework developed using **Python, Playwright, and Pytest** to automate end-to-end test scenarios for the SauceDemo application.

The framework follows the **Page Object Model (POM)** design pattern and supports reusable page classes, data-driven testing, parallel execution, and automated test reporting.

**Application:** https://www.saucedemo.com/

## Tech Stack

- Python 3.11
- Playwright
- Pytest
- Pytest-xdist
- Pytest-HTML
- Allure Reports
- Page Object Model (POM)
- Git and GitHub
- Azure Pipelines

## Project Structure

```text
Accelirate-Playwright-Automation/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_sorting.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── sample-reports/
│   ├── report.html
│   └── junit-results.xml
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── azure-pipelines.yml
├── .gitignore
└── README.md
```

## Automated Test Scenarios

### 1. Login Tests
- Verify successful login with valid credentials.
- Verify login failure for locked-out users.
- Validate empty username and password fields.
- Verify appropriate validation messages.

### 2. Product Sorting
- Verify products are sorted by price (Low to High).
- Verify products are sorted by name (Z to A).

### 3. Shopping Cart
- Add multiple products to the cart.
- Verify cart badge count and product details.
- Remove a product from the cart.
- Verify cart state after returning to the inventory page.

### 4. Checkout
- Complete an end-to-end checkout flow.
- Verify selected products in the cart.
- Validate item subtotal, tax, and final total.
- Verify checkout form validation for missing first name, last name, and postal code.
- Verify successful order completion.

## Framework Design

### Page Object Model

The framework uses POM to separate page locators and page actions from test cases.

Each page class maintains its own locators and reusable methods. This improves maintainability and reduces code duplication.

### Pytest Fixtures

The `conftest.py` file contains reusable fixtures for page objects, application configuration, and authentication state.

### Authentication Reuse

A session-scoped fixture performs login and saves the browser storage state. Other tests reuse this authenticated state, while login tests use the `no_auth` marker to start without an authenticated session.

### Parallel Execution

Pytest-xdist is used to execute tests in parallel across multiple workers.

### Failure Artifacts

Playwright pytest options are configured to retain screenshots, videos, and traces for failed tests.

## Prerequisites

- Python 3.11
- Git
- pip

## Installation

Clone the repository:

```bash
git clone https://github.com/theterushikesh92-stack/Accelirate-Playwright-Automation.git
```

Navigate to the project directory:

```bash
cd Accelirate-Playwright-Automation
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Install Playwright Chromium:

```bash
python -m playwright install chromium
```

## Test Execution

Run all tests:

```bash
python -m pytest
```

Run tests in parallel:

```bash
python -m pytest -n 2
```

Run a specific test file:

```bash
python -m pytest tests/test_login.py
```

Generate HTML and JUnit reports:

```bash
python -m pytest -n 2 --html=reports/report.html --self-contained-html --junitxml=reports/junit-results.xml
```

## Test Reports

The framework generates:

- **HTML Report:** Provides a detailed visual summary of test execution.
- **JUnit XML Report:** Provides machine-readable test results for CI/CD integration.
- **Failure Artifacts:** Screenshots, videos, and traces retained for failed tests.

Sample reports are available in the `sample-reports/` directory.

## CI/CD Integration

The project includes an `azure-pipelines.yml` configuration for Azure Pipelines.

The pipeline is designed to:

1. Set up the Python environment.
2. Install project dependencies and Playwright browsers.
3. Execute tests using parallel workers.
4. Publish JUnit test results.
5. Publish HTML reports and failure artifacts.

## Repository

GitHub: https://github.com/theterushikesh92-stack/Accelirate-Playwright-Automation

## Author
Rushikesh Thete