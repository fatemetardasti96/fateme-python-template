from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello {{cookiecutter.greeting_recipient}}!"}

