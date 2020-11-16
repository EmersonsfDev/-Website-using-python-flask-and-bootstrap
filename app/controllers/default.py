from app import app,db
from flask import render_template, flash,redirect,url_for,request,flash,config,abort,session
from flask_login import login_user
from app.models.forms import LoginForm,ContactForm,ResgisterForm
from flask_mail import Message, Mail
from flask_mysqldb import MySQL 
import MySQLdb.cursors 
import re 
import stripe

mail = Mail()
mail.init_app(app)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('Todos os campos são necessários.')
      return render_template('index.html', form=form)
    else:
      msg = Message(form.subject.data, sender='emersonsf.info@gmail.com', recipients=['rualthof@gmail.com '])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)

      return render_template('index.html', success=True)

  elif request.method == 'GET':
    return render_template('index.html', form=form)


@app.route("/controleProducao")
def controleProducao():
    return render_template('controleProducao.html')

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


@app.route("/blogpost7")
def blogpost7():
    return render_template('blogpost7.html') 

'''
@app.route("/projeto")
def projeto():
    return render_template('projeto.html')
@app.route("/compra")
def compra():
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price':'price_1HjRbbH7KlqUP853FKmXS2CT',
            'quantity' :1,
        }],
        mode='payment',
        success_url=url_for('index', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=url_for('compra', _external=True),
    )
    return render_template('compra.html',checkout_session_id=session['id'],checkout_public_key=app.config['STRIPE_PUBLIC_KEY'])

@app.route('/stripe_webhook', methods=['POST'])
def stripe_webhook():
    print('CHAMANDO WEBHOOK')

    if request.content_length > 1024 * 1024:
        print('PEDIDO MUITO GRANDE')
        abort(400)
    payload = request.get_data()
    sig_header = request.environ.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = 'whsec_slJhJDzKOm0h9NUJFY300kLNcDXvrMZO'
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e: 
        print('Erro no Pagamento')
        return {}, 400
    
    except stripe.error.SignatureVerificationError as e:
        print('Assinatura Inválida')
        return {}, 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items['data'][0]['description'])

    return {}

@app.route("/Planilha_20de_20Dashboard_20de_20Contas_20a_20Receber_202   ")
def Planilha_20de_20Dashboard_20de_20Contas_20a_20Receber_202   ():
    return render_template('Planilha_20de_20Dashboard_20de_20Contas_20a_20Receber_202   .html')

@app.route("/  microsoft_powerapps_canvas_edi")
def   microsoft_powerapps_canvas_edi   ():
    return render_template('microsoft_powerapps_canvas_edi.html')    

'''

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        pwd = request.form['password']
        
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM Usuario WHERE username = % s', (username, )) 
        Usuario = cursor.fetchone() 
        cursor.execute('INSERT INTO Usuario VALUES (NULL, % s, % s, % s)', (username, pwd, email, )) 
        db.connection.commit() 

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = '' 
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM Usuario WHERE email = % s AND password = % s', (email, pwd, )) 
        Usuario = cursor.fetchone() 
        if Usuario: 
            session['loggedin'] = True
            session['id'] = Usuario['codigo']
            session['username'] = Usuario['username']
    
            msg = 'Logado!'
        else: 
         msg = 'Credenciais Inválidas!'
    return render_template('login.html', msg = msg) 
  
@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")

