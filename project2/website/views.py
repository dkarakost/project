from flask import Blueprint,render_template,request,flash
from flask_login import login_required, current_user
from .models import Note,db

views = Blueprint('view',__name__) #set a blueprint for the flash application

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if note is None:
            flash('The note is missing', category='error')
        elif len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, id=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added ', category='success')
    return render_template('home.html',user=current_user)


