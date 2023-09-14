from flask import Flask

app = Flask(__name__)  # dunderscore


@app.route("/")
def hello():
    return "Hello, World!"


app.run(debug=True)
# pip install Flask
# python3 -m pip install Flask
