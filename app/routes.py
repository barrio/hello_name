from flask import render_template, redirect, session, url_for

from app import app
from app.forms import UserForm


@app.route('/', methods=['GET', 'POST'])
def index():
    userform = UserForm()

    if userform.validate_on_submit():
        session['email'] = userform.email.data
        return redirect(url_for('index'))

    return render_template(
        'index.html', userform=userform, email=session.get('email')
    )

