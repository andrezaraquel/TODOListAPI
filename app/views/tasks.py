from app import db
from flask import request, jsonify
from ..models.tasks import Tasks, task_schema, tasks_schema

def add_task(current_user_id):
    title = request.json['title']
    description = request.json['description']
    status = request.json['status']
    user_id = current_user_id
    
    task = Tasks(title, description, status, user_id)

    try:
        db.session.add(task)
        db.session.commit()
        result = task_schema.dump(task)
        return jsonify({'message': 'task created', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create task', 'data': {}}), 500