from fastapi import FastAPI, HTTPException

app = FastAPI()

jobs_data = [{
    "id": "uid1",
    "title": "Nice Job",
    "description": "super nice job"
}, {
    "id": "uid2",
    "title": "Nice Job2",
    "description": "super nice job2"
}]


@app.get("/")
def health():
    return {"health": "OK"}


@app.get("/job")
def getJobs():
    return jobs_data


@app.get("/job/{id}")
def getJob(id):
    for job in jobs_data:
        if(job["id"] == id):
            return job
    raise HTTPException(
        status_code=404, detail="Job with id " + id + " not found")
