from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
class TodoCreate(BaseModel):
    title: str

class Todo(TodoCreate):
    id : int
    completed = bool = False 
todos = []
@app.post("/todos", response_model= list[Todo])
def get_todos():
    return todos 
@app.get("/todos/{todos_id}", response_model=Todo)
def get_todo(todo_id:int ):
    for todo in todos: 
       return todo
raise HTTPException(status_code=404, detail="todo not found")
@app.put("/todos/{todos_id}", response_model = todo)
def update_todo(todo_id: int, updated_todo:TodoCreate):
    for todo in todos:
        if todo.id == todo_id:
            todo.title = updated_todo.title 
            return todo 
raise HTTPException(status_code=404,detail="todo not found")
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    del todos[index]
    return {"message": "todo deleted sucessfully"}
raise HTTPException(status_code=404, detail="Todo not found ")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=3000, host="0.0.0.0", reload=True)

