from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse, Response
import os
from handlers.Worker_directory import WDirectory
from handlers.Worker_file import WFile
router = APIRouter(prefix="/file", tags=["File"])

@router.post("/{id}/files/create")
def create_file(id:int,file: UploadFile = File(...)):
    WFile.write_file(id, file.filename, file.file.read())
 
@router.delete("/{id}/files/{file_id}")
def delete_file(id: int, file_id: int, Response: Response):
    WFile.delete_file(id, file_id)

@router.get("/{id}/file/{file_id}")
def get_file(directory_id: int, file_id: int):
    return FileResponse(WFile.get_file_path(directory_id, file_id), media_type='application/octet-stream',filename=WFile.get_file_name(directory_id, file_id))

@router.get("/{id}/files")
def get_files_directories(id: str):
    return WDirectory.get_file_for_directory(id)
    