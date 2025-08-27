## Start the APP

terminal 1 - from application/backend
```
uvicorn main:app --reload
```


terminal 2 - from application/frontend
```
uvicorn main:app --reload
```


## Prepare a virtual environment to run selenium


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

## Prepare a virtual environment to run selenium

Validate the installation and setup is properly installed with

```shell
python open_class_app.py
```



# Lab Assignment

Automate the validation of the requirement in a script called: `admin_add_product.py`

```
Given I am an admin user​

When I add a product to the catalog​

Then The product is available to be used in the app
```


Send a pull request with the script created.