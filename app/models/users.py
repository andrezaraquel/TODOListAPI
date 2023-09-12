from app import db, ma

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(60), nullable=False)

    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name
    
    def create_user(username, pass_hash, name):
        try:       
            user = Users(username, pass_hash, name)
            db.session.add(user)
            db.session.commit()
            return user_schema.dump(user)
        except Exception as error:
            return str(error.args)

    def get_user_by_username(username):
        try:
            return Users.query.filter(Users.username == username).one()
        except Exception as error:
            return str(error.args)

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'name')

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)