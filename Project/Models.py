from Project import db,login_manager
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def LoadUser(id):
    return User.query.get(id)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.Text,index=True)
    lname = db.Column(db.Text,index=True)
    email = db.Column(db.Text,unique=True)
    major = db.Column(db.Text,index=True)
    password = db.Column(db.Text)
    bio= db.Column(db.String(80),index=True)
    badges = db.Column(db.Text,index=True)
    #one to many relationship 
    posts = db.relationship("Posts",back_populates='author',lazy=True)
    def __init__(self,fname,lname,email,major,password,bio,badge):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.major = major
        self.password = generate_password_hash(password)
        self.bio = bio
        self.badges = badge
    def checkpass(self,pasw):
        return check_password_hash(self.password,pasw)
    
         

class Posts(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    topic = db.Column(db.Text)
    picture_path = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    typeofpost = db.Column(db.Text,nullable=False,server_default="public")
    likes = db.relationship("Likes",back_populates='PostLiked',lazy=True)
    liking_users = db.relationship(
        "User",
        secondary="likes", # اللينك Posts.liking_users 
        backref="liked_posts", #liked_posts in User Model
        lazy="dynamic"
    )
    author = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comments",back_populates='post')

    def __init__(self,topic,path,author,typeofpost):
        self.topic=topic
        self.picture_path=path
        self.author = author
        self.typeofpost = typeofpost

        


class Followers(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    follower_id = db.Column(db.Integer,db.ForeignKey('user.id'))    
    user = db.relationship('User', foreign_keys=[user_id])
    follower = db.relationship('User', foreign_keys=[follower_id])
    def __init__(self,user_id,follower_id):
        self.user_id=user_id
        self.follower_id=follower_id

class Comments(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    post_id = db.Column(db.Integer,db.ForeignKey("posts.id"))
    commenter_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    commenttxt = db.Column(db.Text)
    posts = db.relationship('Posts',foreign_keys=[post_id])
    commenters = db.relationship("User",foreign_keys=[commenter_id])
    post = db.relationship('Posts',back_populates='comments')
    
    def __init__(self,post_id,commenter_id,comments):
        self.post_id=post_id
        self.commenter_id=commenter_id
        self.commenttxt=comments
    
class Likes(db.Model):
    likinguser = db.Column(db.Integer,db.ForeignKey("user.id"),primary_key=True)
    likedpost = db.Column(db.Integer,db.ForeignKey("posts.id"),primary_key=True)
    UserLiking = db.relationship("User",foreign_keys=[likinguser])
    PostLiked = db.relationship("Posts",foreign_keys=[likedpost])
    def __init__(self,likinguser,likedpost):
        self.likinguser = likinguser
        self.likedpost = likedpost

