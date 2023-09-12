from itsdangerous import Serializer
from app import db, ma

class Tasks(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, description, status, user_id):
        self.title = title
        self.description = description
        self.status = status
        self.user_id = user_id

    def add_task(title, description, status, user_id):
        try:
            task = Tasks(title, description, status, user_id)
            db.session.add(task)
            db.session.commit()
            return task_schema.dump(task)
        except Exception as error:
            return str(error.args)

    def get_task_by_id(task_id, user_id):
        try:
            task = Tasks.query.filter(Tasks.id == task_id, Tasks.user_id == user_id).one()
            return task_schema.dump(task)
        except Exception as error:
            return str(error.args)

    def get_tasks_by_status(status, user_id):
        try:
            tasks =  Tasks.query.filter(Tasks.status == status, Tasks.user_id == user_id)
            return tasks_schema.dump(tasks)
        except Exception as error:
            return str(error.args)

    def get_tasks(user_id):
        try:
            tasks =  Tasks.query.filter(Tasks.user_id == user_id)
            return tasks_schema.dump(tasks)
        except Exception as error:
            return str(error.args)

    def edit_task(task_id, title, description, status,  user_id):
        task = Tasks.query.filter(Tasks.id == task_id, Tasks.user_id == user_id).first()
        if not task:
            return None

        if title:
            task.title = title
        if description:
            task.description = description
        if status:
            task.status = status
        try:
            db.session.commit()
            return task_schema.dump(task)
        except Exception as error:
            return str(error.args)

    def delete_task_by_id(task_id, user_id):
        try:
            task = Tasks.query.filter(Tasks.id == task_id, Tasks.user_id == user_id).first()
            db.session.delete(task)
            db.session.commit()
            return task_schema.dump(task)
        except Exception as error:
            return str(error.args)

class TasksSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'status', 'user_id')

task_schema = TasksSchema()
tasks_schema = TasksSchema(many=True)