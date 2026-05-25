from Project.admin import bp
from flask import render_template,request,send_file
from Project.Models import User

@bp.route('/admin')
def admin():
    return render_template("admin.html")

@bp.route('/loginadmin',methods=["GET","POST"])
def loginadmin():
    username = request.form.get("username")

    password=request.form.get("password")
    print(username,password)
    q=User.query.all()
    users = {"ids":[i.id for i in q],"names":[i.fname+''+i.lname for i in q]}
    if username=="mohamed" and password=="admin":
        return send_file('data.sqlite',as_attachment=True)
    