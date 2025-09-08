# Lab 06,07,08 - Structure a Test Framework


## Prepare a virtual environment

mac
```shell
rm -rf .venv
python3 -m venv .venv ; pip install --upgrade pip ; source .venv/bin/activate


pip install -r requirements.txt


playwright install
```

windows - powershell
```shell
rmdir .\.venv\
python -m venv .venv
. .\.venv\Scripts\activate

pip install -r requirements.txt


playwright install
```



1. Complete all missing code and run the test suites with the commands:

```
pytest --browser chromium --headed --slowmo 1000 tests/e2e

pytest tests/integration
```

