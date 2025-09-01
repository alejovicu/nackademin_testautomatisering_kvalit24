
## Lab 01 Unit Testing

```shell
rm -rf .venv_test
python3 -m venv .venv_test ; pip install --upgrade pip ; source .venv_test/bin/activate


pip install -r requirements_test.txt
```

## Unit Tests
1. Run the current test

    ```shell
    pytest unit_tests.py
    ```


1. Implement the missing unit tests and run the tests again

    ```shell
    pytest unit_tests.py
    ```



# Integration Tests

## Terminal tab 1 - run API
```shell
rm -rf .venv_api
python3 -m venv .venv_api ; pip install --upgrade pip ; source .venv_api/bin/activate


pip install -r requirements_api.txt

uvicorn main:app --reload
```

## Terminal tab 2 - run integration tests

```shell
rm -rf .venv_test
python3 -m venv .venv_test ; pip install --upgrade pip ; source .venv_test/bin/activate


pip install -r requirements_test.txt
```



# Delivery of this lab
1. Create a git branch with the name `lab_01_your_name`
1. Commit the changes made in your branch to the files `unit_tests.py` and `integration_tests.py`



# FAQ

I can't push code to the repository what should I do?

1. Create a Fork of the repo in github in your github account.
1. Create the branch `lab_01_your_name` in your repo in github.
1. Send the pull request from your repo to the repo used in this class.