from app import app
from flask import request

from . import auth
from ..models.tasks import Tasks as tasks_model
from ..views import tasks as tasks_view

@app.route("/tasks", methods=['POST'])
@auth.token_required
def add_task(current_user):
    try:
        title = request.json['title']
        description = request.json['description']
        status = request.json['status']
    except:
        return tasks_view.add_task_bad_request()

    result = tasks_model.add_task(title, description, status,current_user.id)
    if isinstance(result, dict):
        return tasks_view.successful_creation('task created', result)
    return tasks_view.unsuccessful_operation('unable to create task', result)

@app.route("/tasks", methods=['GET'])
@auth.token_required
def get_tasks(current_user):
    result = tasks_model.get_tasks(current_user.id)
    if isinstance(result, list):
        return tasks_view.successful_operation('success', result)
    else:
        return tasks_view.unsuccessful_operation('could not get tasks', result)

@app.route("/tasks/id/<task_id>", methods=['GET'])
def get_task_by_id(task_id):

    @auth.token_required
    def get_task(current_user):
        result = tasks_model.get_task_by_id(task_id, current_user.id)
        if isinstance(result, dict):
            return tasks_view.successful_operation('success', result)
        else:
            return tasks_view.unsuccessful_operation('could not get task', result)

    return get_task()

@app.route("/tasks/status/<status>", methods=['GET'])
def get_tasks_by_status(status):

    @auth.token_required
    def get_tasks(current_user):
        result = tasks_model.get_tasks_by_status(status, current_user.id)
        if isinstance(result, list):
            return tasks_view.successful_operation('success', result)
        else:
            return tasks_view.unsuccessful_operation('could not get tasks', result)

    return get_tasks()

@app.route("/tasks/<task_id>", methods=['PATCH'])
def edit_task_by_id(task_id):

    @auth.token_required
    def edit_task(current_user):
        title = request.json.get('title')
        description = request.json.get('description')
        status = request.json.get('status')

        result = tasks_model.edit_task(task_id, title, description, status, current_user.id)
        if not result:
            return tasks_view.unsuccessful_operation('task not found', {})
        elif isinstance(result, dict):
            return tasks_view.successful_operation('task updated', result)
        return tasks_view.unsuccessful_operation('unable to update task', result)

    return edit_task()

@app.route("/tasks/id/<task_id>", methods=['DELETE'])
def delete_task(task_id):

    @auth.token_required
    def delete_task_from_user(current_user):
        result = tasks_model.delete_task_by_id(task_id, current_user.id)
        if isinstance(result, dict):
            return tasks_view.successful_operation('task deleted', result)
        return tasks_view.unsuccessful_operation('unable to delete task', result)

    return delete_task_from_user()