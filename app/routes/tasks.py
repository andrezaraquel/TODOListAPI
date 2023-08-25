from app import app
from flask import jsonify
from ..views import tasks, helper

@app.route("/tasks", methods=['POST'])
@helper.token_required
def add_task(current_user):
    return tasks.add_task(current_user.id)