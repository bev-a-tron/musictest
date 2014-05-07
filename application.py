from flask import Flask,render_template,Markup,request,redirect,url_for
from random import shuffle
import sqlite3

import os

from Database import Database
from Response import Response

app = Flask(__name__)
app.debug = True

app.progvars={}
app.filenames=['jsuc5P',\
              'kgLUha2',\
              'kQYPf7',\
              'lSFaDi',\
              'mTdR8a']
#app.num_clips=len(app.filenames)
app.num_clips=2

#Setup Database and Tables
db = Database()
db.setup()

@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        app.num=0
        app.order=range(0,5)
        shuffle(app.order)
        return render_template('userinfo.html',num_clips=app.num_clips)
    else:
        app.progvars['name'] = request.form['name']
        app.progvars['age'] = request.form['age']
        return redirect(url_for('main'))

@app.route('/main')
def main():
    if app.num == app.num_clips: return render_template('end.html')
    app.num += 1
    return redirect(url_for('item'))

@app.route('/item',methods=['GET'])
def item():
    #print 'this is a get item'
    return render_template('layout.html',num=app.num,filename=app.filenames[app.order[app.num-1]]+'.mp3')

@app.route('/env', methods=['GET'])
def showEnv():
  return str(os.environ)

@app.route('/item',methods=['POST'])
def item2():
    #print 'this is a post item'
    #initialize in case no answer

    response = Response()

    response.order = app.order[app.num-1]
    response.recog = request.form['recog']
    response.comp = request.form['comp']
    response.comp_conf = request.form['comp_conf']
    response.piece = request.form['piece']
    response.piece_conf = request.form['piece_conf']
    response.name = app.progvars['name']
    response.age = app.progvars['age']

    db.saveResponse(response)

    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
