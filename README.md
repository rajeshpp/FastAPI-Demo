# FastAPI Basics

### Install FastAPI
> pip install fastapi[all]

### Basic App
Save with the name `main.py`
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    """Sample Startup Function"""
    return "Hello FastAPI"

```
### Start App
> uvicorn main:app

<img src="./images/basic_app.png" alt="basic_app" width="500" height="500"/>

### Get Users, when no users present
<img src="./images/get_no_users.png" alt="get_no_users" width="500" height="500"/>

### Get Users, when users present
<img src="./images/get_all_users.png" alt="get_all_users" width="500" height="500"/>

### Get Specific User
<img src="./images/get_specific_user.png" alt="get_specific_user" width="500" height="500"/>

### Create User
<img src="./images/create_user.png" alt="create_user" width="500" height="500"/>
