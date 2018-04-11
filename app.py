from flask import Flask, render_template,request
import model

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>Michigan Sports Info!</h1>
        <ul>
            <li><a href="/bball"> Men's Basketball </a></li>
             <li><a href="/fball"> Men's Foottball </a></li>
        </ul>
    '''


@app.route('/bball', methods=['GET', 'POST'])
def bball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_bball_seasons(sortby, sortorder)
    else:
        seasons = model.get_bball_seasons()

    return render_template("seasons.html", seasons=seasons)


@app.route('/fball', methods=['GET', 'POST'])
def fball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        fseasons = model.get_fball_seasons(sortby, sortorder)
    else:
        fseasons = model.get_fball_seasons()

    return render_template("fseasons.html", fseasons=fseasons)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
    else:
        fistname = ''
        lastername=''

    return render_template("hello.html")


if __name__ == '__main__':
    model.init_bball()
    app.run(debug=True)
