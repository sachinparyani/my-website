from flask import Flask, redirect, render_template, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1c53e01a166d84f5851deef9f898b7e5'

posts = [
    {
        'author': 'Sachin Paryani',
        'title': 'Hiking the Granite Mountain',
        'content': 'It was a beautiful hike on a bright and sunny day. Details coming soon...',
        'date_posted': 'September 20, 2019'
    },
    {
        'author': 'Sachin Paryani',
        'title': 'Creating and using Azure Machine Learning Datasets',
        'content': ('Data and Machine Learning are probably the two biggest buzzwords of the technology industry today. '
        'Details coming soon...'),
        'date_posted': 'September 10, 2019'
    }
]

@app.route("/")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/home")
def home():
    return redirect("/") 

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Sign Up', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', category='success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)