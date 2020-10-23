from app import app,db
from flask import render_template, flash,redirect,url_for,request
from flask_login import login_user
from app.models.tables import User
from app.models.forms import LoginForm,ContactForm,ResgisterForm
from flask_mail import Message, Mail

mail = Mail()
mail.init_app(app)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('index.html', form=form)
    else:
      msg = Message(form.subject.data, sender='emersonsf.info@gmail.com', recipients=['emersonsf.info@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)

      return render_template('index.html', success=True)

  elif request.method == 'GET':
    return render_template('index.html', form=form)


@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/blogpostbase")
def blogpostbase():
    return render_template('blogpostbase.html')

@app.route("/blogpost")
def blogpost():
    return render_template('blogpost.html')

@app.route("/blogpost2")
def blogpost2():
    return render_template('blogpost2.html')

@app.route("/blogpost3")
def blogpost3():
    return render_template('blogpost3.html')
  
@app.route("/blogpost4")
def blogpost4():
    return render_template('blogpost4.html')
 
@app.route("/blogpost5")
def blogpost5():
    return render_template('blogpost5.html')    

@app.route("/blogpost6")
def blogpost6():
    return render_template('blogpost6.html')      

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        pwd = request.form['password']

        user = User(username, email, pwd)
        db.session.add(user)
        db.session.commit()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))        

        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html')

