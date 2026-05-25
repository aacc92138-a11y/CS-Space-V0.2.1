from flask import Blueprint

bp = Blueprint("Auth",__name__,template_folder='templates')

from Project.Auth import views
