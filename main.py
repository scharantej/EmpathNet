
# Import the necessary modules
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import bcrypt

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    profile = db.relationship('Profile', backref='user', uselist=False)

# Define the Profile model
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    interests = db.Column(db.String(255), nullable=False)
    about_me = db.Column(db.String(255), nullable=False)

# Create the database tables
db.create_all()

# Define the root route
@app.route('/')
def index():
    return render_template('index.html')

# Define the profile route
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('profile.html')

# Define the matching route
@app.route('/matching')
def matching():
    return render_template('matching.html')

# Define the chat route
@app.route('/chat')
def chat():
    return render_template('chat.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
