from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def base_get_route():
    return {"message": "hello world, this is the get operation from the fastAPI"}

@app.post('/', description= "this is the second route")
async def base_post():
    return {"message": "this is the post operation from the fast api"}

@app.put('/{id}')
async def put():
    return {"message": "hello from the put route"}