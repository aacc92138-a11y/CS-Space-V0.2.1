from Project.Profile import bp
from flask_login import login_required,current_user
from flask import render_template,redirect
from Project.Models import User,Followers,Posts,Likes,Comments
from Project.Profile.forms.profileforms import Bio,Info
from Project.Profile.forms.privateprofforms import Form as PrivatePost
from Project import db,app
import os

@bp.route('/profile/<id>')
def profile(id):
    user = User.query.get(id)
    followers = Followers.query.filter_by(user_id=id).all()
    following = Followers.query.filter_by(follower_id=id).all()
    followersids = [i.follower_id for i in followers]
    posts = len(User.query.get(id).posts)
    userpublic = Posts.query.filter_by(typeofpost='public',user_id=id).all()
    followerscounter=len(followers)
    followingcounter = len(following)
    return render_template('profile.html',pid=id,user=user,posts=userpublic,postcounter=posts,count1=followerscounter,count2=followingcounter,followersids=followersids)

@bp.route('/myprofile',methods=["POST","GET"])
@login_required
def myprofile():
    form = Bio()
    form1=Info()
    if form.validate_on_submit():
        bio = form.bio.data
        user = User.query.get(current_user.id)
        user.bio=bio
        db.session.commit()
        return redirect('/myprofile')
    followers = Followers.query.filter_by(user_id=current_user.id).all()
    following = Followers.query.filter_by(follower_id=current_user.id).all()
    posts = len(User.query.get(current_user.id).posts)
    followerscounter=len(followers)
    followingcounter = len(following)
    user = current_user
    return render_template('myprofile.html',form=form,user=user,form1=form1,counter1=followerscounter,counter2=followingcounter,postscount=posts,followers=followers)

@bp.route('/edit',methods=["POST","GET"])
def update():
    form1=Info()
    if form1.validate_on_submit():
        fname = form1.fname.data
        lname = form1.lname.data 
        user = User.query.get(current_user.id)
        user.fname=fname
        user.lname=lname
        db.session.commit()
        
        return redirect('/myprofile')  
    
@bp.route('/FollowUser/<id>')
def Follow(id):
    FollowedUser=id
    FollowingUser = current_user.id
    FollowObj = Followers(FollowedUser,FollowingUser)
    db.session.add(FollowObj)
    db.session.commit()    
    return redirect(f'/profile/{id}')
@bp.route('/UnFollowUser/<id>')
def UnFollow(id):
    FollowedUser=id
    FollowingUser = current_user.id
    FollowObj = Followers.query.filter_by(user_id=FollowedUser,follower_id=FollowingUser).first()
    db.session.delete(FollowObj)
    db.session.commit()    
    return redirect(f'/profile/{id}')

@login_required
@bp.route('/myprofile/privatepost',methods=["GET","POST"])
def ProfilePrivate():
    form = PrivatePost()
    id = current_user.id
    name = current_user.fname + current_user.lname
    followers = Followers.query.filter_by(user_id=current_user.id).all()
    following = Followers.query.filter_by(follower_id=current_user.id).all()
    followerscounter=len(followers)
    followingcounter = len(following)
    actualposts=Posts.query.filter_by(user_id=id,typeofpost='private').all()
    postsc = len(Posts.query.filter_by(user_id=id,typeofpost='private').all())
    user = current_user
    likes = Likes
    posts = Posts.query.all()
    posts.reverse()
    likes_count = {post.id: Likes.query.filter_by(likedpost=post.id).count() for post in posts}
    if form.validate_on_submit():
        posttxt = form.user_input.data
        image = form.image.data
        if image:
            image.save(os.path.join(app.config['UPLOAD_FOLDER'],image.filename))
            post = Posts(posttxt,image.filename,current_user,'private')
        else:
            image =''
            post = Posts(posttxt,image,current_user,'private')
        db.session.add(post)
        db.session.commit()

        return redirect(f'/profile/{id}/privatepost')
    
    return render_template("privateposts/UserPrivate.html",form=form,likes=likes,likes_count=likes_count,comments=Comments,postcount=postsc,id=id,name=name,fcount = followerscounter,fingcount=followingcounter,user=user,postsobj=actualposts)
@login_required
@bp.route('/profile/<int:id>/privatepost')
def privatepostsforuser(id):
    user = User.query.get(id)
    posts = Posts.query.filter_by(author=user,typeofpost="private").all()
    followers = Followers.query.filter_by(user_id=id).all()
    following = Followers.query.filter_by(follower_id=id).all()
    followerscounter=len(followers)
    followingcounter = len(following)
    postscount = len(Posts.query.filter_by(user_id=id,typeofpost='private').all())
    current_user_followers = Followers.query.filter_by(user_id=current_user.id)
    print(current_user.id,[i.user_id for i in followers])
    if current_user.id != id:
        if current_user.id in [i.follower_id for i in followers] and id in [j.follower_id for j in current_user_followers]:
            return render_template('privateposts/FollowersPrivate.html',pid=id,likes=Likes,comments=Comments,fcount=followerscounter,fingcount=followingcounter,postc=postscount,user=user,posts=posts)
        else:
            if current_user.id not in [i.user_id for i in followers]:
                return "انت مش من متابعين المستخدم"
            elif id not in [j.user_id for j in current_user_followers]:
                return "المستخدم ده مش متابعك خليه يتابعك عشان تشوفوا بوستات بعض"
    else:
        return render_template("privateposts/FollowersPrivate.html",pid=id,likes=Likes,comments=Comments,fcount=followerscounter,fingcount=followingcounter,postc=postscount,user=user,posts=posts)        
