
## prepare each DEV and QA environment by creating each virtual environment 

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




From backend-dev path deploy the `dev` environment
```shell
uvicorn main:app --reload --port 8080 
```

In other terminal, from backend-qa deploy the `qa` environment
```shell
uvicorn main:app --reload --port 9090
```



# Lab assignment:

From a fresh state database create two admin users in Swagger

DEV:
`admin_dev  | pass_1234`

QA:
`admin_qa  | pass_5678`


Implement the validation for the requirements in postman, export it and save it as `nackademin-app.postman_collection.json` in this path.

```
Given I am an authenticated user​

When I log in into the application​

Then I should see all my products
```

```
Given I am an admin user​

When I add a product to the catalog​

Then The product is available to be used in the app
```

Create the environment in postman to run the tests towards QA environtment and save it in this path as `qa.local.postman_environment.json`

Run the tests towards DEV and QA environments using the command:

Mac
```
newman run nackademin-app.postman_collection.json -e dev.local.postman_environment.json
newman run nackademin-app.postman_collection.json -e qa.local.postman_environment.json
```

windows - powershell
```
newman run .\nackademin-app.postman_collection.json -e .\dev.local.postman_environment.json
newman run .\nackademin-app.postman_collection.json -e .\qa.local.postman_environment.json
```