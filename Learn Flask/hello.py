from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, world!</h1>' \
            '<p> This is a paragraph</p>' \
            '<img src="https://www.catschool.co/wp-content/uploads/2023/06/orange-tabby-kitten-1024x731.png" width=200>'

@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run(debug=True)

greet()