from app import app
from flask import request, jsonify

from . import auth
from ..views import tasks

@app.route("/tasks", methods=['POST'])
@auth.token_required
def add_task(current_user):
    task = tasks.add_task(current_user.id)
    if task:
        return jsonify({'message': 'task created', 'data': task}), 201
    return jsonify({'message': 'unable to create task', 'data': {}}), 401

@app.route("/tasks", methods=['GET'])
@auth.token_required
def get_tasks(current_user):
    tasks_list = tasks.get_tasks(current_user.id)
    if tasks_list:
        return jsonify({'message': 'success', 'data': tasks_list}), 200
    else: 
        return jsonify({'message': 'could not get tasks', 'data': {}}), 401

@app.route("/tasks/id/<task_id>", methods=['GET'])
def get_task_by_id(task_id):

    @auth.token_required
    def get_task(current_user):
        task = tasks.get_task_by_id(task_id, current_user.id)
        if task:
            return jsonify({'message': 'success', 'data': task}), 200
        else: 
            return jsonify({'message': 'could not get task', 'data': {}}), 401

    return get_task()

@app.route("/tasks/status/<status>", methods=['GET'])
def get_tasks_by_status(status):

    @auth.token_required
    def get_tasks(current_user):
        tasks_list = tasks.get_tasks_by_status(status, current_user.id)
        if tasks_list:
            return jsonify({'message': 'success', 'data': tasks_list}), 200
        else: 
            return jsonify({'message': 'could not get tasks', 'data': {}}), 401

    return get_tasks()

@app.route("/tasks/<task_id>", methods=['PATCH'])
def edit_task_by_id(task_id):

    @auth.token_required
    def edit_task(current_user):
        task = tasks.edit_task(task_id, current_user.id)
        if task:
            return jsonify({'message': 'task updated', 'data': task}), 200
        return jsonify({'message': 'unable to update task', 'data': {}}), 401

    return edit_task()

@app.route("/tasks/id/<task_id>", methods=['DELETE'])
def delete_task(task_id):

    @auth.token_required
    def delete_task_from_user(current_user):
        task = tasks.delete_task_by_id(task_id, current_user.id)
        if task:
            return jsonify({'message': 'task deleted', 'data': task}), 200
        return jsonify({'message': 'unable to delete task', 'data': {}}), 401

    return delete_task_from_user()