from flask import Blueprint

bp = Blueprint('Home',__name__,template_folder='templates')

from Project.Home import views