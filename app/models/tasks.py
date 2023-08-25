from app import db, ma

class Tasks(db.Model):
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
    
    
class TasksSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'status', 'user_id')
        
task_schema = TasksSchema()
tasks_schema = TasksSchema(many=True)