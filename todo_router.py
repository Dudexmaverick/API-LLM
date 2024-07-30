from fastapi import APIRouter
router = APIRouter
@router.post("/todos")
def create_todo():
    pass
@router.get("/todos")
def get_todo(todo_id:int):
    pass
