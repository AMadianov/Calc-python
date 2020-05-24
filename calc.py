from flask import Flask, request, redirect
from app.math import Parser
from flask.templating import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        expression = request.form['expression']
        result = Parser(str(expression)).calc()
        return str(result)

@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)