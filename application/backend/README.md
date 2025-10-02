
## Setup local environment

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


This will deploy the backend application in the port 8000


Start the application
```shell
uvicorn main:app --reload
```

To Stop the application type `ctrl + C` in the terminal that was started.


# APIs
## 

### Don`t require token

#### Create User
```
POST /signup
{ "username": "john", "password": "1234" }
```

#### Login with User
```
POST /login
username=john&password=1234 (x-www-form-urlencoded)
```


### Requires Authorization bearer token

#### Create Product
```
POST /products
{ "name": "Laptop" }
```
#### Assign product to user
```
POST /assign/1
```


## FAQ

If the process doesn't stop, find the process and stop it manually
```shell
lsof -i :8000
kill -9 <PID>
```
