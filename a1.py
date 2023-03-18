from flask import *

app = Flask(__name__)

@app.route('/')
def welocme():
    return 'welcome to flask frame  work'

@app.route('/wish/<name>')
def wish(name):
    return f'my name is : {name}'


@app.route('/home')
def home():
    return render_template('krishna.html',name='shubham',age=23)
    

if __name__=='__main__':
    app.run(debug=True)