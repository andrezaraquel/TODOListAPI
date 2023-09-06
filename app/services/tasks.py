from app import db
from flask import request
from ..models.tasks import Tasks, task_schema, tasks_schema

def add_task(current_user_id):
    try:
        title = request.json['title']
        description = request.json['description']
        status = request.json['status']
        user_id = current_user_id

        task = Tasks(title, description, status, user_id)

        db.session.add(task)
        db.session.commit()
        return task_schema.dump(task)
    except:
        return None
    
def get_task_by_id(task_id, user_id):
    try:
        task = Tasks.query.filter(Tasks.id == task_id, Tasks.user_id == user_id).one()
        return task_schema.dump(task)
    except:
        return None
    
def get_tasks_by_status(status, user_id):
    try:
        tasks =  Tasks.query.filter(Tasks.status == status, Tasks.user_id == user_id)
        return tasks_schema.dump(tasks)
    except:
        return None

def get_tasks(user_id):
    try:
        tasks =  Tasks.query.filter(Tasks.user_id == user_id)
        return tasks_schema.dump(tasks)
    except:
        return None
    
def edit_task(task_id, user_id):  
    task = Tasks.query.filter(Tasks.id == task_id, Tasks.user_id == user_id).first()
    try:
        task.title = request.json['title']
    except:
        pass        
    try:
        task.description = request.json['description']
    except:
        pass
    try:
        task.status = request.json['status']
    except:
        pass
            
    try:
        db.session.commit()
        return task_schema.dump(task)
    except:
        return None
    
def delete_task_by_id(task_id, user_id):
    try:
        task = Tasks.query.filter(Tasks.id == task_id, Tasks.user_id == user_id).first()
        db.session.delete(task)
        db.session.commit()
        return task_schema.dump(task)
    except:
        return None