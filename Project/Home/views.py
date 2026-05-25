from Project.Home import bp
from flask import render_template,redirect,flash
from Project import login_manager
from Project.Models import User

@bp.route('/',methods=["POST","GET"])
def index():
    return render_template('index.html')

