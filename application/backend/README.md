
## Setup local environment

```shell
rm -rf venv
python3 -m venv venv ; pip install --upgrade pip ; source venv/Scripts/activate

pip install -r requirements.txt

```


This will deploy the backend application in the port 8000


Start the application
```shell
uvicorn backend.main:app --reload
```

To Stop the application type `ctrl + C` in the terminal that was started.


# APIs can be found by using http://127.0.0.1:8000/docs (swagger)
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
