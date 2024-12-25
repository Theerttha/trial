from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy as sql
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db=sql(app)

class data(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    username=db.Column(db.String(30))
    password=db.Column(db.String(100))

    def __repr__(self):
        return '<Task %r>' % self.id
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        user_name=request.form['user']
        pass_word=request.form['password']
        users=data.query.all()
        print(users)
        for i in users:
            if i.username==user_name and i.password==pass_word:
                return "yes"
    return render_template('index.html')
@app.route('/register',methods=['POST','GET'],endpoint='register')
def index():
    if request.method=='POST':
        user_reg=request.form['user_register']
        pass_word_reg=request.form['password_register']
        users=data.query.all()
        reg_exists=False
        for i in users:
            if i.username==user_reg:
                if i.password==pass_word_reg:
                    return render_template('register.html',reg_exists=True)
                else:
                    return render_template('register.html',reg_user_exists=True)
            if i.password==pass_word_reg:
                return render_template('register.html',reg_password_exists=True)
        obj=data(username=user_reg, password=pass_word_reg)
        try:
            db.create_all()
            db.session.add(obj)
            db.session.commit()
            
            return render_template('index.html')
        except:
            return "error"
    return render_template('register.html')
if __name__=="__main__":
    app.run(debug=True)