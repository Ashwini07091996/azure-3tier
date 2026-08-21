from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {"id": 1, "title": "Learn Azure", "completed": False},
    {"id": 2, "title": "Build 3-tier architecture", "completed": False},
    {"id": 3, "title": "Deploy application", "completed": False}
]

@app.get("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "azure-3tier-api"
    })

@app.get("/api/tasks")
def get_tasks():
    return jsonify(tasks)

@app.post("/api/tasks")
def create_task():
    data = request.get_json()

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(task)

    return jsonify(task), 201
