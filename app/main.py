from fastapi import FastAPI

from routers import ner

app = FastAPI()


app.include_router(ner.router)


# start uvicorn server with:
# uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)