# Quickbase Interview

## Initial problem

You can find initial problem description [here!](https://github.com/QuickBase/interview-demos/tree/master/python)

## How to use?

Prerequisite: Have Python installed on your machine

1. Clone the repository

    Navigate to your desired location and clone the repository:
    ```
    $ git clone https://github.com/erdemhalil/qb-interview.git
    ```
2. Create a virtual environment
    ```
    $ python3 -m venv /path/to/new/virtual/environment
    ```

    NOTE: For information, refer to [this page](https://docs.python.org/3/library/venv.html)

3. Activate venv (from Bash)
    ```
    $ source ./env/Scripts/activate
    ```

4. Install dependencies
    ```
    $ pip install requests
    ```

5. Run code and tests
    ```
    $ python main.py
    $ python -m unittest tests/test_requests.py
    ```

## Issues

- Both GitHub and Freshdesk API Tokens are hardcoded, meaning that they are vulnerable
- Unit Tests are limited, same data is used over and over again. This leads to expecting weird HTTP status codes such as 409 when creating a new contact in Freshdesk
- Program has been developed and tested on Windows 10 only, hence why the instructions are for Windows

## Notes

- If you want to use your own API Keys/Tokens, you will have to manually change the ones in main.py
- I've created trial GitHub and Freshdesk accounts for testing purposes
- As of 23/03/2022, the created Freshdesk account's trial period will expire in 20 days
- I've used `qbtest` as Freshdesk domain to test
