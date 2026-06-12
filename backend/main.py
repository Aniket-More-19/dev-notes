from fastapi import FastAPI

app = FastAPI()

todos = [
    {
        "id": 1,
        "todo": "Go to GYM",
        "completed": False,
        "priority": "medium",
        "created_at": "2026-06-01T12:00:00Z",
        "updated_at": "2026-06-01T12:00:00Z",
    },
    {
        "id": 2,
        "todo": "Learn CI/CD",
        "completed": False,
        "priority": "high",
        "created_at": "2026-06-01T12:00:00Z",
        "updated_at": "2026-06-01T12:00:00Z",
    },
    {
        "id": 3,
        "todo": "Go to market",
        "completed": False,
        "priority": "low",
        "created_at": "2026-06-01T12:00:00Z",
        "updated_at": "2026-06-01T12:00:00Z",
    },
]

@app.get("/")
async def getAllTodos():
    return {"todos": todos}

@app.get("/{id}")
async def getTodoById(id: int):
    for todo in todos:
        if todo["id"] == id:
            return todo
    return {"error": "Todo not found"}

@app.post("/createTodo")
async def createTodo(todo: dict):
    todos.append({
        "id": len(todos) + 1,
        "todo": todo["todo"],
        "completed": todo["completed"],
        "priority": todo["priority"],
        "created_at": todo["created_at"],
        "updated_at": todo["updated_at"],
    })

@app.put("/updateTodo/")
async def updateTodo(id: int, updatedTodo: dict):
    for todo in todos:
        if todo["id"] == id:
            todo["todo"]=updatedTodo["todo"]
            todo["completed"]=updatedTodo["completed"]
            todo["priority"]=updatedTodo["priority"]
            todo["created_at"]=updatedTodo["created_at"]
            todo["updated_at"]=updatedTodo["updated_at"]
            break

@app.delete("/deleteTodo/{id}")
async def deleteTodo(id: int):
    for todo in todos:
        if todo["id"] == id:
            todos.pop(todos.index(todo))
            return {"message": "Todo deleted successfully"}