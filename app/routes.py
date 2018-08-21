from flask import render_template, redirect, session, url_for

from app import app
from app.forms import UserForm


@app.route('/', methods=['GET', 'POST'])
def index():
    userform = UserForm()
    last_input = session['userinput']
    session['userinput'] = None

    if userform.validate_on_submit():
        session['userinput'] = {
            'email': userform.email.data,
            'password': userform.password.data,
            'remember_me': userform.remember_me.data
        }
        return redirect(url_for('index'))

    return render_template(
        'index.html', userform=userform, userinput=last_input
    )

