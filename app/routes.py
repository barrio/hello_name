from flask import render_template, redirect, session, url_for

from app import app
from app.forms import UserForm


@app.route('/', methods=['GET', 'POST'])
def index():
    last_input = session.get('userinput')
    session['userinput'] = None

    userform = UserForm()
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

