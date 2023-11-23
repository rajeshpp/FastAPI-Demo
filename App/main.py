from fastapi import FastAPI
from utils.read_file import get_all_users, get_specific_user
from utils.store_users import post_user
from models.users import Users
from mangum.adapter import Mangum

app = FastAPI()
input_file = 'users.txt'
handler = Mangum(app)


@app.get("/")
async def hello():
    """Sample Startup Function"""
    return {"Hello": "FastAPI"}


@app.get("/users")
async def get_users():
    """Sample function to get all the users"""
    try:
        return get_all_users(input_file)
    except FileNotFoundError:
        return "No User present. First create an User."


@app.get("/users/{user}")
async def get_one_user(user):
    """Sample function to get all the users"""
    try:
        return get_specific_user(input_file, user)
    except FileNotFoundError:
        return "No User present. First create an User."
    except Exception as e:
        print(e)
        return f"Some issue while getting details of user: {user}."


@app.post("/users/")
async def create_user(user: Users):
    try:
        post_user(input_file, user.user)
        return f"User created is: {user.user}"
    except Exception as e:
        print(e)
        return "Some issue while user creation."
