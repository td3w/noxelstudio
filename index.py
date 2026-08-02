import os
import random
import requests
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'noxel_studio_secret_key_change_me')

RESEND_API_KEY = os.getenv('RESEND_API_KEY')

KV_REST_API_URL = os.getenv('KV_REST_API_URL')
KV_REST_API_TOKEN = os.getenv('KV_REST_API_TOKEN')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, email):
        self.id = str(id)
        self.email = email

    @staticmethod
    def get(user_id):
        if not KV_REST_API_URL or not KV_REST_API_TOKEN:
            return User(user_id, session.get('user_email', 'creator@noxelstudio.dev'))
        headers = {"Authorization": f"Bearer {KV_REST_API_TOKEN}"}
        res = requests.get(f"{KV_REST_API_URL}/get/user:{user_id}", headers=headers)
        data = res.json().get('result')
        if data:
            return User(user_id, data)
        return None

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

PRODUCTS = [
    {
        "id": "01",
        "name": "Starter Pack",
        "subtitle": "Essential clean backgrounds to refresh your daily setup.",
        "price": "2.99",
        "quality": "HD Quality Files",
        "included": [
            "2x Desktop Wallpapers (16:9 / Ultrawide ready)",
            "2x Mobile Wallpapers (Optimized for iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Crisp Standard HD Quality Files"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_1"
    },
    {
        "id": "02",
        "name": "Pro Creator Pack",
        "subtitle": "Optimized ultrawide setups for professional creators.",
        "price": "3.99",
        "quality": "HD Quality Files",
        "included": [
            "4x Desktop Wallpapers (16:9 / Ultrawide ready)",
            "4x Mobile Wallpapers (Optimized for iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Dual-Monitor Matching Sets in HD"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_2"
    },
    {
        "id": "03",
        "name": "Studio Collection",
        "subtitle": "Complete aesthetic designer archive for immersive setups.",
        "price": "5.99",
        "quality": "4K Ultra HD Files",
        "included": [
            "7x Desktop Wallpapers (16:9 / Ultrawide ready)",
            "7x Mobile Wallpapers (Optimized for iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "Exclusive Minimalist Light & Dark Mode in 4K"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_3"
    },
    {
        "id": "04",
        "name": "Ultimate Mega Bundle",
        "subtitle": "All current & future releases in one master package.",
        "price": "7.99",
        "quality": "4K Ultra HD Files",
        "included": [
            "16x Desktop Wallpapers (16:9 / Ultrawide ready)",
            "16x Mobile Wallpapers (Optimized for iPhone & Android)",
            "Instant digital download (.zip archive)",
            "Lifetime access to future updates",
            "VIP Community Access & All Future Drops in 4K"
        ],
        "stripe_link": "https://buy.stripe.com/your_link_4"
    }
]

def render_page(template_name, **context):
    try:
        return render_template(template_name, **context)
    except Exception:
        if template_name.lower() != template_name:
            return render_template(template_name.lower(), **context)
        elif template_name.capitalize() != template_name:
            return render_template(template_name.capitalize(), **context)
        raise

@app.route('/')
def index():
    return render_page('Index.html', products=PRODUCTS)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            flash('Please enter a valid email address.')
            return render_page('login.html')
        
        code = f"{random.randint(100000, 999999)}"
        session['email_for_code'] = email
        session['expected_code'] = code

        # Always print code to logs so you never get locked out if domain verification is pending
        print(f"\n==============================\nDEBUG VERIFICATION CODE FOR {email}: {code}\n==============================\n")

        try:
            headers = {
                "Authorization": f"Bearer {RESEND_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "from": "Noxel Studio <support@noxelstudio.dev>",
                "to": [email],
                "subject": "Your Noxel Studio Sign-In Code",
                "text": f"Your verification code is: {code}"
            }
            res = requests.post("https://api.resend.com/emails", json=payload, headers=headers, timeout=8)
            print(f"Resend API Response Status: {res.status_code}, Body: {res.text}")
        except Exception as e:
            print(f"Resend API exception: {e}")

        flash(f'Verification code generated successfully for {email}!')
        return redirect(url_for('verify'))
    return render_page('login.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    email = session.get('email_for_code')
    expected_code = session.get('expected_code')
    
    if not email or not expected_code:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        entered_code = request.form.get('code')
        
        if entered_code == expected_code:
            user_id = abs(hash(email)) % (10 ** 8)
            session['user_email'] = email
            user = User(user_id, email)
            if KV_REST_API_URL and KV_REST_API_TOKEN:
                headers = {"Authorization": f"Bearer {KV_REST_API_TOKEN}"}
                requests.get(f"{KV_REST_API_URL}/get/user:{user_id}", headers=headers)
            login_user(user)
            session.pop('email_for_code', None)
            session.pop('expected_code', None)
            return redirect(url_for('index'))
        else:
            flash('Invalid verification code. Please check your inbox or server logs and try again.')
            
    return render_page('verify.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('user_email', None)
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
