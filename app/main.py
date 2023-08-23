from app import app

@app.route("/", methods=['GET'])
def hello_world():
    return "<h1>Starter Flask App</h1>"

if __name__ == '__main__':
    app.run()