from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World Sucker!</h1>"

@app.route("/about")
def about():
    return "sucker motherfucker"

if __name__=='__main__':
    app.run(debug=True)

#set FLASK_APP=flask_blog.py
#set FLASK_DEBUG=1
