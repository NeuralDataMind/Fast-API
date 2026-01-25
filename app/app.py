from fastapi import FastAPI

app = FastAPI()

text_post = {}

@app.get("/post")
def get_all_post():
    return text_post