from flask import Blueprint

bp = Blueprint("Post",__name__,template_folder='templates')

from Project.Posts import views