from flask import Flask, request, jsonify

'''
Create an instance of the Flask class. 
The first argument is the name of the application’s module or package.
'''

app = Flask(__name__)

@app.route("/")
def predict():
    return "Hai Welcome to MLOps End to End"
@app.route("/predict")
def index():
    return "welcome to the index page"


if __name__ == '__main__':
    app.run(debug=True) 
# debug=True enables the debug mode, which provides detailed error messages and automatically reloads the server when code changes are detected. 
# #This is useful during development but should be turned off in production for security reasons.

