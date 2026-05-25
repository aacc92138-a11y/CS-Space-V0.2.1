from flask import Blueprint

bp =Blueprint("Admin",__name__,template_folder='templates')

from Project.admin import views