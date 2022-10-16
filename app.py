from flask import Flask

app = Flask(__name__)


# print(__name__)


@app.route("/")
def hello_world():
    return "<div>" \
                "<h1 style='text-align: center'>Hello World!</h1>" \
                "<p><h2 style='text-align: center'>This is a paragraph.</h2></p>" \
                "<img src='https://media4.giphy.com/media/YRVP7mapl24G6RNkwJ/200w.gif?cid" \
                "=82a1493bqgkcaw5puwn3p2t5hqxhhb5u5otte3jqoh4zo8c7&rid=200w.gif&ct=g'" \
           "</div> "


# Different routes using the app.route
@app.route("/bye")
def bye():
    return "Bye!"


# Creating variable paths and concerting the path to a specified data type.
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<h1>Hello there {name}, you're {number} years old!</h1>"


# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello there {name}, you're {number} years old!"


# @app.route("/<name>")
# def greet(name):
#     return f"<h1>Hello there {name}, how old are you?</h1>"


if __name__ == "__main__":
    # Run the App in debug mode to auto-reload.
    app.run(debug=True)
