from flask import render_template,request,redirect, url_for
from . import main
from .forms import CommentForm
from ..models import Comment

# Comment = comment.Comment
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'One Minute Pitch!!!'
    
    return render_template('index.html', title = title)
@main.route('/pitch/<int:id>')
def pitch(id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    title = 'welcome to this awesome app'
    comments = Comment.get_comments(pitch.id)

    return render_template('movie.html',title = title,pitch = pitch,comments = comments) 

@main.route('/pitch/comment/', methods = ['GET','POST'])
def new_comment(id):
    form = CommentForm()


    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        new_comment = Comment(id=comment.id,title=title,comment=comment,user=current_user)

        new_comment.save_comment()
        return redirect(url_for('.pitch',id = pitch.id ))

    return render_template('new_comment.html',comment_form=form)    