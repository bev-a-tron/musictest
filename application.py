from flask import Flask,render_template,Markup,request,redirect,url_for
from random import shuffle
import sqlite3

app = Flask(__name__)

app.progvars={}
app.filenames=['jsuc5P',\
              'kgLUha2',\
              'kQYPf7',\
              'lSFaDi',\
              'mTdR8a']

#configuration
app.config['DATABASE'] = '/responses.db'

def connect_db():
    print 'connect db'
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    cur = g.db.cursor()
    cur.execute('''CREATE TABLE answers
                (name text, age int, actual int, recognize text,\
                 composer text, c_confidence int, piece text,\
                 p_confidence int)''')
    cur.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        app.num=0
        app.order=range(0,5)
        shuffle(app.order)
        return render_template('userinfo.html')
    else:
        app.progvars['name'] = request.form['name']
        app.progvars['age'] = request.form['age']
        return redirect(url_for('main'))

@app.route('/main')
def main():
    if app.num == len(app.filenames): return render_template('end.html')
    app.num += 1
    return redirect(url_for('item'))
    
@app.route('/item',methods=['GET'])
def item():
    #print 'this is a get item'
    return render_template('layout.html',num=app.num,filename=app.filenames[app.order[app.num-1]]+'.mp3')

@app.route('/item',methods=['POST'])
def item2():
    #print 'this is a post item'
    
    cur.execute('insert into entries (name,age,actual,recognize,composer,c_confidence,piece,p_confidence) values (?,?,?,?,?,?,?,?)',
                 [app.progvars['name'],\
                  int(app.progvars['age']),\
                  app.order[app.num-1],\
                  request.form['recog'],\
                  request.form['comp'],\
                  int(request.form['comp_conf']),\
                  request.form['piece'],\
                  int(request.form['piece_conf'])
                  ])

    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
