# Dot-test

This project contains automated tests for registration processes, presumably for the Knowlee platform. While no formal description was provided, this README aims to provide a comprehensive overview of the project based on its structure and contents.

## Key Features & Benefits

*   **Automated Testing:** This project automates the testing of registration flows, ensuring consistent and reliable validation.
*   **Configuration-Driven:** Uses a `config.py` file to manage environment-specific settings.
*   **Page Object Model:** Employs the Page Object Model (POM) for better test maintainability and reusability.
*   **Random Data Generation:** Includes generators for creating random email addresses and NIP numbers.

## Prerequisites & Dependencies

Before running these tests, ensure you have the following installed:

*   **Python 3.6+:**  This project is written in Python.
*   **pip:**  Python's package installer.
*   **Selenium:** For browser automation.
*   **WebDriverManager:** For managing browser drivers.
*   **pytest:**  A testing framework.

You can install the necessary dependencies using `pip`:

```bash
pip install selenium pytest webdriver-manager
```

## Installation & Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/wichni/Dot-test.git
    cd Dot-test
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt # If a requirements.txt file exists. Otherwise, install manually the packages specified above.
    ```

4.  **Configure `config.py`:**
    Modify the `config.py` file to match your testing environment.  Specifically, update the `BASE_URL`, `EMAIL`, `PASSWORD`, `EMAIL_ADMIN`, and `PASSWORD_ADMIN` variables.

    ```python
    BASE_URL = "https://beta.knowlee.edu.pl"
    EMAIL = "johnsenior12345678@gmail.com"
    PASSWORD = "12345678"
    EMAIL_ADMIN ="admin1@knowlee.edu.pl"
    PASSWORD_ADMIN = "givqom-vusry8-Ribrud"
    ```

## Usage Examples

To run the tests, use the `pytest` command:

```bash
pytest
```

You can also specify a particular test file or test function:

```bash
pytest test_example.py
pytest test_example.py::test_function
```

## Configuration Options

The following variables can be configured in `config.py`:

| Variable        | Description                               | Default Value                      |
| --------------- | ----------------------------------------- | ---------------------------------- |
| `BASE_URL`      | The base URL of the application.          | `https://beta.knowlee.edu.pl`      |
| `EMAIL`         | Test user email.                           | `johnsenior12345678@gmail.com`     |
| `PASSWORD`      | Test user password.                        | `12345678`                         |
| `EMAIL_ADMIN`   | Admin user email.                           | `admin1@knowlee.edu.pl`            |
| `PASSWORD_ADMIN`| Admin user password.                        | `givqom-vusry8-Ribrud`            |

These variables allow you to easily adapt the tests to different environments or user accounts.

## Project Structure

```
RegistrationTests/
├── .gitignore                  # Specifies intentionally untracked files that Git should ignore
├── .idea/                      # IntelliJ IDEA project settings (not essential for running tests)
│   ├── .gitignore
│   ├── AutoTestsKnowlee.iml   # IntelliJ module settings
│   └── inspectionProfiles/    # IntelliJ code inspection profiles
│       └── profiles_settings.xml
│   ├── misc.xml               # IntelliJ miscellaneous settings
│   ├── modules.xml            # IntelliJ module management settings
│   └── vcs.xml                # IntelliJ VCS (Version Control System) settings
├── config.py                   # Configuration file for base URL and credentials
├── conftest.py                 # Pytest configuration file (fixtures, etc.)
└── generators/               # Modules for generating test data
│   ├── __init__.py             # Marks the directory as a Python package
│   ├── email_generators.py     # Functions to generate random email addresses
│   ├── nip_generators.py       # Function to generate random NIP (tax identification) numbers
│   └── password_generators.py  # Functions to generate random passwords
└── pages/                    # Page Object Model (POM) implementation
    ├── __init__.py             # Marks the directory as a Python package
    ├── admin_profile_page.py   # Page object for the admin profile page
    └── career_advisor_page.py  # Page object for the career advisor page
```


## License Information

No license was specified for this project.

## Acknowledgments

*   Selenium: For providing the foundation for browser automation.
*   WebDriverManager: For simplifying browser driver management.
*   pytest: For offering a flexible and powerful testing framework.
