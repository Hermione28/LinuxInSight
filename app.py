from database import init_db
from flask import Flask, jsonify, render_template, request, redirect, session
from services.metrics_service import get_metrics

app = Flask(__name__)
app.secret_key = "secret123"   # required for login

# LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # simple login (for now)
        if username == "admin" and password == "admin":
            session['user'] = username
            return redirect('/')
        else:
            return "Invalid credentials"

    return render_template('login.html')


# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


# HOME (protected)
@app.route('/')
def home():
    if 'user' not in session:
        return redirect('/login')
    return render_template('index.html')


# METRICS API
@app.route('/metrics')
def metrics():
    if 'user' not in session:
        return jsonify({"error": "unauthorized"}), 401
    return jsonify(get_metrics())


if __name__ == "__main__":
    init_db()
    app.run(debug=True)