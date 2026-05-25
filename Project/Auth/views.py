from Project.Auth import bp
from Project.Auth.forms.signupf import SignUp
from Project.Auth.forms.signin import SignIn
from flask import render_template,flash,redirect,url_for,request
from Project.Models import User
from Project import db
from flask_login import login_user,logout_user,login_required

@bp.route("/signup",methods=["POST","GET"])
def signup():
    form = SignUp()
    if form.validate_on_submit():
        fname = form.firstName.data
        lname = form.lastName.data
        email = form.Email.data
        password = form.Password.data
        major = form.major.data
        names = [
        "..","AbdalrhmanKhalaf","AbdullahKharshom","Ahmed Belal","Ahmed Elmahdy",
        "Ahmed Fashwer","Ahmed Hrakat","Ahmed shetaya","Ahmed Soliman","AiselElgazar",
        "AliA. Aboselima ","Amr Wael ","Afnan Rafeek ","AyaOmar","BadrElswisy",
        "Esraa Hegazy ","FayedMohamed","GamalAlbhrawy","GannaAhmed","HaniEl meligi",
        "Maryam M","MalakMohamed Ali","Marlon'sTwin","MennaMohammed Abdalaziz",
        "MenaMonir","Mohamed Elemary","MohamedElsherbiny","MohamedMahmoud",
        "MohamedSameh","MohamedZaghmour","MohamedElemary","Momoمرجان","MosayaMossa",
        "Mmmm99","MawadaAhmed","Nour19","NourEldean","OmarAl-Dahshan","OmarFarouk",
        "OmarZahran","OsamaElsalomy","Rahma Sadoon ","RahmaMohammed ","RaghadEbrahim",
        "RoaaGhoneim","SaadZahran","SalmaHany","SamaFayed","ShahdFadel","ShahdGabr",
        "YasserShahbou","Zينسليم","amanyreda","haneenelsaqqa","hussien Mamdouh",
        "leenahtarek","youseffelfel","إياد حماده","أحمد محمد","اسرالفتاجيلي",
        "الناكحً","ايادصقر","حنين احمد","حامد البيسي","سما حامد","سيف الدسوقي19",
        "صالحياسر ","عادل الصياد","عاصمالبن","عصامطارق ","عمرمجدي","عمادشرف",
        "عمرو    الشمنهوري","على ابراهيم ","عائشة حسين ","عبد الرحمن محمد زكريا الطاووسي",
        "عبدالله عباس خفاجي","عبدالرحمن","عبدالرحمنالخميسى","عبدالرحمنمحمد",
        "محمد أيمن العمرى","محمد أيمنالعمرى","محمد فليه","محمد البحيري ",
        "محمد الديب","محمد سالم","محمد عبدهجاده","محمد عمرو","محمد محمد",
        "محمد وائل","محمد العرباني","محمد البدراي","محمدhamoda","محمودالبديوى",
        "مريمالانصاري","مريم أبو الدهب ","مريم محمد","ملكعتمان","مهنداحمد",
        "ندى الشربيني","نادين وائل","نورالاعصر","نوراسعد'","نورين الداجن ",
        "نورهان عزيز ","يارا المنسى","ياراغنيم","لمياء عيسي","جنةطارق",
        "شهدالقصاص"
        ]
        if fname+''+lname in names:
            user = User(fname,lname,email,major,password,'عدل البايو','diamond')
        else:    
            user = User(fname,lname,email,major,password,'عدل البايو','classic')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('Auth.signin'))
    return render_template("signup.html",form=form)

@bp.route('/signin',methods=["POST","GET"])
def signin():
    signin = SignIn()
    if signin.validate_on_submit():
        email = signin.Email.data
        password = signin.Password.data
        if User.query.filter_by(email=email):
            user = User.query.filter_by(email=email).first()
            if user and user.checkpass(password):
                flash("Signed In")
                login_user(user)                
                return redirect(url_for('Home.index'))
            else:
                return "invalid credentials"
    return render_template('signin.html',form=signin)

@bp.route('/logout')
@login_required
def logout(): 
    logout_user()
    return redirect(url_for('Home.index'))

@bp.route('/vip')
def vipusers():
    return render_template('vip.html')

@bp.route('/vip/action',methods=["POST"])
def UpdateBadge():
    name = request.form.get('name')
    password = request.form.get("password")
    idm = request.form.get('id')
    choice = request.form.get('choices')
    print(choice)
    if name=='mohamed' and password=='admin':
        user = User.query.get(int(idm))
        print(user.badges)
        if choice == 'Badge':
            user.badges='diamond'
            db.session.commit()
        elif choice == 'Delete':
            posts=user.posts
            for j in posts:
                likes=j.likes
                comments = j.comments
                for k in likes:
                    db.session.delete(k)
                for l in comments:
                    db.session.delete(l)    
                db.session.delete(j)
            db.session.delete(user)
            db.session.commit()
        return redirect('/vip')
    return 'invalid action'