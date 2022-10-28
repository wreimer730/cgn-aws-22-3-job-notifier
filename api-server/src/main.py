from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health():
    return {"health": "OK"}


@app.get("/job")
def getJobs():
    return [{
        "id": "uid1",
        "title": "Nice Job",
        "description": "super nice job"
    }, {
        "id": "uid2",
        "title": "Nice Job2",
        "description": "super nice job2"
    }]
