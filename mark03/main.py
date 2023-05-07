from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "hello world, this is the get operation from the fastAPI"}

@app.post('/')
async def post():
    return {"message": "this is the post operation from the fast api"}

@app.put('/')
async def put():
    return {"message": "hello from the put route"}

@app.get('/user')
async def list_users():
    return {"message": "list users route"}

@app.get('/users/{user_id}')
async def get_user(user_id: int ):
    return {"user_id": user_id} 

@app.get('/user/me')
async def get_current_user():
    return {"message":"This is the current user"}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return{"food_name": food_name, "message": "you are healthy"}
    
    if food_name == FoodEnum.fruits:
        return {"food_name": food_name, "message": "you are still heathy in the fruity way"}
     
    return {"food_name":food_name, "message": "I like milky bar"}