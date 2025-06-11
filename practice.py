from flask import Flask,request,render_template
app = Flask(__name__)
#@app.route('/')
#def home():
#    return "hello world"

@app.route('/')
def records():
    records=[
          {"title":"Harry potter","author":"JK Rowling","read":"no"},
          {"title": "The art of being alone", "author": "Renuka", "read": "yes"},
          {"title": "Gitanjali", "author": "Rabindranath Tagore", "read": "yes"}
    ]
    return render_template("first.html",records=records)

@app.route('/')
def reg():
    return render_template('register.html')


if __name__ =='__main__':
    app.run(debug=True):
