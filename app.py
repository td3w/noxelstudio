from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from email.message import EmailMessage
import os
import random
import sys
import smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'noxel-secure-key-2026'

if os.environ.get('VERCEL') == '1' or os.environ.get('AWS_EXECUTION_ENV'):
    db_path = '/tmp/noxel_users.db'
else:
    db_path = 'noxel_users.db'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    verification_code = db.Column(db.String(6), nullable=True)
    accepted_policy = db.Column(db.Boolean, default=False)
    marketing_opt_in = db.Column(db.Boolean, default=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def send_verification_email(target_email, code):
    try:
        msg = EmailMessage()
        msg.set_content(f"Your Noxel Studio access code is: {code}\n\nEnter this in the client portal to verify your ID.")
        msg['Subject'] = 'Noxel ID // Verification Code'
        msg['From'] = 'support@noxelstudio.dev'
        msg['To'] = target_email
        
        resend_key = os.environ.get('RESEND_API_KEY', '')
        
        server = smtplib.SMTP('smtp.resend.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('resend', resend_key)
        server.send_message(msg)
        server.quit()
        
        print(f"--> SUCCESS: Email sent to {target_email} via Resend", file=sys.stderr)
    except Exception as e:
        print(f"--> ERROR: Resend SMTP failed: {str(e)}", file=sys.stderr)
        raise e

products = [
    {"id": 1, "name": "Starter Pack", "price": "2.99", "subtitle": "Essential clean backgrounds for daily setups.", "included": ["2x Desktop Wallpapers (16:9 / Ultrawide ready)", "2x Mobile Wallpapers (Optimized for iPhone & Android)", "Instant digital download (.zip archive)"], "stripe_link": "#"},
    {"id": 2, "name": "Pro Creator Pack", "price": "3.99", "subtitle": "High-fidelity assets for optimized ultrawide setups.", "included": ["10x Desktop Wallpapers", "10x Mobile Wallpapers", "4K Resolution"], "stripe_link": "#"},
    {"id": 3, "name": "Studio Collection", "price": "5.99", "subtitle": "An immersive designer archive for multi-monitor setups.", "included": ["25x Desktop Wallpapers", "25x Mobile Wallpapers", "8K Resolution Support"], "stripe_link": "#"},
    {"id": 4, "name": "Ultimate Mega Bundle", "price": "7.99", "subtitle": "Covering all current and future releases.", "included": ["All existing collections", "Lifetime updates", "Priority support"], "stripe_link": "#"}
]

@app.route('/')
def index():
    db.create_all() 
    return render_template('index.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    db.create_all() 
    if request.method == 'POST':
        action = request.form.get('action') 
        email = request.form.get('email')
        password = request.form.get('password')

        if action == 'register':
            policy = request.form.get('policy')
            if not policy:
                flash('You must agree to the Terms & Privacy Policy to register.')
                return redirect(url_for('login'))

            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email already exists. Please log in.')
                return redirect(url_for('login'))
            
            marketing = True if request.form.get('marketing') else False
            code = str(random.randint(100000, 999999))
            
            new_user = User(
                email=email, 
                password_hash=generate_password_hash(password), 
                verification_code=code, 
                is_verified=False,
                accepted_policy=True,
                marketing_opt_in=marketing
            )
            db.session.add(new_user)
            db.session.commit()
            
            send_verification_email(email, code)
            session['verify_email'] = email
            return redirect(url_for('verify'))
        
        elif action == 'login':
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password_hash, password):
                if not user.is_verified:
                    session['verify_email'] = email
                    flash('Please verify your email address to continue.')
                    return redirect(url_for('verify'))
                
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Invalid email or password. Access Denied.')
                return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    db.create_all()
    email = session.get('verify_email')
    
    if not email:
        return redirect(url_for('login'))

    if request.method == 'POST':
        code = request.form.get('code')
        user = User.query.filter_by(email=email).first()
        
        if user and user.verification_code == code:
            user.is_verified = True
            user.verification_code = None 
            db.session.commit()
            
            login_user(user)
            session.pop('verify_email', None)
            return redirect(url_for('index'))
        else:
            flash('Invalid verification code. Please try again.')

    return render_template('verify.html', email=email)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
