# Lab 04


## Prepare a virtual environment

mac
```shell
rm -rf .venv
python3 -m venv .venv ; pip install --upgrade pip ; source .venv/bin/activate


pip install -r requirements.txt

```

windows - powershell
```shell
rmdir .\.venv\
python -m venv .venv
. .\.venv\Scripts\activate

pip install -r requirements.txt

```


1. Install the browsers  `playwright install` then run the existing demo test:
    ```
    pytest --browser chromium --headed
    ```

1. Modify the file `test_product.py` and automate the requirements:

    ```
    Given I am an admin user​

    When I add a product to the catalog​

    Then The product is available to be used in the app
    ```

    ```
    Given I am an admin user​

    When I remove a product from the catalog​

    Then The product should not be listed in the app to be used
    ```
# https://playwright.dev/python/docs/locators