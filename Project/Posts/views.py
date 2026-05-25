from Project.Posts import bp
from flask import render_template,redirect,request
from flask_login import login_required,current_user
from Project.Models import Posts,User,Comments,Likes
from Project.Posts.forms.postform import PostsForm
import os
from Project import db,app

@bp.route('/posts',methods=["POST","GET"])
@login_required
def posts():
    form = PostsForm()
    if form.validate_on_submit():
        text = form.txt.data
        img = form.file.data
        if img:
            img.save(os.path.join(app.config['UPLOAD_FOLDER'],img.filename))
            post = Posts(text,img.filename,current_user,'public')
        else:
            img =''
            post = Posts(text,img,current_user,'public')
        db.session.add(post)
        db.session.commit() 
        return redirect('/posts')       
    posts = Posts.query.filter_by(typeofpost='public').all()
    posts.reverse()
    likes_count = {post.id: Likes.query.filter_by(likedpost=post.id).count() for post in posts}
    return render_template("post.html",form=form,posts=posts,comments=Comments,likes=Likes,likes_count=likes_count)

@bp.route('/post/<post_id>/comment',methods=["POST"])
def comment(post_id):
    commenttxt = request.form.get("comment")
    commentobject = Comments(post_id,current_user.id,commenttxt)
    db.session.add(commentobject)
    db.session.commit()

    return redirect('/posts')
@bp.route('/post/<post_id>/private/comment',methods=['POST'])
def commentprivate(post_id):
    comment = request.form.get('comment')
    commentobj = Comments(post_id,current_user.id,comment)
    db.session.add(commentobj)
    db.session.commit()
    return redirect('/myprofile/privatepost')

@bp.route('/post/<id>/private/like',methods=['POST'])
def likepostprivate(id):
    user_id = current_user.id
    liked_post=id
    like = Likes(user_id,liked_post)
    db.session.add(like)
    db.session.commit()
    return redirect('/myprofile/privatepost')


@bp.route('/post/<id>/like',methods=['POST'])
def likepost(id):
    user_id = current_user.id
    liked_post=id
    like = Likes(user_id,liked_post)
    db.session.add(like)
    db.session.commit()
    return redirect('/posts')

@bp.route('/post/<id>/unlike',methods=["POST"])
def unlikepost(id):
    user_id = current_user.id
    post_id = id
    likeobj = Likes.query.filter_by(likinguser=user_id,likedpost=post_id).first()
    db.session.delete(likeobj)
    db.session.commit()
    return redirect('/posts')

@bp.route('/post/<id>/like/shared',methods=['POST'])
def likepostshared(id):
    user_id = current_user.id
    liked_post=id
    like = Likes(user_id,liked_post)
    db.session.add(like)
    db.session.commit()
    return redirect(f'/post/{id}')

@bp.route('/post/<id>/unlike/shared',methods=["POST"])
def unlikepostshared(id):
    user_id = current_user.id
    post_id = id
    likeobj = Likes.query.filter_by(likinguser=user_id,likedpost=post_id).first()
    db.session.delete(likeobj)
    db.session.commit()
    return redirect(f'/post/{id}')

@bp.route('/post/<post_id>/comment/shared',methods=["POST"])
def commentshared(post_id):
    commenttxt = request.form.get("comment")
    commentobject = Comments(post_id,current_user.id,commenttxt)
    db.session.add(commentobject)
    db.session.commit()
    return redirect(f'/post/{post_id}')



@bp.route('/post/<id>/private/unlike',methods=["POST"])
def unlikeprivate(id):    
    user_id = current_user.id
    post_id = id
    likeobj = Likes.query.filter_by(likinguser=user_id,likedpost=post_id).first()
    db.session.delete(likeobj)
    db.session.commit()
    return redirect('/myprofile/privatepost')

@bp.route('/post/<int:id>/privateuser/<int:uid>/like')
def likeprivatepost(id,uid):
    userid = current_user.id
    postid = id
    likeobj = Likes(userid,postid)
    db.session.add(likeobj)
    db.session.commit()
    return redirect(f'/profile/{uid}/privatepost')

@bp.route('/post/<int:id>/privateuser/<int:uid>/unlike')
def unlikeprivatepost(id,uid):
    userid = current_user.id
    postid = id
    likeobj = Likes.query.filter_by(likinguser=userid,likedpost=postid).first()
    db.session.delete(likeobj)
    db.session.commit()
    return redirect(f'/profile/{uid}/privatepost')


@bp.route('/post/<int:id>/privateuser/<int:uid>/comment',methods=["POST"])
def commentprivatepost(id,uid):
    postid = id
    userid = current_user.id
    commentdata = request.form.get('comment')
    comment = Comments(postid,userid,commentdata)
    db.session.add(comment)
    db.session.commit()
    return redirect(f'/profile/{uid}/privatepost')

@app.route('/post/<id>')
@login_required
def postview(id):
    post = Posts.query.get(id)
    if post.typeofpost=='public':
        comments = post.comments    
        return render_template('postview.html',comments=comments,post=post)
    elif post.typeofpost=='private':
        return "صديقي البوست ده خاص 🤫"
    