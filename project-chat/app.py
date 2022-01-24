from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://omcynanoiqufct:22d0c41650903ee74e1064ff6b0548092df5270031a8078a253f710c3b831c5c@ec2-52-86-223-172.compute-1.amazonaws.com:5432/d337fvklu3195k'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api = Api(app)

CORS(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.get("/")
def index_get():
    return jsonify({
        "message" : "welcome api Reveal Sense Team"
    })  


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)  
    message = {"answer": response}
    return jsonify(message)

@app.route("/get", methods=["GET"])
def getData():
    todo_list = Todo.query.all()
    output = []
    for todo in todo_list:
        todoList = {}
        todoList['id'] = todo.id
        todoList['title'] = todo.title
        todoList['complete'] = todo.complete
        output.append(todoList)

    print(output)
    return jsonify({
        'todo': output
    }), 200

@app.route("/todo/add", methods=["POST"])
def add():
    title = request.get_json()
    new_todo = Todo(
        title = title['title'],
        complete = False
    )
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({
        "message": "Success create!"
    }), 200

@app.route("/todo/update/<int:todo_id>", methods=["PUT"])
def update(todo_id):
    title = request.get_json()
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    todo.title = title["title"]
    db.session.commit()
    return jsonify({
        "message" : "Success update"
    }), 200


@app.route("/todo/delete/<int:todo_id>", methods=["DELETE"])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return jsonify({
        "message" : "Success delete"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
    

  