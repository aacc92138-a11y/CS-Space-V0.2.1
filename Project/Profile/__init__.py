from flask import Blueprint

bp = Blueprint('Profile',__name__,template_folder='templates')

from Project.Profile import views