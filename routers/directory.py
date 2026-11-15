from fastapi import APIRouter
from handlers.Worker_directory import WDirectory
router = APIRouter(prefix="/directory", tags=["Directory"])

@router.post("/create_directories")
def create_directories(name:str,day:int|None = None):
    WDirectory.create(name, day)

@router.delete("/delete_directories")
def delete_directories(id:int):
    WDirectory.remove(id)

@router.get("/directories")
def get_directories():
    return WDirectory.get_directories()