
# Accelirate Playwright Automation Framework

## Project Overview

This project is a UI automation framework developed using Python, Playwright, and Pytest to automate end-to-end test scenarios for the SauceDemo application.

The framework follows the Page Object Model (POM) design pattern and supports reusable page classes, data-driven testing, parallel execution, and automated test reporting.

**Application:** https://www.saucedemo.com/

## Tech Stack

- Python 3.11
- Playwright
- Pytest
- Pytest-xdist
- Pytest-HTML
- Allure Pytest
- Page Object Model (POM)
- Git and GitHub
- Azure Pipelines

## Project Structure

```text
Accelirate_Playwright_Automation/
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
├── reports/
│   ├── report.html
│   └── junit-results.xml
│
├── sample-reports/
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

## Framework Architecture

### Page Object Model (POM)

The framework uses the Page Object Model design pattern to separate page locators and page actions from test cases.

Each page class maintains its own locators and reusable methods.

This approach improves code reusability, maintainability, and readability.

### Pytest Fixtures

The `conftest.py` file contains reusable fixtures for browser setup and page object initialization.

Fixtures help avoid duplicate setup code and provide a consistent test execution environment.

### Data-Driven Testing

Pytest parametrization is used to execute multiple test scenarios with different input data.

This is used particularly for negative login scenarios and checkout form validation.

### Parallel Execution

Pytest-xdist is used to execute tests in parallel across multiple workers.

The framework supports parallel execution using:

```bash
python -m pytest -n 2
```

### Failure Artifacts

Playwright pytest options can be configured to capture screenshots, videos, and traces for failed tests.

These artifacts help with debugging and failure analysis.

## Prerequisites

- Python 3.11
- Git
- pip
- Visual Studio Code or PyCharm (optional)

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/theterushikesh92-stack/Accelirate-Playwright-Automation.git
```

### 2. Navigate to the Project Directory

```bash
cd Accelirate-Playwright-Automation
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Install Playwright Chromium

```bash
python -m playwright install chromium
```

## Test Execution

### Run All Tests

```bash
python -m pytest
```

### Run Tests in Parallel

```bash
python -m pytest -n 2
```

### Run a Specific Test File

```bash
python -m pytest tests/test_login.py
```

### Run Tests with HTML and JUnit Reports

```bash
python -m pytest -n 2 --html=reports/report.html --self-contained-html --junitxml=reports/junit-results.xml
```

### Run Tests with Allure Results

```bash
python -m pytest --alluredir=reports/allure-results
```

## Test Execution Results

The framework was successfully executed with parallel execution enabled.

**Latest Execution Summary:**

| Metric | Result |
|---|---:|
| Total Tests | 13 |
| Passed | 13 |
| Failed | 0 |
| Execution Workers | 2 |
| Execution Time | 15.05 seconds |
| Pass Percentage | 100% |

## Test Reports

The framework supports the following reporting options:

### HTML Report

Provides a visual summary of test execution, including passed and failed test cases.

Location:

```text
reports/report.html
```

### JUnit XML Report

Generates machine-readable test execution results that can be integrated with CI/CD tools.

Location:

```text
reports/junit-results.xml
```

### Allure Reports

Allure pytest can generate detailed test execution results.

Generate results:

```bash
python -m pytest --alluredir=reports/allure-results
```

View the report (after installing Allure Commandline):

```bash
allure serve reports/allure-results
```

## CI/CD Integration

The project includes an `azure-pipelines.yml` configuration for Azure Pipelines integration.

The pipeline configuration is intended to:

1. Set up the Python environment.
2. Install project dependencies.
3. Install Playwright browsers.
4. Execute automation test cases.
5. Publish JUnit test results.
6. Publish HTML reports and failure artifacts.

## Version Control

Git and GitHub are used for source code management.

The project is maintained in the following repository:

https://github.com/theterushikesh92-stack/Accelirate-Playwright-Automation

## Key Framework Features

- Page Object Model architecture.
- Reusable page classes and methods.
- Pytest fixtures.
- Data-driven test execution.
- Positive and negative test scenarios.
- Parallel execution using pytest-xdist.
- HTML and JUnit reporting.
- Playwright browser automation.
- CI/CD pipeline configuration.
- Git and GitHub integration.

## Author

**Rushikesh Thete**
QA Automation Engineer

