from flask import render_template,request,redirect, url_for,abort
from . import main
from .. import db,photos
from .forms import CommentForm,UpdateProfile, PitchForm
from ..models import Comment,User,Pitch
from flask_login import login_required, current_user
from flask_user import current_user
# Comment = comment.Comment
# Views
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'One Minute Pitch'
    pitches=Pitch.get_pitch()   
    print(pitches)
    return render_template('index.html', title = title,pitches=pitches)

@main.route('/pitch/',methods = ['GET','POST'])
@login_required
def pitch():
    form = PitchForm()
    pitch = Pitch.query.all()
    '''
    View pitch page function that returns the pitch details page and its data
    '''
    if form.validate_on_submit():
        author = form.author.data
        category = form.category.data
        body = form.body.data 

        pitch = Pitch(category=category,author=author,body=body)

        pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('pitch.html',pitch_form=form, pitches=pitch)   

@main.route('/comment/', methods = ['GET','POST'])
@login_required
def new_comment():
    form = CommentForm()
    comment = Comment.query.all()
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data 

        new_comment = Comment(comment=comment,title=title)

        new_comment.save_comments()
        return redirect(url_for('main.index'))

    return render_template('new_comment.html',comment_form=form, comments=comment)    