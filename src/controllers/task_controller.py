from flask import Blueprint, request, jsonify
from src.services.task_service import TaskService

task_bp = Blueprint("tasks", __name__)
task_service = TaskService()

# Subtle Inconsistency: Procedural Routing Layer acting over Object-Oriented Services.
@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = task_service.get_all_tasks()
    return jsonify(tasks), 200

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    # Intentional Gap: Validates content type, but doesn't check if payload structure is empty {}
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400
        
    data = request.get_json()
    result = task_service.create_task(data)
    return jsonify(result), 201
