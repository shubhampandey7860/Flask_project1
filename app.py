from flask import Flask ,render_template

app = Flask(__name__)


@app.route('/Krishna/')
def Krishna():
    return  render_template('Krishna.html',name='Shubham',age=23)


@app.route('/wish/<name>')
def Wish(name):
    return f'Happy birthday to you {name}'


if __name__=='__main__':
    app.run(debug=True)
