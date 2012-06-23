from flask import Flask,render_template,Markup,request,redirect,url_for
from random import shuffle

app = Flask(__name__)

app.progvars={}
app.filenames=['jsuc5P',\
               'kgLUha2',\
               'kQYPf7',\
               'lSFaDi',\
               'mTdR8a']
app.num=0

@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        app.order=range(0,5)
        shuffle(app.order)
        print app.order
        return render_template('userinfo.html')
    else:
        app.progvars['name'] = request.form['name']
        app.progvars['age'] = request.form['age']
        return redirect(url_for('main'))

@app.route('/main')
def main():
    print app.order
    if app.num == len(app.filenames): return render_template('end.html')
    app.num += 1
    return redirect(url_for('item'))
    
@app.route('/item',methods=['GET'])
def item():
    print 'this is a get item'
    print 'file is: ', app.filenames[app.num-1]
    return render_template('layout.html',num=app.num,filename=app.filenames[app.num-1]+'.mp3')

@app.route('/item',methods=['POST'])
def item2():
    print 'this is a post item'
    recog = request.form['recog']
    comp = request.form['comp']
    comp_conf = request.form['comp_conf']
    piece = request.form['piece']
    piece_conf = request.form['piece_conf']
    name = app.progvars['name']
    age = app.progvars['age']
    
    f=open('data_%s_%s.txt'%(name,age),'a')
    f.write('recog: %s \n'%(recog))
    f.write('composer: %s \n'%(comp))
    f.write('confidence: %s \n'%(comp_conf))
    f.write('piece: %s \n'%(piece))
    f.write('confidence: %s \n'%(piece_conf))
    f.close()

    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
