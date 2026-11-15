from fastapi import FastAPI
from handlers.Worker_shedule import WShendule
from routers import directory, file

app = FastAPI()
shedule = WShendule()
app.include_router(directory.router)
app.include_router(file.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)