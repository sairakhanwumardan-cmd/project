from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask project!"
@app.route('/about')
def about():
    return "about page"
@app.route('/contact')
def contact():
    return "contact"
if __name__ == '__main__':
    app.run(debug=True)